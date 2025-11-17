// Template Diario di Bordo SWE - Skarab (Parametrico)

// Colori personalizzati
#let secondary = rgb(128, 24, 40)     // Bordeaux puro 
#let darkbg = rgb(28, 28, 30)        // Grigio scuro
#let lightbg = rgb(242, 242, 247)    // Grigio chiaro

#set page(
  paper: "presentation-16-9",
  margin: (x: 2.5em, y: 3em),
  header: context {
    if counter(page).get().first() > 1 [
      #set text(size: 10pt, fill: black)
      #grid(
        columns: (1fr, auto),
        align: (left, right),
        [Skarab Group],
        [#counter(page).display("1/1", both: true)]
      )
      #line(length: 100%, stroke: 0.5pt + black)
    ]
  },
  footer: context {
    if counter(page).get().first() > 1 [
      #line(length: 100%, stroke: 0.5pt + black)
      #set text(size: 9pt, fill: black)
      #grid(
        columns: (1fr, 1fr, 1fr),
        align: (left, center, right),
        [Diario di Bordo <<<NUMERO_DIARIO>>>],
        [<<<DATA_PRESENTAZIONE>>>],
        []
      )
    ]
  }
)

#set text(size: 20pt, font: "New Computer Modern Sans", lang: "it")
#set par(justify: true)
#set heading(numbering: none)

// Stile per i titoli
#show heading.where(level: 1): it => {
  pagebreak(weak: true)
  v(2em)
  block(
    width: 100%,
    fill: secondary,
    inset: 1em,
    radius: 8pt,
  )[ #text(fill: white, size: 32pt, weight: "bold")[#it.body] ]
  v(1em)
}

#show heading.where(level: 2): it => {
  v(1em)
  text(fill: secondary, size: 24pt, weight: "bold")[#it.body]
  v(0.5em)
  line(length: 100%, stroke: 1pt + secondary)
  v(0.5em)
}

// SLIDE TITOLO
#page[
  #set align(center + horizon)
  #rect(width: 87%, fill: secondary, radius: 12pt, inset: 1.3em)[
    #text(fill: white, size: 30pt, weight: "bold")[
      Diario di Bordo <<<NUMERO_DIARIO>>> - Skarab Group
    ]
  ]
  #v(0em)
  #text(size: 19pt, fill: secondary)[
    Ingegneria del Software - A.A. 2025/2026
  ]
  #v(0em)
  #line(length: 60%, stroke: 2pt + secondary)
  #v(0em)
  // Layout a due colonne
  #grid(
    columns: (30%, 40%),
    column-gutter: 2em,
    align(center)[
      #text(size: 18pt, weight: "bold")[Componenti del Team:]
      #v(0em)
      #text(size: 14pt)[
        Alberto Suar\
        Kevin Basso\
        Riccardo Martinello\
        Alice Zago\
        Andrea Sgreva\
        Antonio Sandu\
        Riccardo Berengan
      ]
      #v(0.1em)
      #text(size: 13pt)[
        Contatto: *#link("mailto:skarabswegroup@gmail.com")*
      ]
    ],
    align(center + horizon)[
      #image("skarablogo_.jpg", width: 50%)
    ]
  )
]

// SLIDE Difficoltà incontrate
#grid(
  columns: (1fr, auto),
  align: (left + horizon, right + horizon),
  column-gutter: 1em,
  text(fill: secondary, size: 24pt, weight: "bold")[Difficoltà Incontrate],
  image("skarablogo_.jpg", width: 1.5cm)
)
#v(0em)
#line(length: 100%, stroke: 1pt + secondary)
#v(0.1em)

// Contenuto Difficoltà incontrate (placeholder)
- #text(fill: secondary)[<<<DIFFICOLTA_INCONTRATE>>>]