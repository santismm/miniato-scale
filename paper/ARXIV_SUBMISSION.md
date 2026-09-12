# arXiv submission — The Miniato Scale, version 1.0

Submission draft already created on arXiv: **8070629** (resume from https://arxiv.org/user). Steps already saved in that draft: contact certified, Submittal Agreement accepted, submitting as author, licence CC BY 4.0, primary category cs.AI. Blocked at "You are not endorsed for this archive" until a cs.AI endorser accepts.

## 1. Endorsement (blocking)

1. Log in and open: https://arxiv.org/auth/need-endorsement.php?category_id=cs.AI
2. arXiv shows a six-character **endorsement code** and the endorser's instructions. Send the message below to one endorser. Candidates from your LinkedIn network, checked on arXiv's own "show endorsers" pages on 12 Sept 2026:

| Candidate | arXiv says | Use |
|---|---|---|
| **Edoardo Cetin** (Sakana AI) | **"Can endorse for cs.AI, cs.LG, cs.CV, cs.CL"** (paper 2512.12167) | **First choice: verified.** |
| Fernando Castañeda García-Rozas (Nvidia) | Registered author, "Not currently an endorser" (paper 2301.12012) | Cannot endorse. |
| Jonas Adler (DeepMind) | Not registered as owner of the paper checked (2007.14745) | Unknown; would need his own arXiv account linked to 3+ cs papers. |
| Nayat Sanchez-Pi (Inria Chile) | Not registered as owner of the papers checked | Unknown; same caveat. Thematically closest, but unverified. | arXiv's rule for cs.AI (checked 12 Sept 2026): the endorser must have submitted 3 papers to any cs.* subject class between three months and five years ago. Any of the candidates above with recent cs.LG/cs.AI/cs.RO papers should qualify; arXiv confirms it on the endorsement page. The code was also e-mailed to santismm@gmail.com; forwarding that e-mail is enough.

### Message to the endorser (English)

Subject: arXiv endorsement request, cs.AI

Dear [Name],

I am about to submit my first arXiv preprint and need an endorsement for cs.AI. The paper proposes the Miniato Scale, an eleven-level ordinal severity scale for AI incidents, with a public card, a bulletin for trends, a reference implementation and a validation programme. It is a methodological proposal, not a validated standard, and it says so.

arXiv's endorsement code is: GQXIPU
Endorsement page: https://arxiv.org/auth/endorse?x=GQXIPU
Preprint PDF and code: https://github.com/santismm/miniato-scale (paper/main.pdf)

Endorsing only confirms that the work is appropriate for arXiv; it is not a review and does not imply agreement. If you would rather not, no problem at all.

Thank you,
Santiago Miniato Santa María Morales
santismm@gmail.com

### Mensaje al avalador (español)

Asunto: Solicitud de aval en arXiv, cs.AI

Hola [Nombre],

Voy a enviar mi primer preprint a arXiv y necesito un aval (endorsement) para cs.AI. El artículo propone la escala Miniato, una escala ordinal de once niveles para la gravedad de incidentes de IA, con una tarjeta pública, un boletín para tendencias, una implementación de referencia y un programa de validación. Es una propuesta metodológica, no un estándar validado, y así lo dice.

Código de aval de arXiv: GQXIPU
Página de aval: https://arxiv.org/auth/endorse?x=GQXIPU
PDF y código: https://github.com/santismm/miniato-scale (paper/main.pdf)

El aval solo confirma que el trabajo encaja en arXiv; no es una revisión ni implica acuerdo. Si prefieres no hacerlo, ningún problema.

Gracias,
Santiago Miniato Santa María Morales
santismm@gmail.com

## 2. Files (step "Add Files")

Upload `miniato-scale-arxiv-v1.0.tar.gz` (contains main.tex, references.bib, main.bbl). arXiv will run pdflatex; the bbl is included so BibTeX is not needed. Expected: 20 pages, 1 figure (TikZ), 6 tables.

## 3. Metadata (step "Metadata"), ready to paste

**Title**
The Miniato Scale: Communicating the Severity of Artificial Intelligence Incidents and Tracking Their Evolution

**Authors**
Santiago Miniato Santa María Morales

**Abstract** (plain text; arXiv does not render LaTeX macros here)
How bad was that AI incident? Today there is no shared answer. Incident databases rate harm within categories, but no widely adopted public level exists that spans domains, carries its own uncertainty, keeps what happened apart from what nearly happened, and can be counted year after year. This paper proposes one: the Miniato Scale, eleven ordinal levels from 0 to 10, with a bulletin format for trends. The level classifies realised consequences in six domains (human health, rights, economic assets, operations, biosphere, societal systems) and takes the maximum: an unaffected domain never dilutes a serious harm in another. Loss of control, autonomy and evidential confidence are shown next to the number and never added into it. Mortality and economic loss share one anchor, theta = 10^7 euros per statistical death, so the two routes sit on one ladder by a stated convention rather than by accident; from level 4 upward, someone has died or harm the calibration places alongside a death has occurred. Levels 9 and 10 are reserved for extinction-class outcomes. Where evidence runs out the result is a set of admissible levels, not a guess. The number is never published alone: a card pairs it with a label, a loss-of-control flag and an evidence status. The bulletin reports exceedance counts per period, the maximum level reached and a ledger in native units, the counting practice of seismic catalogues. Applied retrospectively, five documented cases receive 1, 3, 4, >=5 and >=2, a synthetic hazard receives 0, and loss of control is marked by the flag rather than by the level. A reference implementation and a validation programme accompany the proposal, which is presented as a method to be tested, not as a validated standard.

**Comments**
20 pages, 1 figure, 6 tables. Reference implementation, tests and case records: https://github.com/santismm/miniato-scale

**Primary category**: cs.AI (Artificial Intelligence)
**Cross-list**: cs.CY (Computers and Society)
**License**: CC BY 4.0
**ACM class** (optional): K.4.1; I.2.0
**Report number / Journal ref / DOI**: leave empty

## 4. Preview and submit

Check the PDF that arXiv builds, then press Submit. Announcement happens on the next weekday cycle; arXiv emails the identifier. After announcement, add the arXiv id and DOI to CITATION.cff and README.
