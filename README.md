# Data-Challenge-LesPetitsBots

Projet réalisé lors du Data Challenge organisé par IA Pau du 2 au 4 décembre 2022

## Installation

`pip install -r requirements.txt`

## Utilisation

`uvicorn app.main:app`

Le serveur est lancé sur le `localhost:8000`, et vous pouvez avoir accès à la documentation de chaque fonction sur `localhost:8000/docs`

## Filtres

Vous avez la possibilité de rajouter des filtres à base d'expression `regex` pour filtrer certaines informations précises, comme des numéros de dossier.  

Un filtre doit avoir cette forme
```py
{
    'name': "Nom du filtre",
    'regex': r"Expression régulière",
    'tag': "TAG"
}
```

## Whitelist

Vous avez la possibilité de whitelister certains mots pour qu'ils ne soient pas anonymisés.
Elle utilise un fichier `.csv` avec une seule colonne, stockée dans `app/data/whitelist.csv`. Attention, c'est un correspondance stricte.

|words|
|:-|
|exemple|
|...|
