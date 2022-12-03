# Data-Challenge-LesPetitsBots

Projet réalisé lors du Data Challenge du 2 au 4 décembre 2022

## Installation

`pip install -r requirements.txt`

## Utilisation

`uvicorn app.main:app`

## Filtres

Vous avez la possibilité de rajouter des filtres à base d'expression `regex` pour filtrer certaines informations précises, comme des numéros de dossier.  

Un filtre doit avoir cette forme :
```py
{
    'name': "Nom du filtre",
    'regex': r"Expression régulière",
    'tag': "TAG"
}
```

## Whitelist

Vous avez la possibilité de whitelister certains mots pour qu'ils ne soient pas anonymisés.