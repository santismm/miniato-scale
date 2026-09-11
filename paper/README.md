# Paper — The Miniato Scale v2.1 (rules `pilot-0.2`)

**The Miniato Scale: Communicating the Severity of Artificial Intelligence Incidents and Tracking Their Evolution**
Santiago Miniato Santa María Morales · September 2026 · preprint, not peer-reviewed.

| File | Content |
|---|---|
| `main.tex` | LaTeX source (article class, natbib, TikZ figure). |
| `references.bib` | 28 references. |
| `main.pdf` | Compiled preprint, 16 pages. |

## Compile

```sh
tectonic main.tex
```

or `pdflatex main && bibtex main && pdflatex main && pdflatex main`.

## Before arXiv submission (author decisions)

1. Verify that the three 2026 incident reports cited in Section 10 (OpenAI, Hugging Face, METR) resolve and support what Table 5 attributes to them. The author has not verified them independently and the paper says so.
2. Choose a licence for the preprint. arXiv requires one; CC BY 4.0 is usual for a proposal meant to be adopted.
3. Category: cs.CY (Computers and Society), cross-list cs.AI.
4. Upload `main.tex`, `references.bib` and the generated `main.bbl` (`tectonic --keep-intermediates main.tex`).
