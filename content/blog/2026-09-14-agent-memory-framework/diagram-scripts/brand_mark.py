# Reusable "datacloudhero.com" brand-mark generator for the diagram SVGs
# in this article (see build.py). ICON_ELEMENTS/GRADIENT_DEFS are the
# icon-only portion of themes/mytheme/static/img/logo.svg (its circle +
# 12 paths, viewBox-native coordinates ~x:3383-3939 y:60-410 - the site
# wordmark's icon sits to the right of the "datacloudhero.com" text
# there too), copied verbatim with the gradient ids renamed (dchPaint*)
# to avoid colliding if this ever needs to sit in the same document as
# the real logo.svg. brand_mark() re-derives the icon's on-canvas
# position from a *measured* text width (see build.py's comment on
# text_w) rather than the font's nominal size, since the two rarely
# match for a bold sans at small sizes - if the font/weight/size ever
# changes, remeasure via canvas.measureText() before touching text_w.
ICON_ELEMENTS = '''<circle cx="147" cy="147" r="147" transform="matrix(-1 0 0 1 3792 60)" fill="url(#dchPaint0)"/>
<path d="M3393 257.934C3393 330.314 3446.67 386 3519.01 386C3591.35 386 3650 327.324 3650 254.944C3650 184.4 3594.29 126.873 3524.49 124C3523.49 124 3508.65 149.8 3506.06 162.258C3493.38 223.161 3393 185.553 3393 257.934Z" fill="#1BAB53" style="mix-blend-mode:multiply"/>
<path d="M3401 278.5C3401 351.125 3461.37 401.5 3534 401.5C3606.63 401.5 3664 351.125 3664 278.5C3664 205.875 3605.13 147 3532.5 147C3524.83 147 3517.31 147.657 3510 148.917C3501.5 181.5 3480.33 168.001 3472.5 171C3423.09 189.916 3401 222.434 3401 278.5Z" fill="#088D4A" fill-opacity="0.8" style="mix-blend-mode:lighten"/>
<path d="M3656 295.5C3656 368.125 3685.37 401 3758 401C3830.63 401 3891 373.125 3891 300.5C3891 227.875 3806.5 219.5 3785 164C3712.37 164 3656 222.875 3656 295.5Z" fill="#D9D9D9"/>
<path d="M3634 316C3634 399.947 3702.05 335 3786 335C3827.5 260.5 3812 206 3806.5 192C3801 178 3793 167.5 3790.5 164.066C3789.01 164.022 3787.51 164 3786 164C3702.05 164 3634 232.053 3634 316Z" fill="#9FD85E"/>
<path d="M3633.5 404.5L3606 372.5C3596.5 372.5 3555.5 371.5 3505.5 355.5C3455.5 339.5 3383 278 3383 278C3383 278 3377.5 325.5 3412 364C3448.29 404.5 3492 404.5 3492 404.5H3560H3633.5Z" fill="url(#dchPaint1)"/>
<path d="M3668 404.5L3637.5 370.5C3637.5 370.5 3737.37 349.041 3772.5 274C3805.5 203.5 3785 164.5 3785 164.5C3785 164.5 3800.77 166 3808.5 167.5C3816.03 168.962 3827.5 172.5 3827.5 172.5C3827.5 172.5 3839.95 246 3798.5 317.5C3757.05 389 3714 404.5 3714 404.5H3668Z" fill="url(#dchPaint2)"/>
<path d="M3505.5 161.5L3480 168C3480 168 3474.41 190 3480 213C3484.75 232.53 3497 248.5 3497 248.5C3513.5 268.556 3634 404.5 3634 404.5H3668C3668 404.5 3606 335.5 3549 270C3543.17 263.301 3517.82 234.343 3513.5 228C3506 217 3503.73 208.054 3503 200C3501 178 3505.5 161.5 3505.5 161.5Z" fill="white"/>
<path d="M3827.5 172.5C3827.5 172.5 3839.95 246 3798.5 317.5C3777.67 353.425 3756.44 375.213 3740.47 388V404.5H3801.5C3801.5 404.5 3899 397.5 3907.5 290C3914.26 204.5 3827.5 172.5 3827.5 172.5Z" fill="#7AC449" fill-opacity="0.7"/>
<path d="M3641.5 340C3641.5 348.424 3701.5 338 3712 330C3740.75 347.455 3740.5 392.988 3740.5 404.5C3773.5 404.5 3758.75 404.5 3802.5 404.5C3810 402 3840 398 3865 378C3876.73 368.613 3897.5 345 3901 320.75C3901 246.882 3841.23 187 3767.5 187C3635 191.5 3641.5 266.132 3641.5 340Z" fill="url(#dchPaint3)" style="mix-blend-mode:darken"/>
<path d="M3600.5 265L3582 249.5C3582 249.5 3624 193.5 3688.5 219C3736.5 237.977 3740 288.5 3740 288.5C3740 288.5 3739.72 322.742 3740 345C3740.29 367.851 3740.5 404.5 3740.5 404.5H3714.5C3714.5 404.5 3714.02 334.326 3714 290C3714 290 3710 249.5 3670 239.5C3630 229.5 3600.5 265 3600.5 265Z" fill="white"/>
<path d="M3505.5 355.5C3455.5 339.5 3383 278 3383 278C3383 278 3386.33 237 3408.5 209.5C3439.14 171.5 3480 168 3480 168C3480 168 3474.41 190 3480 213C3484.75 232.53 3497 248.5 3497 248.5C3513.5 268.556 3605.5 372.5 3605.5 372.5C3596 372.5 3555.5 371.5 3505.5 355.5Z" fill="url(#dchPaint4)"/>
<path d="M3600.5 265L3582 249.5L3531.5 249.5C3588.5 315 3637.5 370.5 3637.5 370.5C3637.5 370.5 3656.5 366.565 3681 355.5C3706.5 343.984 3714 337.5 3714 337.5C3714 337.5 3714.02 334.326 3714 290C3714 290 3710 249.5 3670 239.5C3630 229.5 3600.5 265 3600.5 265Z" fill="#058A49"/>'''

