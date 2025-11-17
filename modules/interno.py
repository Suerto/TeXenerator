# Generatore del documento Verbale Interno
def generate(template):
    print("\n=== Verbale Interno ===\n")

    date = input("Data (AAAA-MM-GG): ").strip()
    start_time = input("Orario Inizio (HH:MM): ").strip()
    end_time = input("Orario Fine (HH:MM): ").strip()
    location = input("Luogo della riunione: ").strip()
    chair = input("Coordinatore: ").strip()

    print("\nInserisci i presenti (separati da virgola):")
    attendees = input("> ").strip()

    print("\nInserisci gli assenti (separati da virgola):")
    absents = input("> ").strip()

    # ---- AGENDA ----
    print("\n--- Definizione dell'Ordine del Giorno ---")
    agenda_items = []
    while True:
        p = input("Aggiungi un punto (Premere Invio per terminare): ").strip()
        if not p:
            break
        agenda_items.append(p)

    # Costruzione LaTeX dell'agenda
    latex_agenda = "\n".join([f"    \\item {p}" for p in agenda_items])

    # ---- SEZIONI ----
    sections = []
    for i, title in enumerate(agenda_items, start=1):
        print(f"\n--- Punto '{title}' ---")
        desc = input("Sintesi del punto: ").strip()
        decision = input("Decisione presa: ").strip()


        section = f"""
                    \\subsection{{Punto {i} — {title}}}
                    \\subsubsection*{{Sintesi}}
                    {desc}

                    \\subsubsection*{{Decisione}}
                    {decision}
                   """
        sections.append(section)
    actions = []
    print("\n--- Azioni e responsabilità ---")
    while True:
        print("\nNuova azione (premi Invio sulla descrizione per terminare)")
        action = input("Azione: ").strip()
        if not action:
            break
        owner = input("Responsabile: ").strip()
        deadline = input("Scadenza: ").strip()
        status = input("Stato (es. Da fare / In corso / Completata): ").strip()

        actions.append((action, owner, deadline, status))

    # Costruzione LaTeX delle righe della tabella
    latex_actions = "\n".join([
        f"{a} & {o} & {d} & {s} \\\\ \\midrule"
        for (a, o, d, s) in actions
    ])

    placeholders = {
        "<<<DATA_MEETING>>>": date,
        "<<<ORA_INIZIO_MEETING>>>": start_time,
        "<<<ORA_FINE_MEETING>>>": end_time,
        "<<<LUOGO_MEETING>>>": location,
        "<<<RESPONSABILE>>>": chair,
        "<<<PRESENTI>>>": attendees,
        "<<<ASSENTI>>>": absents,
    }

    for key, value in placeholders.items():
        if key not in template:
            print(f"Attenzione: placeholder '{key}' non trovato nel template!")
        template = template.replace(key, value)

    template = template.replace("\\AgendaItems", latex_agenda)
    template = template.replace("\\SectionsVerbale", "\n".join(sections))
    template = template.replace("\\ActionsAndResponsibilities", latex_actions)

    return template