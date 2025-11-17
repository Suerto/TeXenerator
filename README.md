# TeXenerator - Generatore documentazione del team SkarabGroup
---
## Descrizione ed utilizzo
TeXenerator è un generatore semi-automatico di documenti in LaTeX il quale, dato in input
un template di un documento, richiede una serie di informazioni al fine di costruire il 
documento finale. 

Per avviare l'esecuzione da Windows:
```bash
python generator.py
```

Oppure da Ubuntu/Debian:
```bash
python3 generator.py
```

Successivamente seguire le procedure indicate dal terminale durante l'esecuzione.
---
## Prerequisiti per la creazione del PDF del documento
### Windows
Necessario avere installato **MiKTeX**: https://miktex.org/download

Durante l’installazione **attiva l’opzione**:
   - *"Install missing packages on-the-fly"* (Installa automaticamente pacchetti mancanti)
In alternativa, eseguire in **Administrator Mode** MikTeX console e alla sezione **Settings** modificare l'omonima voce

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install texlive-full
```

In entrambi casi, verificare poi se è tutto installato correttamente:
```bash
pdflatex --version
```
---

## Creazione del PDF
### Ubuntu/Debian
Dalla cartella `output/` inserire il seguente comando 
```bash
./getPDF.sh
```
### Windows
Dalla cartella `output/` inserire il seguente comando 
```powershell
.\getPDF.bat nome_documento
```

## Work In Progress
Template del Diario di Bordo
Template del Verbale Esterno