#!/bin/bash

# Vérification du que le script en root
if [ "$(id -u)" -ne 0 ]; then
    echo "Ce script doit être exécuté en tant que root (utilise 'sudo')."
    exit 1
fi

# Chemins
INSTALL_DIR="/usr/local/share/revolution"
BIN_DIR="/usr/local/bin"

# Suppression wrapper
rm -f "$BIN_DIR/revolution"

# Suppression dossier d'installation
rm -rf "$INSTALL_DIR"

# Message de confirmation
echo "Désinstallation terminée."
echo "La commande 'revolution' a été supprimée."
