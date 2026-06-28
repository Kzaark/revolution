#!/bin/bash

if [ "$(id -u)" -ne 0 ]; then
    echo "Exécute avec sudo !"
    exit 1
fi

if ! command -v python3 &>/dev/null; then
    echo "Erreur : python3 est requis mais introuvable."
    exit 1
fi

if ! command -v git &>/dev/null; then
    echo "Erreur : git est requis mais introuvable."
    exit 1
fi

INSTALL_DIR="/usr/local/share/revolution"
BIN_DIR="/usr/local/bin"

mkdir -p "$BIN_DIR"

if [ -d "$INSTALL_DIR/.git" ]; then
    echo "Mise à jour du dépôt existant..."
    git -C "$INSTALL_DIR" pull
else
    echo "Clonage du dépôt..."
    git clone https://github.com/Kzaark/revolution.git "$INSTALL_DIR"
fi

cat > "$BIN_DIR/revolution" << 'EOF'
#!/bin/bash
python3 /usr/local/share/revolution/revolution.py "$@"
EOF

chmod +x "$BIN_DIR/revolution" "$INSTALL_DIR/revolution.py"

echo "Installation terminée ! Teste avec : revolution"