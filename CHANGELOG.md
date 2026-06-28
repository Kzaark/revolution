# Changelog

## [1.3.0] - 2026-06-28

### Nouveautés
- Colorisation native de la sortie (citations en jaune, auteurs en rouge, sources en italique)
- Ajout de l'option `--version` / `-v`


## [1.1.0] - 2026-06-28

### Ajout(s)
- `--all <auteur>` : affiche toutes les citations d'un auteur
- `--random <N>` : affiche N citations aléatoires
- `--search <mot>` : recherche un mot dans toutes les citations
- `--list` : liste tous les auteurs disponibles
- `--aliases` : liste tous les alias disponibles
- `--help` / `-h` : affiche l'aide

### Correction(s)
- Chemin incorrect dans `install.sh` (`terminal-fortunes` → `revolution`)
- Les alias n'étaient pas implémentés dans le code
- Le filtre de fichiers ramassait `revolution.py` et `README.md` en plus des citations
- Typo dans le `git clone` du README

### Amélioration(s)
- Check `python3` ajouté dans `install.sh` avant l'installation
- Messages d'erreur plus explicites avec suggestion `--list`

## [1.0.0] - 2025

### Ajout(s)
- Affichage de citations aléatoires parmi tous les auteurs
- Sélection d'un auteur par nom
- Système d'alias
- Script d'installation et de désinstallation
- Auteurs : Karl Marx, Friedrich Engels, Marx & Engels, Lénine, Léon Trotsky, Rosa Luxemburg, Clara Zetkin
