# primitives

A component belongs here only if it appears on **more than one surface**.
Every primitive must:

1. read every colour, size and radius from `../tokens.css` — **zero hex literals**;
2. declare its surface (`paper` / `glass` / `both`) in a comment at the top;
3. add any new contrast pair it relies on to `../check_contrast.py`.

`label.css` and `readout.css` are the reference implementations — the two type
voices, and the two things most likely to drift. Follow their shape.

Still to build: `button` · `card` · `status-badge` · `meter` · `marquee` ·
`screen` · `base`.
