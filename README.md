<img width="428" height="277" alt="image" src="https://github.com/user-attachments/assets/200fb030-9003-407f-bae5-6896508b1f63" /><img width="428" height="277" alt="image" src="https://github.com/user-attachments/assets/76b8922c-27a1-41a0-bf91-a83e65d911ce" /># 🚩 `revolution`
Gadget pour afficher des citations marxistes dans le terminal Linux, inspiré de la commande `fortune`.

## Installation

### Méthode 1 : Via Git (recommandé)
```bash
git clone https://github.com/Kzaark/revolution.git
cd revolution/
chmod +x install.sh
sudo ./install.sh
```

### Méthode 2 : Téléchargement direct
1. Télécharge le dernier release ou clone du dépôt.
2. Suis les mêmes étapes que précédemment.

## Utilisation
```bash
revolution                    → Affiche une citation aléatoire parmi tous les auteurs
revolution <auteur>           → Affiche une citation d'un auteur précis
revolution --all <auteur>     → Affiche toutes les citations d'un auteur
revolution --random <N>       → Affiche N citations aléatoires
revolution --search <mot>     → Recherche un mot dans toutes les citations
revolution --list             → Liste tous les auteurs disponibles
revolution --aliases          → Liste tous les alias disponibles
revolution --update           → Met à jour revolution
revolution --help             → Affiche l'aide
```

## Mise à jour

Une fois installé, tu peux mettre à jour revolution directement depuis le terminal :
```bash
revolution --update
```

## Intégration au terminal

Pour afficher une citation à chaque ouverture de terminal, ajoute cette ligne à ton `~/.bashrc` ou `~/.zshrc` :

```bash
revolution
```

Puis recharge la config :
```bash
source ~/.bashrc  # ou source ~/.zshrc
```

## Personnalisation

### Ajouter un nouvel auteur

1. Crée un fichier texte (ex : `"bordiga"`) dans le dossier du projet avec les citations :
```
" citation texte. " (ouvrage/source)
%
" deuxième citation. "
```
Chaque citation doit être séparée par un `%` obligatoirement.

2. Ajoute-le dans `revolution.py` :
```python
AUTEURS_CONFIG = {
    "bordiga": {"nom": "Amadeo Bordiga"},
    ...
}
```

### Ajouter un alias

Modifie `revolution.py` :
```python
AUTEURS_ALIASES = {
    "trotski": "trotsky",
    "marxengels": "marx-engels",
}
```

## Désinstallation
```bash
sudo ./uninstall.sh
```

## Infos diverses
Environ une quinzaine de citations par auteur.

Compatible avec les commandes `cowsay` et `lolcat`.

![Fortune + Cowsay.](https://github.com/Kzaark/revolution/blob/main/static/images/revolution-cowsay.png?raw=true) `fortune | cowsay`
![Fortune + Lolcat.](https://github.com/Kzaark/revolution/blob/main/static/images/revolution-lolcat.png?raw=true) `fortune | lolcat`
![Fortune + Cowsay + Lolcat.](<img width="428" height="277" alt="image" src="https://github.com/user-attachments/assets/96f72d3d-3d67-4b2e-a49f-622f71a69730" />) Ultime : `fortune | cowsay | lolcat`


### Liste des auteurs
- Friedrich Engels
- Karl Marx
  - Karl Marx et Friedrich Engels (citations communes)
- Lénine
- Rosa Luxemburg
- Léon Trotsky
- Clara Zetkin
- Antonio Gramsci
- Amadeo Bordiga
- Alexandra Kollontaï
- Raya Dunayevskaya

### Alias déjà enregistrés
- `trotski` --> `trotsky`
- `marxengels` --> `marx-engels`
- `engelsmarx` --> `marx-engels`
- `engels-marx` --> `marx-engels`
- `kollontaï` --> `kollontai`

## Licence
[GNU GPL-3.0](https://github.com/Kzaark/revolution/blob/main/LICENCE)
