# graphr-tokens

The Graphr design system as code. Bob design language **v2.0-C "Cabinet."**

> Cream speaks. Glass reports.

One paper (`#F6F0E1`), one glass (`#0E1A18`). Sentences and serif live on paper;
figures, counts and live states live on glass, inset into it. That single rule
replaces the equal-box stat grid — it is the signature of the system.

## Install

```jsonc
// package.json of the consuming repo
"dependencies": {
  "graphr-tokens": "github:weldebob/graphr-tokens"
}
```

```js
// astro.config / vite / next — import once, globally
import 'graphr-tokens/tokens.css'
```

```js
// tailwind.config.js
module.exports = { presets: [require('graphr-tokens/tailwind-preset')] }
```

## What's here

| File | Job |
|---|---|
| `tokens.css` | every custom property. The source of truth. |
| `tailwind-preset.js` | the same tokens as Tailwind theme keys, by reference |
| `check_contrast.py` | verifies all 20 pairs from the guide's §03 table |
| `check-tokens.sh` | fails if any hex literal appears outside `tokens.css` |
| `primitives/` | components used on more than one surface |
| `CLAUDE.md` | the rules, for agents working in this repo |

## Verify

```bash
python3 check_contrast.py   # PROBLEMS: 0
./check-tokens.sh .         # no stray hex
```

Both run in CI. Neither is optional — the whole value of this package is that a
surface cannot drift without a check going red.

## The palette, in one table

| Token | Hex | Surface | Job |
|---|---|---|---|
| `--cream` | `#F6F0E1` | paper | the ground. everything you read. |
| `--screen` | `#0E1A18` | glass | the ground for every figure |
| `--spruce` | `#3D6B64` | **paper only** | structure, the settled register, the reward |
| `--clay-deep` | `#9A4527` | both | the only accent that **acts** |
| `--clay` | `#BF5B3B` | both | display 24px+, borders, rules. never small light text. |
| `--phosphor` | `#6FE3C0` | **glass only** | live figures |

Spruce and phosphor are the same hue at two depths — one nearly black, one at
full chroma. The screen is the green; the readout is the green lit up. Clay is
the complement that survives on both.

Need an in-between? Derive it in oklch from these. Never invent a hue.

## Vocabulary

The arcade lives in the words and the readouts, never in the drawing.

WAVE · CLEARED · DORMANT · BEST WAVE · EXTRA LIFE · INSERT COIN · CATCH ·
ALL CLEAR

Every borrowed term names a real quantity. If it can't, it doesn't ship.
`BEST WAVE` is your own record — never ranked against other people, ever.

## Moving between guides

v2.0 (two papers, violet) and v2.0-C (one paper, spruce) are structurally
identical. A build on either moves to the other by swapping token values in this
one file. That is deliberate — the choice is not a one-way door.
