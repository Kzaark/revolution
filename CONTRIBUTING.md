# Contribuer à revolution

Merci de ton intérêt pour le projet ! Voici comment tu peux contribuer.

## Ajouter des citations

1. Ouvre le fichier correspondant à l'auteur (ex : `marx`, `lenine`, etc.).

2. Ajoute ta citation en respectant le format :
```
" texte de la citation. " (ouvrage/source si existant)
%
```

3. Vérifie que chaque citation est bien séparée par un `%` seul sur sa ligne.

4. Ouvre une Pull Request avec tes ajouts

## Ajouter un auteur

1. Crée un fichier texte à la racine du projet avec le nom de l'auteur en minuscules (ex : `gramsci`)
2. Ajoute au moins 5 citations dans ce fichier en respectant le format ci-dessus
3. Ajoute l'auteur dans `revolution.py` :
```python
AUTEURS_CONFIG = {
    "gramsci": {"nom": "Antonio Gramsci"},
    ...
}
```
4. Ouvre une Pull Request


## Ajouter un alias

Modifie `revolution.py` :
```python
AUTEURS_ALIASES = {
    "ton_alias": "auteur_cible",
    ...
}
```

## Signaler un bug

Ouvre une [Issue](https://github.com/Kzaark/revolution/issues) en décrivant :
- Ce que tu as fait
- Ce que tu attendais
- Ce qui s'est passé à la place

## Proposer une fonctionnalité

Ouvre une [Issue](https://github.com/Kzaark/revolution/issues) avec le tag `enhancement` et décris ta proposition.

## Règles générales

- Les citations doivent être sourcées (ouvrage ou discours si possible).
- Les auteurs doivent s'inscrire dans les courants marxistes du projet.
- Le code doit rester compatible Python 3.
- Respecte le style du code existant