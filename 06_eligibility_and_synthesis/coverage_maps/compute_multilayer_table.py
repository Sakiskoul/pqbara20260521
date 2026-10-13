"""Reproduce documented-positive coverage and full-text-subset sensitivity.

Single-coder evidence map; no inter-coder agreement is estimated.
Codes: 2 substantive; 1 secondary; 0 assessed absent/passing; U not assessed.
Coding_Basis is retained from the baseline coding. The full-text subset is a
sensitivity analysis of that coding, not a new full review of every source.
"""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHEET = HERE / 'multilayer_coverage_coding.csv'
DOMAINS = [
    ('D1_TX', 'Transaction', 'Transaction / wallet / account'),
    ('D2_VAL', 'Validator', 'Validator / consensus / governance'),
    ('D3_NODE', 'Node', 'Node trust / PKI / channels'),
    ('D4_SC', 'Smart', 'Smart contracts / DeFi / bridges'),
    ('D5_ZK', 'ZK', 'ZK / privacy / verifiable computation'),
    ('D6_EVID', 'Evidence', 'Evidence / audit / archival'),
]

def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        required = {'BibTeX_Key', 'Primary_Domain', 'Coding_Basis', *(x[0] for x in DOMAINS)}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f'Missing columns: {sorted(missing)}')
        rows = list(reader)
    keys = [row['BibTeX_Key'] for row in rows]
    if len(rows) != 69 or len(set(keys)) != 69:
        raise ValueError('The unchanged core must contain exactly 69 unique records.')
    for row in rows:
        for code, prefix, _ in DOMAINS:
            value = row[code].strip()
            if value not in {'0', '1', '2', 'U'}:
                raise ValueError(f"Invalid {code}={value!r} in {row['BibTeX_Key']}")
            if row['Coding_Basis'] != 'Full text' and value == '0':
                raise ValueError(f"Metadata-only zero must be U: {row['BibTeX_Key']} {code}")
            if row['Primary_Domain'].startswith(prefix) and value != '2':
                raise ValueError(f"Primary-layer code must remain 2: {row['BibTeX_Key']} {code}")
    return rows

def summarize(rows: list[dict[str, str]]) -> dict:
    full = [row for row in rows if row['Coding_Basis'] == 'Full text']
    limited = [row for row in rows if row['Coding_Basis'] != 'Full text']
    summary = {'core_records': len(rows), 'full_text_coding_records': len(full),
               'limited_text_coding_records': len(limited), 'intercoder_agreement': None,
               'agreement_note': 'Not estimated: no independent coder-pair data are supplied.',
               'layers': []}
    for code, prefix, label in DOMAINS:
        values = [row[code] for row in rows]
        ftvalues = [row[code] for row in full]
        unknown = values.count('U')
        row = {'Domain': code, 'Label': label,
               'Primary_n_of_69': sum(r['Primary_Domain'].startswith(prefix) for r in rows),
               'Substantive_documented_n_of_69': values.count('2'),
               'Any_documented_n_of_69': sum(v in {'1', '2'} for v in values),
               'Unknown_n_of_69': unknown,
               'Full_text_denominator': len(full),
               'Full_text_substantive_n': ftvalues.count('2'),
               'Full_text_any_n': sum(v in {'1', '2'} for v in ftvalues),
               'Limited_text_substantive_n': sum(r[code] == '2' for r in limited),
               'Limited_text_any_n': sum(r[code] in {'1', '2'} for r in limited)}
        row['Missingness_only_max_any_n'] = row['Any_documented_n_of_69'] + unknown
        row['Missingness_only_max_substantive_n'] = row['Substantive_documented_n_of_69'] + unknown
        summary['layers'].append(row)
    summary['cross_layer_primary_n'] = sum(r['Primary_Domain'].startswith('Cross') for r in rows)
    summary['records_with_at_least_two_documented_layers'] = sum(
        sum(r[c] in {'1', '2'} for c, _, _ in DOMAINS) >= 2 for r in rows)
    summary['records_with_at_least_two_substantive_layers'] = sum(
        sum(r[c] == '2' for c, _, _ in DOMAINS) >= 2 for r in rows)
    summary['unknown_cells'] = sum(r[c] == 'U' for r in rows for c, _, _ in DOMAINS)
    summary['interpretation'] = ('Counts retain documented positive codes. U is not absence. '
        'Missingness-only maxima are descriptive bounds holding existing codes fixed, not '
        'confidence intervals; coding errors and unreviewed full-text negatives are not quantified. '
        'The full-text subset is availability-selected and is not representative by design.')
    return summary

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Save CSV and JSON summaries beside this script.')
    args = parser.parse_args()
    summary = summarize(read_rows(SHEET))
    print(f"Core: {summary['core_records']}; full-text-coded: {summary['full_text_coding_records']}; limited-text-coded: {summary['limited_text_coding_records']}")
    print('Domain      Primary  Substantive  Any  Unknown  FT substantive/46  FT any/46')
    for row in summary['layers']:
        print(f"{row['Domain']:10s} {row['Primary_n_of_69']:7d} {row['Substantive_documented_n_of_69']:12d} {row['Any_documented_n_of_69']:4d} {row['Unknown_n_of_69']:8d} {row['Full_text_substantive_n']:18d} {row['Full_text_any_n']:10d}")
    print(f"Unknown cells: {summary['unknown_cells']}; multi-layer positives: {summary['records_with_at_least_two_documented_layers']}; multi-layer substantive: {summary['records_with_at_least_two_substantive_layers']}")
    print(summary['agreement_note'])
    if args.write:
        with (HERE / 'multilayer_coverage_summary.csv').open('w', encoding='utf-8-sig', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(summary['layers'][0]))
            writer.writeheader()
            writer.writerows(summary['layers'])
        (HERE / 'multilayer_coverage_summary.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

if __name__ == '__main__':
    main()
