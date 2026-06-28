#!/usr/bin/env python3
# revolution — Citations marxistes dans le terminal
# Copyright (C) 2026 Kzaark
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import random
import sys
import os
import re
import subprocess
from easteregg import afficher_easteregg

# Chemin
FORTUNES_DIR = "/usr/local/share/revolution"

# Configuration auteurs
AUTEURS_CONFIG = {
    "bordiga": {"nom": "Amadeo Bordiga"},
    "dunayevskaya": {"nom": "Raya Dunayevskaya"},
    "marx": {"nom": "Karl Marx"},
    "engels": {"nom": "Friedrich Engels"},
    "marx-engels": {"nom": "Marx & Engels"},
    "gramsci": {"nom": "Antonio Gramsci"},
    "kollontai": {"nom": "Alexandra Kollontaï"},
    "lenine": {"nom": "Lénine"},
    "trotsky": {"nom": "Léon Trotsky"},
    "luxemburg": {"nom": "Rosa Luxemburg"},
    "zetkin": {"nom": "Clara Zetkin"},
}

# Alias
AUTEURS_ALIASES = {
    "trotski": "trotsky",
    "marxengels": "marx-engels",
    "engelsmarx": "marx-engels",
    "engels-marx": "marx-engels",
    "kollontaï": "kollontai",
}

def lire_citations(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        contenu = f.read()
    return [c.strip() for c in contenu.split('%') if c.strip()]

def extraire_source(citation):
    match = re.search(r'\s*\(([^)]+)\)\s*$', citation)
    if match:
        return citation[:match.start()].strip(), match.group(1)
    return citation, None

def afficher_aide():
    print("""
revolution — Citations marxistes dans ton terminal

Usage :
  revolution                    Affiche une citation aléatoire
  revolution <auteur>           Affiche une citation d'un auteur précis
  revolution --all <auteur>     Affiche toutes les citations d'un auteur
  revolution --random <N>       Affiche N citations aléatoires
  revolution --search <mot>     Recherche un mot dans toutes les citations
  revolution --list             Liste tous les auteurs disponibles
  revolution --aliases          Liste tous les alias disponibles
  revolution --update           Met à jour revolution
  revolution --help             Affiche ce message

Exemples :
  revolution lenine
  revolution trotski
  revolution --all luxemburg
  revolution --random 5
  revolution --search liberté
  revolution --list
""")

def lister_auteurs():
    print("Auteurs disponibles :\n")
    for cle, valeur in AUTEURS_CONFIG.items():
        print(f"  {cle:<15} → {valeur['nom']}")

def lister_aliases():
    print("Alias disponibles :\n")
    for alias, cible in AUTEURS_ALIASES.items():
        print(f"  {alias:<15} → {cible}")

def mettre_a_jour():
    print("Mise à jour de revolution...")
    result = subprocess.run(["git", "-C", FORTUNES_DIR, "pull"], capture_output=True, text=True)
    if result.returncode == 0:
        print("✓ Mise à jour réussie !")
        print(result.stdout)
    else:
        print("✗ Erreur lors de la mise à jour :")
        print(result.stderr)

def afficher_toutes_citations(auteur):
    auteur = AUTEURS_ALIASES.get(auteur, auteur)

    if auteur not in