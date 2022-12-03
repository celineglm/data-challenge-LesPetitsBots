from app.model.Parser import Parser
from fastapi.responses import JSONResponse

from fastapi import APIRouter
router = APIRouter()

customFilters = [
    {
        'name': "Mail",
        'regex': r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
        'tag': "MAIL"
    },
    {
        'name': "Phone number",
        'regex': r"(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}",
        'tag': "PHONE"
    },
    {
        'name': "Passeport number",
        'regex': r"[0-9]{2}[A-z]{2}[0-9]{5}",
        'tag': "PASSEPORT"
    },
    {
        'name': "Credit card",
        'regex': r"\b((4\d{3}|5[1-5]\d{2}|2\d{3}|3[47]\d{1,2})[\s\-]?\d{4,6}[\s\-]?\d{4,6}?([\s\-]\d{3,4})?(\d{3})?)\b",
        'tag': "CARD"
    },
    {
        'name': "IBAN",
        'regex': r"(?:(?:IT|SM)\d{2}[\w]\d{22}|CY\d{2}[\w]\d{23}|NL\d{2}[\w]{4}\d{10}|LV\d{2}[\w]{4}\d{13}|(?:BG|BH|GB|IE)\d{2}[\w]{4}\d{14}|GI\d{2}[\w]{4}\d{15}|RO\d{2}[\w]{4}\d{16}|KW\d{2}[\w]{4}\d{22}|MT\d{2}[\w]{4}\d{23}|NO\d{13}|(?:DK|FI|GL|FO)\d{16}|MK\d{17}|(?:AT|EE|KZ|LU|XK)\d{18}|(?:BA|HR|LI|CH|CR)\d{19}|(?:GE|DE|LT|ME|RS)\d{20}|IL\d{21}|(?:AD|CZ|ES|MD|SA)\d{22}|PT\d{23}|(?:BE|IS)\d{24}|(?:FR|MR|MC)\d{25}|(?:AL|DO|LB|PL)\d{26}|(?:AZ|HU)\d{27}|(?:GR|MU)\d{28})",
        'tag': "IBAN"
    },
    {
        'name': "National card number",
        'regex': r"\b\b\d{12}\b\b",
        'tag': "CNI"
    },
    {
        'name': "Social security number",
        'regex': r"\b\d{13}|\d{13}\s\d{2}\b",
        'tag': "SOCIALSEC"
    }
]

parser = Parser(customFilters)

@router.post("/api/predict")
async def predict_anonymous_data(sentence : str):
    res = parser.parse(sentence)
    return JSONResponse(content=res)

@router.post("/api/predict/tag")
async def replace_text_by_tag(sentence : str):
    return {"Le modèle a prédit que ce texte contient ces données sensibles" :"balalala" }

@router.post("/api/predict/fakedata")
async def replace_text_by_fakedata(sentence : str):
    return {"Le modèle a prédit que ce texte contient ces données sensibles" :"balalala" }