# Paper — The Miniato Scale v2.4 (rules `pilot-0.3`)

**The Miniato Scale: Communicating the Severity of Artificial Intelligence Incidents and Tracking Their Evolution**
Santiago Miniato Santa María Morales · September 2026 · preprint, not peer-reviewed.

| File | Content |
|---|---|
| `main.tex` | LaTeX source (article class, natbib, TikZ figure). |
| `references.bib` | 34 references. |
| `main.pdf` | Compiled preprint, 20 pages. |

## Compile

```sh
tectonic main.tex
```

or `pdflatex main && bibtex main && pdflatex main && pdflatex main`.

## Before arXiv submission (author decisions)

1. Licence: CC BY 4.0 (decided 12 September 2026); select it in the arXiv submission form.
2. Category: cs.CY (Computers and Society), cross-list cs.AI.
3. Upload `main.tex`, `references.bib` and the generated `main.bbl` (`tectonic --keep-intermediates main.tex`).
