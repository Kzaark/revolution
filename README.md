# Revolution
Gadget pour afficher des citations marxistes dans son terminal, inspiré de la commande 'fortune'.

## Installation

### Méthode 1 : Via Git (recommandé)
```bash
git clone https://github.com/Kzaark/revoluion.git
cd revolution/
chmod +x install.sh
sudo ./install.sh

### Méthode 2 : Téléchargement direct
1. Télécharge le dernier release ou clone ce dépôt.
2. Suis les même étape de précédemment.

# Utilisation 
revolution : Affiche une citation aléatoire
revolution <auteur> ex : lenine : Affiche une citation de Lénine
revolution trotski : fonctionne aussi avec des alias (trotski --> trotsky)

# Personnalisation

## Ajouter un nouvel auteur

1. Créer un fichier texte (ex : Bordiga) dans le dossier du projet avec les ciations :
" citation texte. " (ouvrage/source)
%
" deuxième ciation. "

2. Ajoute-le dans le scripts/revolution.py :
AUTEURS_CONFIG = {
	"bordiga": {"nom" : "Amadeo Bordiga"},
	...
}


## Ajouter un alias

Modifie scripts/revolution.py :
AUTEURS_ALIASES = {
	"trotski" : "trotsky",
	"marxengels": "marx-engels",
}

# Désinstallation

sudo ./uninstall.sh

# Licence
 MIT
