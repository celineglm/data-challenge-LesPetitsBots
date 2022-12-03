import re
import faker

from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

from app.model.Whitelist import get_data

class Parser:

    nlp : pipeline = None
    customFilters : list


    def __init__(self, customFilters: list) -> None:
        tokenizer = AutoTokenizer.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
        model = AutoModelForTokenClassification.from_pretrained("Jean-Baptiste/camembert-ner-with-dates")
        self.nlp = pipeline('ner', model=model, tokenizer=tokenizer, aggregation_strategy="simple")

        self.customFilters = customFilters

    def _intermediate_parser(self, sentence : str, processedList: list, regex : str, tag : str):
        reg = re.compile(regex)

        s = re.fullmatch(reg, sentence)

        if s:
            newList = [{'entity_group': tag, 'score': 1.0, 'word': sentence[s.start(): s.end()], 'start': s.start(), 'end': s.end()}]
            for e in processedList:
                # Check if there is overlapping between MAIL and other tags
                if not (e['start'] >= newList[0]['start'] and e['end'] <= newList[0]['end']):
                    newList.append(e)
                    
            return newList

        return processedList

    def parse(self, sentence : str):
        processedList = self.nlp(sentence)

        newList = []
        for element in processedList:
            if element['score'] > 0.9:
                newList.append(element)

        for filter in self.customFilters:
            newList = self._intermediate_parser(sentence, newList, filter['regex'], filter['tag'])

        if newList:
            whitelist = get_data()

            tmpList = []
            for element in newList:
                if element['word'] not in whitelist:
                    tmpList.append(element)
            newList = tmpList

        return newList

    def replace_by_tag(self, sentence : str, processedList : list):
        for element in processedList:
            sentence = sentence.replace(element['word'], element['entity_group'])

        return sentence

    def replace_by_fake(self, sentence : str, processedList : list):
        fake = faker.Faker('fr_FR')

        for element in processedList:
            if(element['entity_group'] == 'PER'):
                sentence = sentence.replace(element['word'], fake.name())
            elif(element['entity_group'] == 'LOC'):
                sentence = sentence.replace(element['word'], fake.address())
            elif(element['entity_group'] == 'DATE'):
                sentence = sentence.replace(element['word'], fake.date())
            elif(element['entity_group'] == 'ORG'): 
                sentence = sentence.replace(element['word'], fake.company())
            elif(element['entity_group'] == 'MAIL'):
                sentence = sentence.replace(element['word'], fake.ascii_free_email())
            elif(element['entity_group'] == 'PHONE'):
                sentence = sentence.replace(element['word'], fake.phone_number())
            elif(element['entity_group'] == 'IBAN'):
                sentence = sentence.replace(element['word'], fake.iban())
            else:
                sentence = sentence.replace(element['word'], element['entity_group'])

        return sentence