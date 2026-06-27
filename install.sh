#!/bin/bash
if [ "$(id -u)" -ne 0 ]; then
    echo "Exécute avec sudo !"
    exit 1
fi

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_DIR="/usr/local/share/revolution"
BIN_DIR="/usr/local/bin"

mkdir -p "$INSTALL_DIR" "$BIN_DIR"

# Copie les fichiers (sauf cachés et install.sh/uninstall.sh)
find "$SOURCE_DIR" -maxdepth 1 -type f ! -name "install.sh" ! -name "uninstall.sh" ! -name ".git*" -exec cp {} "$INSTALL_DIR" \;

# Création wrapper
cat > "$BIN_DIR/revolution" << 'EOF'
#!/bin/bash
python3 /usr/local/share/revolution/revolution.py "$@"
EOF

chmod +x "$BIN_DIR/revolution" "$INSTALL_DIR/revolution.py"
echo "Installation terminée ! Teste avec : revolution"