GRADIENT_DEFS = '''<linearGradient id="dchPaint0" x1="147" y1="0" x2="147" y2="294" gradientUnits="userSpaceOnUse"><stop stop-color="#7AC449"/><stop offset="1" stop-color="#3B5E23"/></linearGradient>
<linearGradient id="dchPaint1" x1="3490.23" y1="278" x2="3525.95" y2="404.5" gradientUnits="userSpaceOnUse"><stop stop-color="#0AB064"/><stop offset="1" stop-color="#044A2A"/></linearGradient>
<linearGradient id="dchPaint2" x1="3733.38" y1="164.5" x2="3733.38" y2="404.5" gradientUnits="userSpaceOnUse"><stop offset="0.360577" stop-color="#0AB064"/><stop offset="1" stop-color="#044A2A"/></linearGradient>
<linearGradient id="dchPaint3" x1="3641.45" y1="294.392" x2="3901" y2="297.108" gradientUnits="userSpaceOnUse"><stop stop-color="#058A49"/><stop offset="1" stop-color="#7AC449" stop-opacity="0.6"/></linearGradient>
<linearGradient id="dchPaint4" x1="3539.97" y1="168" x2="3448.53" y2="372.5" gradientUnits="userSpaceOnUse"><stop offset="0.0336538" stop-color="#08BE65"/><stop offset="0.682692" stop-color="#03713B"/></linearGradient>'''


def brand_mark(cx, cy, font_size=15, icon_h=17):
    """Returns an SVG <g> for the datacloudhero.com brand mark, horizontally
    centered at (cx, cy) [cy = vertical center of the whole mark]."""
    icon_native_w, icon_native_h = 556.0, 344.5
    icon_native_x0, icon_native_y0 = 3383.0, 60.0
    scale = icon_h / icon_native_h
    icon_w = icon_native_w * scale
    text_w = font_size * 9.224  # measured via canvas.measureText at 15px bold Helvetica/Arial
    gap = font_size * 0.35
    total_w = text_w + gap + icon_w
    x0 = cx - total_w / 2
    text_baseline_y = cy + font_size * 0.32
    icon_y0 = cy - icon_h / 2
    icon_x0 = x0 + text_w + gap
    return f'''<g>
    <text x="{x0:.1f}" y="{text_baseline_y:.1f}" font-family="Helvetica, Arial, sans-serif" font-size="{font_size}" font-weight="700"><tspan fill="#1BAB53">datacloudhero</tspan><tspan fill="#111111">.com</tspan></text>
    <g transform="translate({icon_x0:.1f},{icon_y0:.1f}) scale({scale:.5f}) translate({-icon_native_x0:.1f},{-icon_native_y0:.1f})">
{ICON_ELEMENTS}
    </g>
  </g>'''
