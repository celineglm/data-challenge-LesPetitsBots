import re
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

        s = reg.search(sentence)

        if s:
            newList = [{'entity_group': tag, 'score': 1.0, 'word': sentence[s.start(): s.end()], 'start': s.start(), 'end': s.end()}]
            for e in processedList:
                # Check if there is overlapping between MAIL and other tags
                if not (e['start'] >= newList[0]['start'] and e['end'] <= newList[0]['end']):
                    newList.append(e)
                    
                return newList

    def parse(self, sentence : str):
        processedList = self.nlp(sentence)

        for filter in self.customFilters:
            processedList = self._intermediate_parser(sentence, processedList, filter['regex'], filter['tag'])

        if processedList:
            #White list
            whitelist = get_data()

            newList = []
            for element in processedList:
                if element['word'] not in whitelist.values:
                    newList.append(element)

            return newList 

        return processedList