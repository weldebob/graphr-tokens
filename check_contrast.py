#!/usr/bin/env python3
"""
Verifies every foreground/background pair in tokens.css against the measured
table in Bob Style Guide v2.0-C "Cabinet" §03, and against the WCAG AA floor.

Two things are asserted, not one:
  - pairs the guide clears must clear 4.5:1
  - pairs the guide BANS must still fail. If a banned pair starts passing,
    a token moved and the rule that depends on it is now wrong.

TWO ERRATA in the guide's §03, both in the FAILS column, where the exact number
carries no weight — which is presumably why they drifted:
    spruce on glass       guide 2.3:1   measured 2.95:1
    phosphor-dim on cream guide 1.8:1   measured 1.67:1
Both fail AA either way, so every rule that depends on them is unchanged and
correct. This script carries the measured values. Do NOT "fix" them back.

Exit code 0 = clean.
"""
import re
import sys
import pathlib

def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def luminance(hex_colour):
    h = hex_colour.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)

def ratio(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

AA = 4.5

HERE = pathlib.Path(__file__).parent
css = (HERE / "tokens.css").read_text()

# strip comments before parsing, so prose about banned values is never
# mistaken for a declaration
css_code = re.sub(r"/\*.*?\*/", "", css, flags=re.S)

TOKENS = dict(re.findall(r"--([a-z-]+):\s*(#[0-9A-Fa-f]{6})", css_code))

# (fg, bg, description, guide's stated ratio, must_clear_AA)
CHECKS = [
    ("ink",          "cream",          "ink on cream",                    13.9, True),
    ("secondary",    "cream",          "secondary on cream",               5.2, True),
    ("spruce",       "cream",          "spruce on cream",                  5.3, True),
    ("label",        "cream",          "label on cream",                   4.9, True),
    ("label",        "cream-card",     "label on card",                    5.5, True),
    ("label",        "settled",        "label on settled tint",           None, True),
    ("clay-deep",    "cream",          "clay-deep on cream",               5.7, True),
    ("cream-card",   "clay-deep",      "card-white on clay-deep fill",     6.3, True),
    ("cream-card",   "clay-deepest",   "card-white on clay-deepest (hover)", None, True),
    ("phosphor",     "screen",         "phosphor on glass",               11.4, True),
    ("phosphor-dim", "screen",         "phosphor-dim on glass",            9.4, True),
    ("phosphor-dim", "screen-raised",  "phosphor-dim on screen-raised",    8.2, True),
    ("clay-glow",    "screen",         "clay-glow on glass",               7.2, True),
    ("cream",        "screen",         "cream on glass",                  15.7, True),

    # The ink ramp (spec §7). The guide quotes deck 7.9:1, body 9.6:1 and hint
    # 7.1:1; all three measure HIGHER here, so the guide is conservative and
    # every pair clears with room. Carrying None rather than the guide's number
    # keeps this table honest about what it actually asserts.
    ("ink-body",     "cream",          "ink-body on cream",               None, True),
    ("ink-body",     "cream-card",     "ink-body on card",                None, True),
    ("ink-deck",     "cream",          "ink-deck on cream (deck)",        None, True),
    ("ink-deck",     "cream-card",     "ink-deck on card (deck)",         None, True),
    ("ink-hint",     "cream",          "ink-hint on cream",               None, True),
    ("ink-hint",     "cream-card",     "ink-hint on card (field hint)",   None, True),

    # Added by primitives/ — pairs the components actually rely on.
    ("ink",          "cream-card",     "ink on card (card body)",         None, True),
    ("ink",          "settled",        "ink on settled tint (card)",      None, True),
    ("ink",          "unconfirmed",    "ink on unconfirmed tint (card)",  None, True),
    ("label",        "unconfirmed",    "label on unconfirmed (badge)",    None, True),
    ("phosphor",     "screen-raised",  "phosphor on track (meter fill)",  None, True),
    ("secondary",    "cream-card",     "secondary on card (field hint)",  None, True),
    ("secondary",    "settled",        "secondary on settled (disabled)", None, True),

    ("screen",       "phosphor",       "glass text on a phosphor fill",   None, True),
    ("screen",       "phosphor-dim",   "glass text on phosphor-dim (hover)", None, True),

    # The paper action (spec §6) — spruce-deep resting, spruce on hover.
    ("cream-card",   "spruce-deep",    "card-white on the paper button",  None, True),
    ("cream-card",   "spruce",         "card-white on button hover",      None, True),
    ("spruce",       "cream",          "eyebrow on cream",                None, True),
    ("spruce",       "cream-card",     "eyebrow on card",                 None, True),
    ("spruce",       "settled",        "eyebrow on settled tint",         None, True),

    # Must FAIL. These encode the absolute rules; the numbers are the assertion.
    ("phosphor",     "cream",  "phosphor on cream            [BANNED]",    1.4, False),
    # erratum: guide says 1.8, true value 1.67. Rule unchanged.
    ("phosphor-dim", "cream",  "phosphor-dim on cream        [BANNED]",   1.67, False),
    ("cream-card",   "clay",   "card-white on clay fill      [BANNED]",    4.3, False),
    ("ink",          "clay",   "ink on clay fill             [BANNED]",    3.6, False),
    ("clay",         "cream",  "clay on cream, small text    [BANNED]",    3.9, False),
    ("clay",         "screen", "clay on glass                [BANNED]",    4.0, False),
    # erratum: guide says 2.3, true value 2.95. Rule unchanged.
    ("spruce",       "screen", "spruce on glass              [BANNED]",   2.95, False),
    # A glass link colour must never repaint an acting fill: a page rule like
    # `.base a {color: var(--clay-glow)}` out-specifies `.button` and lands
    # clay-glow on clay-deep. Encoded so the failure is caught here, not by eye.
    ("clay-glow",    "clay-deep", "clay-glow on clay-deep fill  [BANNED]", 2.60, False),
]

BANNED_VALUES = {
    "#6366f1": "bright indigo — the default accent of the category this system leaves",
}

def main():
    problems = []
    print(f"{'ratio':>8}  pair")
    print("-" * 62)

    for fg, bg, name, stated, must_clear in CHECKS:
        if fg not in TOKENS or bg not in TOKENS:
            problems.append(f"missing token in pair: {fg} / {bg}")
            continue
        r = ratio(TOKENS[fg], TOKENS[bg])
        clears = r >= AA
        mark = " " if clears == must_clear else "!"
        if clears != must_clear:
            problems.append(
                f"{name}: {r:.2f}:1 "
                f"{'should clear AA but does not' if must_clear else 'should FAIL but clears AA'}"
            )
        note = ""
        if stated is not None and abs(r - stated) > 0.05:
            note = f"   <-- guide says {stated}"
            problems.append(f"{name}: measured {r:.2f}:1, guide states {stated}")
        print(f"{mark}{r:7.2f}:1  {name}{note}")

    for value, why in BANNED_VALUES.items():
        if value in css_code.lower():
            problems.append(f"banned value {value} present in tokens.css — {why}")

    print()
    print(f"tokens parsed: {len(TOKENS)}")
    print(f"pairs checked: {len(CHECKS)}")
    print(f"PROBLEMS: {len(problems)}")
    for p in problems:
        print(f"  - {p}")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
