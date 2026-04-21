#!/usr/bin/env python3
"""
Thin a reservoir simulation schedule file from monthly/bi-weekly to quarterly timesteps.

Strategy:
  - Structural keywords (WELSPECS, COMPDAT, WELOPEN, WTEST, WRFTPLT, WTRACER, etc.):
    kept at their original relative order, placed before the quarterly DATES.
  - State keywords (WCONHIST, WCONINJE, WCONPROD): only the LAST occurrence per
    quarter is written (reflects end-of-quarter well state).
  - RPTSCHED: kept once per quarter (the last one).
  - RPTRST: kept once per year (the last one in the year).
  - TUNING keyword is inserted at the top to allow large internal timesteps.
"""

import re
import sys
from datetime import date
from collections import defaultdict, OrderedDict

INPUT  = r'C:\gitroot\resinsight\resinsight-tutorials\model-data\norne-atw2013\INCLUDE\BC0407_HIST01122006-complete.SCH'
OUTPUT = r'C:\gitroot\resinsight\resinsight-tutorials\model-data\norne-atw2013\INCLUDE\BC0407_HIST01122006.SCH'

# Fix paths to be relative-friendly
import os
BASE = os.path.dirname(os.path.abspath(__file__))
INPUT  = os.path.join(BASE, 'BC0407_HIST01122006-complete.SCH')
OUTPUT = os.path.join(BASE, 'BC0407_HIST01122006.SCH')

MONTH_MAP = {
    'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
    'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12
}
INV_MONTH = {v: k for k, v in MONTH_MAP.items()}

# Keywords whose last-per-quarter value is kept (state, not structure)
STATE_KW   = {'WCONHIST', 'WCONINJE', 'WCONPROD', 'RPTSCHED'}
# Keywords kept only last per year
ANNUAL_KW  = set()  # RPTRST handled explicitly as BASIC=2 always
# Structural keywords: kept all, in order
STRUCTURAL_KW = {
    'WELSPECS', 'COMPDAT', 'WELOPEN', 'WTEST', 'WRFTPLT', 'WTRACER',
    'GRUPTREE', 'VAPPARS', 'NETBALAN', 'WPAVE', 'GCONINJE', 'WECON',
    'GECON', 'GRUPNET', 'WSEGVALV', 'WELSEGS', 'COMPSEGS',
}


def parse_ecl_date(s):
    m = re.search(r"(\d{1,2})\s+'([A-Z]{3})'\s+(\d{4})", s)
    if m:
        return date(int(m.group(3)), MONTH_MAP[m.group(2)], int(m.group(1)))
    return None


