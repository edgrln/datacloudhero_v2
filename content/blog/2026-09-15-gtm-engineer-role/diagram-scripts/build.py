# Regenerates the per-language gtm-engineer-stack.svg files (box labels +
# the datacloudhero.com brand mark from brand_mark.py) from the template
# below. The gtm-engineer-stack.svg one level up is the original
# Russian-labelled, LakedApp-branded template this was built from (kept
# for reference/history, not used in the build) - see CLAUDE.md's
# "Multi-language content" section. After editing this file, also run
# render.py to re-rasterize the SVGs to the PNGs the articles actually
# reference via {attach}.
#
# Usage: python3 build.py   (run from anywhere; paths are relative to
# this script's own location, not the caller's cwd)
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from brand_mark import brand_mark, GRADIENT_DEFS

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEXT = {
    'en': dict(
        cap_top='Revenue action', cap_top_sub='email · lead routing · CRM record',
        gtm='GTM Engineer', gtm_sub='revenue workflows: scoring, routing, outreach', gtm_for='→ sales, marketing, RevOps',
        ae='Analytics Engineer', ae_sub='transformations, clean datasets (dbt / SQL)', ae_for='→ business users, self-service BI',
        de_='Data Engineer', de_sub='data pipelines and infrastructure', de_for='→ data scientists, analysts, the whole company',
        cap_bottom='Raw data', cap_bottom_sub='APIs, databases, events',
        caption='One stack, three layers: from infrastructure to a revenue action',
    ),
    'fr': dict(
        cap_top='Action revenue', cap_top_sub='e-mail · routage de lead · fiche CRM',
        gtm='GTM Engineer', gtm_sub='workflows revenue : scoring, routage, outreach', gtm_for='→ sales, marketing, RevOps',
        ae='Analytics Engineer', ae_sub='transformations, datasets propres (dbt / SQL)', ae_for='→ utilisateurs métier, self-service BI',
        de_='Data Engineer', de_sub="pipelines et infrastructure de données", de_for='→ data scientists, analystes, toute l’entreprise',
        cap_bottom='Données brutes', cap_bottom_sub='API, bases de données, événements',
        caption='Une seule stack, trois couches : de l’infrastructure à l’action revenue',
    ),
    'de': dict(
        cap_top='Revenue-Aktion', cap_top_sub='E-Mail · Lead-Routing · CRM-Eintrag',
        gtm='GTM Engineer', gtm_sub='Revenue-Workflows: Scoring, Routing, Outreach', gtm_for='→ Sales, Marketing, RevOps',
        ae='Analytics Engineer', ae_sub='Transformationen, saubere Datensätze (dbt / SQL)', ae_for='→ Business-User, Self-Service-BI',
        de_='Data Engineer', de_sub='Datenpipelines und Infrastruktur', de_for='→ Data Scientists, Analysten, das ganze Unternehmen',
        cap_bottom='Rohdaten', cap_bottom_sub='APIs, Datenbanken, Events',
        caption='Ein Stack, drei Schichten: von der Infrastruktur zur Revenue-Aktion',
    ),
    'es': dict(
        cap_top='Acción de revenue', cap_top_sub='email · enrutamiento de leads · registro en el CRM',
        gtm='GTM Engineer', gtm_sub='workflows de revenue: scoring, enrutamiento, outreach', gtm_for='→ sales, marketing, RevOps',
        ae='Analytics Engineer', ae_sub='transformaciones, datasets limpios (dbt / SQL)', ae_for='→ usuarios de negocio, self-service BI',
        de_='Data Engineer', de_sub='pipelines e infraestructura de datos', de_for='→ data scientists, analistas, toda la empresa',
        cap_bottom='Datos crudos', cap_bottom_sub='APIs, bases de datos, eventos',
        caption='Un solo stack, tres capas: de la infraestructura a la acción de revenue',
    ),
}

def stack_svg(t):
    mark = brand_mark(cx=280, cy=525, height=12)
    return f'''<svg width="560" height="560" viewBox="0 0 560 560" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#333333" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    {GRADIENT_DEFS}
  </defs>

  <rect width="560" height="560" fill="#ffffff"/>

  <!-- Revenue action cap -->
  <rect x="160" y="20" width="240" height="50" rx="25" fill="#ffffff" stroke="#bab6b6" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="280" y="41" text-anchor="middle" font-size="13" font-weight="600" fill="#605d5d">{t['cap_top']}</text>
  <text x="280" y="58" text-anchor="middle" font-size="11" fill="#7d7979">{t['cap_top_sub']}</text>

  <line x1="280" y1="96" x2="280" y2="72" stroke="#333333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- GTM Engineer layer -->
  <rect x="60" y="100" width="440" height="90" rx="14" fill="#fff3e4" stroke="#a06f24" stroke-width="1.25"/>
  <text x="84" y="134" font-size="18" font-weight="600" fill="#5a3b0a">{t['gtm']}</text>
  <text x="84" y="156" font-size="13" fill="#7d5411">{t['gtm_sub']}</text>
  <text x="84" y="176" font-size="11" fill="#a06f24">{t['gtm_for']}</text>

  <line x1="280" y1="206" x2="280" y2="192" stroke="#333333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Analytics Engineer layer -->
  <rect x="60" y="210" width="440" height="90" rx="14" fill="#d7d3d3" stroke="#605d5d" stroke-width="1"/>
  <text x="84" y="244" font-size="18" font-weight="600" fill="#2d2b2b">{t['ae']}</text>
  <text x="84" y="266" font-size="13" fill="#444141">{t['ae_sub']}</text>
  <text x="84" y="286" font-size="11" fill="#605d5d">{t['ae_for']}</text>

  <line x1="280" y1="316" x2="280" y2="302" stroke="#333333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Data Engineer layer -->
  <rect x="60" y="320" width="440" height="90" rx="14" fill="#eae7e7" stroke="#7d7979" stroke-width="1"/>
  <text x="84" y="354" font-size="18" font-weight="600" fill="#2d2b2b">{t['de_']}</text>
  <text x="84" y="376" font-size="13" fill="#444141">{t['de_sub']}</text>
  <text x="84" y="396" font-size="11" fill="#7d7979">{t['de_for']}</text>

  <line x1="280" y1="430" x2="280" y2="412" stroke="#333333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Raw data cap -->
  <rect x="160" y="430" width="240" height="50" rx="25" fill="#ffffff" stroke="#bab6b6" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="280" y="451" text-anchor="middle" font-size="13" font-weight="600" fill="#605d5d">{t['cap_bottom']}</text>
  <text x="280" y="468" text-anchor="middle" font-size="11" fill="#7d7979">{t['cap_bottom_sub']}</text>

  <!-- Caption -->
  <text x="280" y="500" text-anchor="middle" font-size="12" fill="#605d5d" font-style="italic">{t['caption']}</text>

  <!-- datacloudhero.com brand mark - raw-data cap ends at y=480, mark
       vertically centered at y=525, below the italic caption at y=500,
       within the y=560 canvas. -->
  {mark}
</svg>
'''

for lang, t in TEXT.items():
    path = os.path.join(OUT, lang, 'gtm-engineer-stack.svg')
    with open(path, 'w') as f:
        f.write(stack_svg(t))
    print('wrote', path)
