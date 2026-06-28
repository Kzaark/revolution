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

# Chemin
FORTUNES_DIR = "/usr/local/share/revolution"

# Configuration auteurs
AUTEURS_CONFIG = {
    "marx": {"nom": "Karl Marx"},
    "engels": {"nom": "Friedrich Engels"},
    "marx-engels": {"nom": "Marx & Engels"},
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

def afficher_toutes_citations(auteur):
    auteur = AUTEURS_ALIASES.get(auteur, auteur)

    if auteur not in AUTEURS_CONFIG:
        print(f"Auteur '{auteur}' introuvable. Lance 'revolution --list' pour voir les auteurs disponibles.")
        return

    chemin = os.path.join(FORTUNES_DIR, auteur)
    citations = lire_citations(chemin)

    if not citations:
        print(f"Aucun contenu pour '{auteur}'.")
        return

    nom_auteur = AUTEURS_CONFIG[auteur]["nom"]
    print(f"=== {nom_auteur} ({len(citations)} citations) ===\n")

    for i, citation in enumerate(citations, 1):
        texte, source = extraire_source(citation)
        print(texte)
        print()
        print(f"    -- {nom_auteur}" + (f", \033[3m{source}\033[0m" if source else ""))
        if i < len(citations):
            print("\n" + "─" * 40 + "\n")

def afficher_citations_aleatoires(n):
    fichiers = [f for f in os.listdir(FORTUNES_DIR) if f in AUTEURS_CONFIG]
    toutes = []
    for fichier in fichiers:
        citations = lire_citations(os.path.join(FORTUNES_DIR, fichier))
        for citation in citations:
            toutes.append((fichier, citation))

    if not toutes:
        print("Aucune citation trouvée.")
        return

    selection = random.sample(toutes, min(n, len(toutes)))

    for i, (fichier, citation) in enumerate(selection, 1):
        texte, source = extraire_source(citation)
        nom_auteur = AUTEURS_CONFIG[fichier]["nom"]
        print(texte)
        print()
        print(f"    -- {nom_auteur}" + (f", \033[3m{source}\033[0m" if source else ""))
        if i < len(selection):
            print("\n" + "─" * 40 + "\n")

def rechercher_citations(mot):
    fichiers = [f for f in os.listdir(FORTUNES_DIR) if f in AUTEURS_CONFIG]
    resultats = []

    for fichier in fichiers:
        citations = lire_citations(os.path.join(FORTUNES_DIR, fichier))
        for citation in citations:
            if mot.lower() in citation.lower():
                resultats.append((fichier, citation))

    if not resultats:
        print(f"Aucune citation trouvée pour '{mot}'.")
        return

    print(f"{len(resultats)} citation(s) trouvée(s) pour '{mot}' :\n")
    for i, (fichier, citation) in enumerate(resultats, 1):
        texte, source = extraire_source(citation)
        nom_auteur = AUTEURS_CONFIG[fichier]["nom"]
        print(texte)
        print()
        print(f"    -- {nom_auteur}" + (f", \033[3m{source}\033[0m" if source else ""))
        if i < len(resultats):
            print("\n" + "─" * 40 + "\n")

def afficher_citation(auteur=None):
    if auteur:
        auteur = AUTEURS_ALIASES.get(auteur, auteur)

    fichiers = [f for f in os.listdir(FORTUNES_DIR) if f in AUTEURS_CONFIG]

    if not fichiers:
        print(f"Aucun fichier trouvé dans {FORTUNES_DIR}")
        return

    fichier = random.choice(fichiers) if not auteur else next((f for f in fichiers if f == auteur), None)
    if not fichier:
        print(f"Auteur '{auteur}' introuvable. Lance 'revolution --list' pour voir les auteurs disponibles.")
        return

    citations = lire_citations(os.path.join(FORTUNES_DIR, fichier))
    if not citations:
        print(f"Aucun contenu dans {fichier}.")
        return

    citation, source = extraire_source(random.choice(citations))
    nom_auteur = AUTEURS_CONFIG.get(fichier, {}).get("nom", fichier)

    print(citation)
    print()
    print(f"    -- {nom_auteur}" + (f", \033[3m{source}\033[0m" if source else ""))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("--help", "-h"):
        afficher_aide()
    elif len(sys.argv) > 1 and sys.argv[1] == "--list":
        lister_auteurs()
    elif len(sys.argv) > 1 and sys.argv[1] == "--aliases":
        lister_aliases()
    elif len(sys.argv) > 2 and sys.argv[1] == "--all":
        afficher_toutes_citations(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == "--all":
        print("Usage : revolution --all <auteur>")
    elif len(sys.argv) > 2 and sys.argv[1] == "--random":
        try:
            afficher_citations_aleatoires(int(sys.argv[2]))
        except ValueError:
            print("Usage : revolution --random <nombre>")
    elif len(sys.argv) > 1 and sys.argv[1] == "--random":
        print("Usage : revolution --random <nombre>")
    elif len(sys.argv) > 2 and sys.argv[1] == "--search":
        rechercher_citations(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == "--search":
        print("Usage : revolution --search <mot>")
    else:
        afficher_citation(sys.argv[1] if len(sys.argv) > 1 else None)