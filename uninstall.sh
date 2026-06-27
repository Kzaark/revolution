#!/bin/bash

# Vérifie que le script est lancé en root
if [ "$(id -u)" -ne 0 ]; then
    echo "⚠️  Ce script doit être exécuté en tant que root (utilise 'sudo')."
    exit 1
fi

# Chemins (mis à jour pour "revolution")
INSTALL_DIR="/usr/local/share/revolution"
BIN_DIR="/usr/local/bin"

# Supprime le wrapper (pas un lien symbolique, mais un fichier)
rm -f "$BIN_DIR/revolution"

# Supprime le dossier d'installation
rm -rf "$INSTALL_DIR"

# Message de confirmation
echo "✅ Désinstallation terminée."
echo "   La commande 'revolution' a été supprimée."