def quarter_start(d):
    qm = ((d.month - 1) // 3) * 3 + 1
    return date(d.year, qm, 1)


def fmt_date_line(d):
    return f" {d.day} '{INV_MONTH[d.month]}' {d.year} /"


# ---------------------------------------------------------------------------
# Parse the file into a header section (before first DATES) and a list of
# (date_obj, keyword_blocks) pairs where keyword_blocks is a list of
# (keyword_name, raw_text) tuples.
# ---------------------------------------------------------------------------

def split_into_steps(raw_text):
    """Return (header_text, steps) where steps = list of (date, blocks_text)."""
    # Split at each DATES keyword start
    chunks = re.split(r'(?=^DATES\b)', raw_text, flags=re.MULTILINE)
    header = chunks[0]
    steps = []
    for chunk in chunks[1:]:
        # Extract the date from the DATES block
        d = None
        for line in chunk.splitlines():
            d = parse_ecl_date(line)
            if d:
                break
        steps.append((d, chunk))
    return header, steps


def extract_keyword_blocks(text):
    """
    Parse text into a list of (keyword, full_block_text).
    Non-keyword lines (comments, blank lines before a keyword) are prepended
    to the following keyword block.
    """
    blocks = []
    lines = text.splitlines(keepends=True)
    i = 0
    pending = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped or stripped.startswith('--'):
            pending.append(line)
            i += 1
            continue

        kw_match = re.match(r'^([A-Z][A-Z0-9_]{2,12})\s*(?:--|$)', stripped)
        if kw_match:
            kw = kw_match.group(1)
            block = list(pending) + [line]
            pending = []
            i += 1
            # Accumulate until a standalone '/' line
            while i < len(lines):
                block.append(lines[i])
                if lines[i].strip() == '/':
                    i += 1
                    break
                i += 1
            blocks.append((kw, ''.join(block)))
        else:
            # Inline keyword with data on same line (rare in schedule files)
            # Treat as opaque comment-like block
            pending.append(line)
            i += 1

    if pending:
        blocks.append(('_TRAILING', ''.join(pending)))

    return blocks


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

with open(INPUT, 'r') as f:
    raw = f.read()

header, steps = split_into_steps(raw)

# Group steps by year
# year_key -> list of (date, blocks)
years = OrderedDict()
for d, chunk in steps:
    if d is None:
        continue
    ykey = d.year
    if ykey not in years:
        years[ykey] = []
    years[ykey].append((d, extract_keyword_blocks(chunk)))

# ---------------------------------------------------------------------------
# Build output
# ---------------------------------------------------------------------------

out_lines = []

# Write header (everything before first DATES, which includes the original
# WELSPECS, COMPDAT, GRUPTREE, WCONHIST, etc. plus the TUNING insertion)
out_lines.append(header.rstrip('\n'))
out_lines.append('')

# Insert TUNING to allow large internal timesteps
out_lines.append('-- Thinned schedule: one timestep per year for faster simulation')
out_lines.append('-- TUNING: allow larger internal Newton timesteps')
out_lines.append('TUNING')
out_lines.append('-- TSINIT  TSMAXZ  TSMINZ  TSMCHP  TSFCNV  TFDIFF  THRUPT  TMAXWC')
out_lines.append('  1.0    100.0    0.1    0.15    0.3    1.25  1*    10.0 /')
out_lines.append('-- TRGTTE  TRGCNV  TRGMBE  TRGLCV  XXXTTE  XXXCNV  XXXMBE  XXXLCV  XXXWFL')
out_lines.append('   0.1    0.001  1.0E-7  0.001    10.0    0.01   1.0E-6   0.01    1.0E-6 /')
out_lines.append('-- NEWTMX  NEWTMN  LITMAX  LITMIN  MXWSIT  MXWPIT  DDPLIM  DDSLIM  TRGDPR')
out_lines.append('   25      1      50      0       8       8      1*       1*     200.0 /')
out_lines.append('')

for q_idx, (ykey, step_list) in enumerate(years.items()):
    # Collect all structural blocks (in order of occurrence across all steps in this quarter)
    structural_blocks = []   # (kw, text) in encounter order
    # State: last seen per keyword
    state_last = {}          # kw -> text
    # Annual: last seen per (kw, year)
    annual_last = {}         # (kw, year) -> text

    # The first actual date in this quarter (used for first quarter to avoid
    # going before the simulation start date)
    first_actual_date = step_list[0][0]
    last_actual_date  = step_list[-1][0]

    for orig_date, blocks in step_list:
        for kw, text in blocks:
            if kw == 'DATES':
                continue
            if kw in STRUCTURAL_KW:
                structural_blocks.append((kw, text))
            elif kw in STATE_KW:
                state_last[kw] = text
            elif kw in ANNUAL_KW:
                annual_last[(kw, orig_date.year)] = text
            elif kw == 'RPTRST':
                pass  # ignored; always write BASIC=2 per year below
            elif kw == '_TRAILING':
                pass  # drop trailing comments between date blocks
            # else: unknown keyword, keep it as structural
            else:
                structural_blocks.append((kw, text))

    # Use the last actual date in this year (keeps original dates, skips intermediates)
    report_date = last_actual_date
    # Write RPTRST BEFORE DATES so it is in effect when this report step runs
    out_lines.append('RPTRST')
    out_lines.append(" 'BASIC=2' /")
    out_lines.append('')
    # Write yearly DATES
    out_lines.append(f'-- Yearly step: {fmt_date_line(report_date)}')
    out_lines.append('DATES')
    out_lines.append(fmt_date_line(report_date))
    out_lines.append('/')
    out_lines.append('')

    # Write structural blocks
    for kw, text in structural_blocks:
        out_lines.append(text.rstrip('\n'))
        out_lines.append('')

    # Write state keywords (last WCONHIST, WCONINJE, RPTSCHED per year)
    for kw in ('WCONHIST', 'WCONINJE', 'WCONPROD', 'RPTSCHED'):
        if kw in state_last:
            out_lines.append(state_last[kw].rstrip('\n'))
            out_lines.append('')

out_lines.append('')

output_text = '\n'.join(out_lines)

with open(OUTPUT, 'w') as f:
    f.write(output_text)

# Summary
with open(OUTPUT) as f:
    out_content = f.readlines()

orig_dates = len([s for s, c in steps if s is not None])
out_dates = sum(1 for line in out_content if re.match(r'^DATES\s*$', line))
print(f"Input:  {len(raw.splitlines())} lines, {orig_dates} timesteps")
print(f"Output: {len(out_content)} lines, {out_dates} timesteps (quarterly)")
print(f"Speedup factor (timestep reduction): {orig_dates / max(out_dates,1):.1f}x")
print(f"Written: {OUTPUT}")
