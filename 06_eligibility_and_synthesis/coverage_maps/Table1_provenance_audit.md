# Table 1: bounded provenance audit, 29 September 2026

The CSV retains 29 external comparators and the present-review row. Canonical
BibTeX-key aliases are explicit; no comparator was added or removed. This pass
adds source paths, source hashes and claim-specific locators, while distinguishing
located files from inspected passages. It is not a new independent full-paper
coding of all 29 comparators.

## What was checked

Positive-treatment passages were inspected for all 11 supplementary positioning
comparators named by the selection rule: Campbell, Edwards, Ciulei, Joseph,
Hasan, Nather, Vonnethen, Dekkaki, Gharavi, Diaz and Udugahapattuwa. The checks
also cover selected positive passages in Buser's exotic-signature survey and
Khodaiemehr's broad blockchain survey. For the metadata-only comparator
`coreH2024security`, the available Abstract field was inspected and explicitly
identified as metadata, not a full-text check. The final readiness pass also
located Wicaksana's published survey and inspected the positive passages on
PDF pages 5 and 17. Thus 15 records have inspected
positive-treatment locators; a locator verifies the presence of that treatment,
not every supplied coverage-strength judgment.

Source files and precise extracted-text line ranges are given per coverage
dimension in `table1_coverage_decisions.csv`. Campbell uses a PDF-page/section
locator because the local text extraction contains unusually long lines. Paths
to further existing PDFs are discovery pointers only. Where a source or a
claim-specific passage was not checked, the cell says so rather than asserting
verification. Negative cells were not independently re-audited across complete
papers and are labelled accordingly.

`Assessment_Source_SHA256` hashes `Assessment_Source_Text` when present, otherwise the
located PDF. Text-line numbers refer to the exact hashed text file, not to the
manuscript. The earlier Table1 audit's source version is retained; a final
publication/version reconciliation remains necessary if it differs from the
cited edition. Original status labels such as "Full text audited" describe the
supplied audit, not a newly completed exhaustive audit in this assessment.

## Corrected decisions

Gharavi et al. (`gharavi2024pqiot`) originally had `ZK_Privacy=ScopeLim`.
The paper has a dedicated subsection **E. Privacy vs. Transparency**, with
**2) Zero-knowledge Proofs**, alongside ring and blind signatures. The inspected
text is `681683.txt`, lines 2108-2165, especially lines 2142-2154. It discusses
quantum-resistant ZKPs and concrete blockchain/IoT privacy roles. Under the
manuscript's declared rule (a dedicated section/subsection with substantive
secondary treatment), this warrants **ScopeMod**. The current CSV makes that
correction and preserves **ScopeLim** in `Baseline_ZK_Privacy`. This is a scope
coverage correction, not an assessment of cryptographic correctness or maturity.

Udugahapattuwa et al. (`udugahapattuwa2026quantumresistant`) had
`ZK_Privacy=ScopeAbsent` in the incoming coding. The targeted passage at LF
lines 413–422 of `11434854.txt` discusses quantum exposure of privacy-protocol
assumptions and supports `ScopeLim`. The CSV retains the original value in
`Baseline_ZK_Privacy` and records the correction and locator.

## Source reconciliation on 30 September 2026

The published Wicaksana survey (`coreA2025survey`) was located as
`papers/new/high risk/1-s2.0-S1574013725000280-main.pdf`. Its title, author and
publication identity were checked. PDF page 5, Section 4.1.2 and Table 3,
provides dedicated ZK/privacy coverage. PDF page 17, Section 8.3, discusses
integration into existing protocols, standardization, computational overhead
and throughput. These passages support the existing secondary-treatment
decisions. The CSV now supplies the PDF path, SHA-256 and cell-level locators.
The evidence-continuity absence remains an inherited decision.

## Important limits

- `coreH2024security` remains metadata-only. Its positive treatment is provisional;
  lack of documented ZK/privacy or evidence-continuity treatment in its abstract
  is unknown at full-paper level, not verified absence.
- Wicaksana's source and positive-treatment locators are now reconciled. Its
  negative coverage code was not independently reassessed across the whole paper.
- The source files for newly added comparators may be available without every
  coverage cell having been re-checked. Discovery is not full-text assessment.
- The present-review row is author self-description, not independent assessment.
- No inter-coder agreement, full dual coding or negative-coverage validation is
  inferred from the presence of these locators.
