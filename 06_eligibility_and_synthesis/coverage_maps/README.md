# Domain coverage and comparator assessments

`multilayer_coverage_coding.csv` records non-exclusive coverage of six migration
domains in the 69 core studies. `table1_coverage_decisions.csv` records the
29 external comparators and the present-review row used in Table 1.

## Domain identifiers

| Code | Operational migration domain |
|---|---|
| D1_TX | Transaction, wallet and account authorization |
| D2_VAL | Validator, consensus and governance |
| D3_NODE | Node trust, PKI and secure communication |
| D4_SC | Smart contracts, DeFi and bridges |
| D5_ZK | Privacy, zero-knowledge and verifiable computation |
| D6_EVID | Evidence, audit and archival verification |

The 18 cross-layer primary records remain in the 69-record denominator. They do
not form a seventh non-exclusive domain. D6 includes storage, authentication,
access control and redaction alongside archival verification. Its count does
not establish evaluation of long-term signature or timestamp renewal.

## Coverage codes and assessment basis

| Code | Meaning |
|---|---|
| 2 | Documented substantive treatment of a mechanism in the domain |
| 1 | Specific secondary treatment |
| 0 | Absence or an incidental mention in the assessed material |
| U | Coverage unassessed from the available titles, abstracts and metadata |

`Coding_Basis` identifies 46 full-text assessments and 23 assessments based on
titles, abstracts and metadata. Metadata-based positive codes describe only
documented coverage. A lack of documented coverage in those records is U.
The `Baseline_D*` columns preserve the numeric assessment before metadata-only
zeros were designated unassessed. `Change_Note` and `Review_Status` record the
corresponding changes and the scope of subsequent checks.

The non-exclusive map has no independent second-coder reliability estimate.
It is separate from the reported screening audit and the exclusive primary
classifications. Generative-AI assistance in preparing the coverage and
comparator assessments is disclosed in the manuscript's methodology and
generative-AI declaration.

## Reproduction

Run from this directory with Python 3.10 or later, using the standard library:

```text
python compute_multilayer_table.py
python compute_multilayer_table.py --write
```

The first command is read-only. `--write` regenerates the summary CSV and JSON.
The script checks 69 unique identifiers, code ranges, assessment-basis rules
and consistency with primary-domain assignments. It reports primary counts,
substantive coverage, any documented coverage, unknowns and the full-text subset.
The full-text denominator is 46. Missingness-only maxima are descriptive bounds
that hold the existing codes fixed and allow U values to be positive.

## Comparator decisions and provenance

Table 1 has 28 external comparators assessed from full text and one,
`coreH2024security`, assessed from its abstract and indexed metadata. Its NA
codes indicate unassessed coverage. Coverage levels describe scope rather than
quality or demonstrated effectiveness.

`targeted_layer_provenance.csv` and the comparator CSV retain supporting
locators, source hashes and assessment notes. Their notes distinguish inspected
passages from decisions carried forward without an independent full-paper
check. A passage locator verifies that passage's content. It does not certify
every coverage judgment for the paper. Baseline comparator codes retain the
earlier assessments where a documented correction was made.

`references.bib`, when distributed with this directory, provides publication
identifiers and links for the cited sources. Source filenames and hashes are
provenance identifiers. Full-text articles are not redistributed in this data
package and remain subject to the publishers' access and reuse terms.
