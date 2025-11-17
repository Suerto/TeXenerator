# TeXenerator - Generatore documentazione del team SkarabGroup

---
## Prerequisiti


## Descrizione ed utilizzo
TeXenerator è un generatore semi-automatico di documenti in LaTeX il quale, dato in input
un template di un documento, richiede una serie di informazioni al fine di costruire il 
documento finale. 

## Per la creazione del PDF
Dalla cartella `output/` inserire il seguente comando 
```bash
pdflatex -interaction=nonstopmode -halt-on-error documento.tex && rm *.out *.toc *.aux *log
```