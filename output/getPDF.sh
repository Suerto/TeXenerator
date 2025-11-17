#!/bin/bash
# Script per compilare un documento LaTeX in PDF su Linux/macOS

# Controlla se è passato un argomento, altrimenti chiedi
if [ -z "$1" ]; then
    read -p "Inserisci il nome del documento .tex (senza estensione): " FILENAME
else
    FILENAME="$1"
fi

# Compila il documento due volte
pdflatex -interaction=nonstopmode -halt-on-error "${FILENAME}.tex"
pdflatex -interaction=nonstopmode -halt-on-error "${FILENAME}.tex"

# Rimuove i file temporanei
rm -f "${FILENAME}.aux" "${FILENAME}.log" "${FILENAME}.out" "${FILENAME}.toc"

echo
echo "PDF generato correttamente: ${FILENAME}.pdf"