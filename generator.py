import os
import sys
import importlib.util

TEMPLATES_DIR = "../DocumentazioneProgetto/docs-template"
MODULES_DIR = "generators"
OUTPUT_DIR = "output"

def get_template(document: str) -> str:
    if not os.path.exists(f"{TEMPLATES_DIR}/{document}.tex"):
        raise FileNotFoundError("Template del documento non trovato")
    with open(file = f"{TEMPLATES_DIR}/{document}.tex", mode = "r", encoding = "utf-8") as td:
        return td.read()

def fill_frontespizio(template_path):
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"File non trovato: {template_path}")
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    print("\n=== Compilazione Frontespizio ===\n")
    
    titolo = input("Titolo documento: ").strip()
    data_doc = input("Data redazione (AAAA-MM-GG): ").strip()
    versione = input("Versione (SemVer X.Y.Z): ").strip()
    descrizione_modifica = input("Descrizione modifica: ").strip()
    redattore = input("Redattore (Cognome Nome): ").strip()

    placeholders = {
        "<<<TITOLO>>>": titolo,
        "<<<DATA>>>": data_doc,
        "<<<DATA_MODIFICA>>>": data_doc,
        "<<<VERSIONE>>>": versione,
        "<<<REDATTORE>>>": redattore,
        "<<<DESC_MODIFICA>>>": descrizione_modifica,
    }

    for key, value in placeholders.items():
        if key not in template:
            print(f"Attenzione: placeholder '{key}' non trovato nel template!")
        template = template.replace(key, value)

    return template

def get_module(module_name):
    spec = importlib.util.spec_from_file_location(module_name, f"{MODULES_DIR}/{module_name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def write_document(content: str, filename: str):
    if not os.path.exists(f"{OUTPUT_DIR}"):
        os.makedirs(OUTPUT_DIR)
    with open(f"{OUTPUT_DIR}/{filename}", "w", encoding="utf-8") as wd:
        wd.write(content)
    print(f"Documento {OUTPUT_DIR}/{filename} generato")

def create_document():
    print("=== Generatore Documenti LaTeX ===\n")
    print("Tipi di documento disponibili:")
    print("  - Verbale Interno\n  - Verbale Esterno")

    doc_name = input("\nIndicare nome con cui salvare il documento: ").strip()
    document_type = input("\nIndicare tipo di Documento (interno | esterno): ").strip()

    if document_type not in ["interno", "esterno"]:
        print("Tipo di documento non supportato.")
        return

    # ---- Caricamento Frontespizio e Template ----
    frontespizio = fill_frontespizio(f"{TEMPLATES_DIR}/frontespizio.tex")
    template = get_template(document_type)
    documento_finale = frontespizio + get_module(document_type).generate(template)

    # ---- Salvataggio ----
    write_document(documento_finale, f"{doc_name}.tex")

def modify_document():
    print("Nota: il documento deve trovarsi nella cartella output/")
    doc_name = input("Indicare nome del documento (senza .tex): ").strip()
    file_path = os.path.join(OUTPUT_DIR, f"{doc_name}.tex")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Il file {doc_name}.tex non è presente in {OUTPUT_DIR}/")

    # --- 1. Leggo il documento ---
    with open(file_path, "r", encoding="utf-8") as f:
        doc = f.read()

    # --- 2. Raccolta della nuova modifica ---
    print("\n--- Nuova modifica da aggiungere ---")
    data_mod = input("Data modifica (AAAA-MM-GG): ").strip()
    versione = input("Versione del documento: ").strip()
    desc_mod = input("Descrizione modifica: ").strip()
    redattore = input("Redattore: ").strip()

    new_row = (
        f"{data_mod} & {versione} & {desc_mod} & "
        f"{redattore} & <<<VERIFICATORE>>> \\\\ \n\\hline\n"
    )

    header_text = (
        "\\textbf{Data Modifica} & \\textbf{Versione} & "
        "\\textbf{Descrizione Modifica} & \\textbf{Redattore} & \\textbf{Verificatore}\\\\"
    )

    header_index = doc.find(header_text)
    if header_index == -1:
        raise ValueError("Header del changelog non trovato nel documento.")

    after_header_hline = doc.find("\\hline", header_index)
    if after_header_hline == -1:
        raise ValueError("Non è stato trovato '\\hline' dopo l'header del changelog.")
    insert_pos = after_header_hline + len("\\hline")

    if doc[insert_pos:insert_pos+2] == "\r\n":
        insert_pos += 2
    elif doc[insert_pos:insert_pos+1] == "\n":
        insert_pos += 1
    doc = doc[:insert_pos] + new_row + doc[insert_pos:]

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(doc)

def verify_document():
    print("Nota: il documento deve trovarsi nella cartella output/")
    doc_path = input("Indicare nome del documento: ").strip()
    if not os.path.exists(f"{OUTPUT_DIR}/{doc_path}.tex"):
        raise FileNotFoundError(f"Il file {doc_path}.tex non è presente in {OUTPUT_DIR}/")
    with open(file = f"{OUTPUT_DIR}/{doc_path}.tex", mode = "r", encoding = "utf-8") as vd:
        doc = vd.read()
    verificatore = input("Verificatore (Cognome Nome): ").strip()
    doc = doc.replace("<<<VERIFICATORE>>>", verificatore)
    with open(file = f"{OUTPUT_DIR}/{doc_path}.tex", mode = "w", encoding = "utf-8") as cd:
        cd.write(doc)

def main():
    request = input("Indicare operazione (creazione | modifica | verifica): ").strip().lower()
    if request == "creazione":
        create_document()
    elif request == "modifica":
        modify_document()
    elif request == "verifica":
        verify_document()
    else:
        print("Modalità non valida")

if __name__ == "__main__":
    main()