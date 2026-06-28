# 🚩 `revolution`

Gadget pour afficher des citations marxistes dans le terminal Linux, inspiré de la commande `fortune`.

![Licence](https://img.shields.io/badge/licence-GPL--3.0-red?style=flat-square)
![Python](https://img.shields.io/badge/python-3.x-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey?style=flat-square&logo=linux)
![Terminal](https://img.shields.io/badge/terminal-bash%20%7C%20zsh%20%7C%20fish-black?style=flat-square)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen?style=flat-square)

---

## Table des matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exemple de sortie](#exemple-de-sortie)
- [Mise à jour](#mise-à-jour)
- [Intégration au terminal](#intégration-au-terminal)
- [Personnalisation](#personnalisation)
- [Désinstallation](#désinstallation)
- [Infos diverses](#infos-diverses)
- [Licence](#licence)

---

## Prérequis

- Python 3.x
- Git
- (Optionnel) `cowsay` et/ou `lolcat` pour les combinaisons fun

```bash
sudo apt install cowsay lolcat   # Debian/Ubuntu
sudo pacman -S cowsay lolcat     # Arch
brew install cowsay lolcat       # macOS
```

---

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

---

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

---

## Exemple de sortie

```
$ revolution lénine

« Toute révolution n'a de valeur que si elle sait se défendre. »
  — Lénine
```

---

## Mise à jour
Une fois installé, tu peux mettre à jour revolution directement depuis le terminal :
```bash
revolution --update
```

---

## Intégration au terminal
Compatible avec **Bash**, **Zsh** et **Fish**.

Pour afficher une citation à chaque ouverture de terminal, ajoute cette ligne à ton fichier de config :

| Shell | Fichier de config |
|-------|-------------------|
| Bash  | `~/.bashrc` |
| Zsh   | `~/.zshrc` |
| Fish  | `~/.config/fish/config.fish` |

```bash
revolution
```

Puis recharge la config :
```bash
source ~/.bashrc   # Bash
source ~/.zshrc    # Zsh
exec fish          # Fish
```

---

## Personnalisation

### Ajouter un nouvel auteur
1. Crée un fichier texte (ex : `bordiga`) dans le dossier du projet avec les citations :
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

---

## Désinstallation
```bash
sudo ./uninstall.sh
```

---

## Infos diverses

Environ une quinzaine de citations par auteur.  
Compatible avec les commandes `cowsay` et `lolcat`.

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://github.com/Kzaark/revolution/blob/main/static/images/revolution-cowsay.png?raw=true" alt="revolution | cowsay" width="428" height="277" /><br/>
        <code>revolution | cowsay</code>
      </td>
      <td align="center">
        <img src="https://github.com/Kzaark/revolution/blob/main/static/images/revolution-lolcat.png?raw=true" alt="revolution | lolcat" width="428" height="277" /><br/>
        <code>revolution | lolcat</code>
      </td>
    </tr>
    <tr>
      <td colspan="2" align="center">
        <img src="https://github.com/user-attachments/assets/96f72d3d-3d67-4b2e-a49f-622f71a69730" alt="revolution | cowsay | lolcat" width="428" height="277" /><br/>
        Ultime : <code>revolution | cowsay | lolcat</code>
      </td>
    </tr>
  </table>
</div>

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
- `trotski` → `trotsky`
- `marxengels` → `marx-engels`
- `engelsmarx` → `marx-engels`
- `engels-marx` → `marx-engels`
- `kollontaï` → `kollontai`

---

## Licence
[GNU GPL-3.0](https://github.com/Kzaark/revolution/blob/main/LICENCE)
