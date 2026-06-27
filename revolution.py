#!/usr/bin/env python3
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

def lister_auteurs():
    for cle, valeur in AUTEURS_CONFIG.items():
        print(f"  {cle:<15} → {valeur['nom']}")

def afficher_toutes_citations(auteur):
    auteur = AUTEURS_ALIASES.get(auteur, auteur)

    if auteur not in AUTEURS_CONFIG:
        print(f"Auteur '{auteur}' introuvable.")
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

def afficher_citation(auteur=None):
    if auteur:
        auteur = AUTEURS_ALIASES.get(auteur, auteur)

    fichiers = [f for f in os.listdir(FORTUNES_DIR) if f in AUTEURS_CONFIG]

    if not fichiers:
        print(f"Aucun fichier trouvé dans {FORTUNES_DIR}")
        return

    fichier = random.choice(fichiers) if not auteur else next((f for f in fichiers if f == auteur), None)
    if not fichier:
        print(f"Auteur '{auteur}' introuvable.")
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
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        lister_auteurs()
    elif len(sys.argv) > 2 and sys.argv[1] == "--all":
        afficher_toutes_citations(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == "--all":
        print("Usage : revolution --all <auteur>")
    else:
        afficher_citation(sys.argv[1] if len(sys.argv) > 1 else None)