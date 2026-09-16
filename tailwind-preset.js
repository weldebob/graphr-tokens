/* graphr-tokens — Tailwind preset for Bob design language v2.0-C "Cabinet"
 *
 * Values reference the custom properties in tokens.css rather than repeating
 * hex literals, so there is exactly one place a colour can change. Tailwind's
 * opacity modifiers (bg-cream/50) will NOT work against var() references — that
 * is intentional. This system has no translucency: hairlines, hard edges and
 * the glass do the containing.
 */
module.exports = {
  theme: {
    extend: {
      colors: {
        /* identity */
        spruce:      'var(--spruce)',       // PAPER ONLY
        'clay-deep': 'var(--clay-deep)',    // the only accent that acts
        clay:        'var(--clay)',         // 24px+ / borders only
        phosphor:    'var(--phosphor)',     // GLASS ONLY

        /* paper */
        cream:            'var(--cream)',
        'cream-card':     'var(--cream-card)',
        ink:              'var(--ink)',
        'ink-body':       'var(--ink-body)',    // summaries and card body
        'ink-deck':       'var(--ink-deck)',    // decks — never --secondary
        'ink-hint':       'var(--ink-hint)',    // field hints
        secondary:        'var(--secondary)',
        label:            'var(--label)',
        line:             'var(--line)',
        divider:          'var(--divider)',
        settled:          'var(--settled)',
        'settled-line':   'var(--settled-line)',
        unconfirmed:      'var(--unconfirmed)',
        'unconfirmed-line':'var(--unconfirmed-line)',
        'spruce-deep':    'var(--spruce-deep)',

        /* glass */
        screen:          'var(--screen)',
        'screen-raised': 'var(--screen-raised)',
        'screen-line':   'var(--screen-line)',
        'phosphor-dim':  'var(--phosphor-dim)',   // GLASS ONLY
        'clay-glow':     'var(--clay-glow)',      // GLASS ONLY
      },

      fontFamily: {
        display: ['Newsreader', 'Georgia', 'serif'],
        ui:      ['Figtree', 'system-ui', 'sans-serif'],
        readout: ['IBM Plex Mono', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
      },

      /* floors. neither voice goes below 10px. */
      fontSize: {
        label:   ['10px', { lineHeight: '1', letterSpacing: '0.18em' }],
        readout: ['10px', { lineHeight: '1.2' }],
        ui:      ['12px', { lineHeight: '1.5' }],
      },

      letterSpacing: { label: '0.18em' },

      borderRadius: {
        DEFAULT: '2px',
        none: '0',
        sm: '1px',
        md: '4px',   // the ceiling. there is no lg, xl, or full.
      },

      boxShadow: {
        none: 'none',   // there are no soft shadows in this system.
      },

      maxWidth: {
        measure: '620px',   // prose. range 580–640.
      },

      minHeight: { touch: '44px' },
      minWidth:  { touch: '44px' },
    },
  },

  corePlugins: {
    // Retired with the rounded floating card.
    boxShadow: false,
    dropShadow: false,
    // The palette is closed; gradients cannot express it.
    backgroundImage: false,
  },
}
