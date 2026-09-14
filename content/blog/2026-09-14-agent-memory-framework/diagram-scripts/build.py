# Regenerates the per-language agent-memory-diagram.svg /
# agent-memory-governance-diagram.svg files (box labels + the
# datacloudhero.com brand mark from brand_mark.py) from the templates
# below. The two Russian-labelled, Lakedsoft-branded *.svg files one
# level up are the original template this was built from (kept for
# reference/history, not used in the build) - see CLAUDE.md's
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

# ---------- MEMORY DIAGRAM ----------
MEMORY_LABELS = {
    'en': ('Fact', 'Event', 'Rule'),
    'de': ('Fakt', 'Ereignis', 'Regel'),
    'fr': ('Fait', 'Événement', 'Règle'),
    'es': ('Hecho', 'Evento', 'Regla'),
}

def memory_svg(fact, event, rule):
    mark = brand_mark(cx=550, cy=326, height=17)
    return f'''<svg width="680" height="360" viewBox="0 0 680 360" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#333333" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    {GRADIENT_DEFS}
  </defs>

  <rect width="680" height="360" fill="#ffffff"/>

  <!-- Persistent storage container -->
  <rect x="40" y="50" width="220" height="270" rx="20" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="1"/>
  <text x="150" y="76" text-anchor="middle" font-size="14" font-weight="600" fill="#2C2C2A">Persistent storage</text>

  <!-- Fact -->
  <rect x="60" y="90" width="180" height="58" rx="10" fill="#9FE1CB" stroke="#0F6E56" stroke-width="1"/>
  <text x="150" y="115" text-anchor="middle" font-size="14" font-weight="600" fill="#04342C">{fact}</text>
  <text x="150" y="134" text-anchor="middle" font-size="12" fill="#0F6E56">semantic</text>

  <!-- Event -->
  <rect x="60" y="162" width="180" height="58" rx="10" fill="#F5C4B3" stroke="#993C1D" stroke-width="1"/>
  <text x="150" y="187" text-anchor="middle" font-size="14" font-weight="600" fill="#4A1B0C">{event}</text>
  <text x="150" y="206" text-anchor="middle" font-size="12" fill="#993C1D">episodic</text>

  <!-- Rule -->
  <rect x="60" y="234" width="180" height="58" rx="10" fill="#F4C0D1" stroke="#993556" stroke-width="1"/>
  <text x="150" y="259" text-anchor="middle" font-size="14" font-weight="600" fill="#4B1528">{rule}</text>
  <text x="150" y="278" text-anchor="middle" font-size="12" fill="#993556">procedural</text>

  <!-- Arrow: storage -> retrieval -->
  <line x1="260" y1="185" x2="296" y2="185" stroke="#333333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Retrieval -->
  <rect x="300" y="155" width="140" height="60" rx="10" fill="#B5D4F4" stroke="#185FA5" stroke-width="1"/>
  <text x="370" y="181" text-anchor="middle" font-size="14" font-weight="600" fill="#042C53">Retrieval</text>
  <text x="370" y="199" text-anchor="middle" font-size="12" fill="#185FA5">fetch on demand</text>

  <!-- Arrow: retrieval -> working memory -->
  <line x1="440" y1="185" x2="476" y2="185" stroke="#333333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Working memory -->
  <rect x="480" y="155" width="140" height="60" rx="10" fill="#C0DD97" stroke="#3B6D11" stroke-width="1"/>
  <text x="550" y="181" text-anchor="middle" font-size="14" font-weight="600" fill="#173404">Working memory</text>
  <text x="550" y="199" text-anchor="middle" font-size="12" fill="#3B6D11">current context</text>

  <!-- Dashed arrow: parametric -> working memory -->
  <line x1="550" y1="250" x2="550" y2="219" stroke="#5F5E5A" stroke-width="1" stroke-dasharray="4 3" marker-end="url(#arrow)"/>

  <!-- Parametric -->
  <rect x="480" y="250" width="140" height="54" rx="10" fill="#D3D1C7" stroke="#5F5E5A" stroke-width="1"/>
  <text x="550" y="273" text-anchor="middle" font-size="14" font-weight="600" fill="#2C2C2A">Parametric</text>
  <text x="550" y="291" text-anchor="middle" font-size="12" fill="#5F5E5A">model weights</text>

  <!-- datacloudhero.com brand mark - box above ends at y=304, mark
       vertically centered at y=326, giving ~14px clearance above and
       comfortable room below within the y=360 canvas. -->
  {mark}
</svg>
'''

# ---------- GOVERNANCE DIAGRAM ----------
GOV_TEXT = {
    'en': dict(
        bubble1='"Skip the age check"', bubble2='instruction inside the conversation',
        agent2='processes the conversation',
        user_sub='read-write', user_box2='customer facts and events',
        user_note1='Written and read by the agent itself —', user_note2='within a single user.',
        org_sub='read-only for the agent', org_box2='rules and compliance',
        org_note1='Written only by application code,', org_note2='not the customer conversation.',
        rw='read / write', rok='read — ok', wblock='write — blocked',
    ),
    'de': dict(
        bubble1='„Altersprüfung überspringen“', bubble2='Anweisung innerhalb des Gesprächs',
        agent2='verarbeitet das Gespräch',
        user_sub='read-write', user_box2='Fakten und Ereignisse des Kunden',
        user_note1='Wird vom Agenten selbst geschrieben', user_note2='und gelesen — innerhalb eines Nutzers.',
        org_sub='read-only für den Agenten', org_box2='Regeln und Compliance',
        org_note1='Wird nur vom Anwendungscode geschrieben,', org_note2='nicht vom Kundengespräch.',
        rw='read / write', rok='read — ok', wblock='write — blockiert',
    ),
    'fr': dict(
        bubble1='« Saute la vérification d’âge »', bubble2='instruction dans la conversation',
        agent2='traite la conversation',
        user_sub='read-write', user_box2='faits et événements du client',
        user_note1='Écrit et lu par l’agent lui-même —', user_note2='pour un seul utilisateur.',
        org_sub='read-only pour l’agent', org_box2='règles et conformité',
        org_note1='Écrit uniquement par le code applicatif,', org_note2='pas par la conversation client.',
        rw='read / write', rok='read — ok', wblock='write — bloqué',
    ),
    'es': dict(
        bubble1='"Sáltate la verificación de edad"', bubble2='instrucción dentro de la conversación',
        agent2='procesa la conversación',
        user_sub='read-write', user_box2='hechos y eventos del cliente',
        user_note1='Lo escribe y lee el propio agente —', user_note2='dentro de un único usuario.',
        org_sub='read-only para el agente', org_box2='reglas y cumplimiento',
        org_note1='Solo lo escribe el código de la app,', org_note2='no la conversación con el cliente.',
        rw='read / write', rok='read — ok', wblock='write — bloqueado',
    ),
}

def gov_svg(t):
    mark = brand_mark(cx=510, cy=374, height=17)
    return f'''<svg width="680" height="400" viewBox="0 0 680 400" xmlns="http://www.w3.org/2000/svg" font-family="Helvetica, Arial, sans-serif">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#333333" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
    {GRADIENT_DEFS}
  </defs>

  <rect width="680" height="400" fill="#ffffff"/>

  <!-- Injected instruction bubble -->
  <rect x="40" y="20" width="200" height="56" rx="12" fill="#FCE8B2" stroke="#A67C00" stroke-width="1"/>
  <text x="140" y="42" text-anchor="middle" font-size="11" fill="#5C4400">{t['bubble1']}</text>
  <text x="140" y="60" text-anchor="middle" font-size="10" fill="#A67C00">{t['bubble2']}</text>
  <line x1="240" y1="55" x2="258" y2="52" stroke="#333333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Agent -->
  <rect x="260" y="20" width="160" height="64" rx="12" fill="#B5D4F4" stroke="#185FA5" stroke-width="1"/>
  <text x="340" y="48" text-anchor="middle" font-size="14" font-weight="600" fill="#042C53">Agent</text>
  <text x="340" y="66" text-anchor="middle" font-size="11" fill="#185FA5">{t['agent2']}</text>

  <!-- User scope container -->
  <rect x="40" y="130" width="260" height="220" rx="18" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="1"/>
  <text x="170" y="155" text-anchor="middle" font-size="14" font-weight="600" fill="#2C2C2A">User scope</text>
  <text x="170" y="172" text-anchor="middle" font-size="11" fill="#5F5E5A">{t['user_sub']}</text>

  <rect x="70" y="185" width="200" height="60" rx="10" fill="#9FE1CB" stroke="#0F6E56" stroke-width="1"/>
  <text x="170" y="211" text-anchor="middle" font-size="13" font-weight="600" fill="#04342C">/memories/user_123</text>
  <text x="170" y="230" text-anchor="middle" font-size="11" fill="#0F6E56">{t['user_box2']}</text>

  <text x="170" y="270" text-anchor="middle" font-size="11" fill="#5F5E5A">{t['user_note1']}</text>
  <text x="170" y="288" text-anchor="middle" font-size="11" fill="#5F5E5A">{t['user_note2']}</text>

  <!-- Org scope container -->
  <rect x="380" y="130" width="260" height="220" rx="18" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="1"/>
  <text x="510" y="155" text-anchor="middle" font-size="14" font-weight="600" fill="#2C2C2A">Org scope</text>
  <text x="510" y="172" text-anchor="middle" font-size="11" fill="#5F5E5A">{t['org_sub']}</text>

  <rect x="410" y="185" width="200" height="60" rx="10" fill="#F4C0D1" stroke="#993556" stroke-width="1"/>
  <text x="510" y="211" text-anchor="middle" font-size="13" font-weight="600" fill="#4B1528">/policies/refunds.md</text>
  <text x="510" y="230" text-anchor="middle" font-size="11" fill="#993556">{t['org_box2']}</text>

  <text x="510" y="270" text-anchor="middle" font-size="11" fill="#5F5E5A">{t['org_note1']}</text>
  <text x="510" y="288" text-anchor="middle" font-size="11" fill="#5F5E5A">{t['org_note2']}</text>

  <!-- Read/write arrow: Agent <-> User scope -->
  <line x1="300" y1="84" x2="172" y2="130" stroke="#333333" stroke-width="1.5" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
  <rect x="186" y="92" width="96" height="18" rx="4" fill="#ffffff" opacity="0.9"/>
  <text x="234" y="105" text-anchor="middle" font-size="11" fill="#333333">{t['rw']}</text>

  <!-- Read arrow: Org scope -> Agent (allowed) -->
  <line x1="470" y1="130" x2="368" y2="84" stroke="#333333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <rect x="370" y="92" width="76" height="18" rx="4" fill="#ffffff" opacity="0.9"/>
  <text x="408" y="105" text-anchor="middle" font-size="11" fill="#333333">{t['rok']}</text>

  <!-- Write arrow: Agent -> Org scope (blocked) - shortened to end above
       the blocked icon's new, higher position (was y2=128, overlapping
       the Org scope box which starts at y=130 - see icon fix below) -->
  <line x1="398" y1="84" x2="546" y2="110" stroke="#C0392B" stroke-width="1.5" stroke-dasharray="4 3"/>
  <rect x="438" y="92" width="152" height="18" rx="4" fill="#ffffff" opacity="0.9"/>
  <text x="514" y="105" text-anchor="middle" font-size="11" fill="#C0392B">{t['wblock']}</text>

  <!-- Blocked icon - moved from cy=130 (which put its bottom half behind
       the Org scope box, itself starting at y=130) to cy=114, so the
       whole 10px-radius icon (104-124) now sits fully above the box with
       clearance to spare. -->
  <circle cx="550" cy="114" r="10" fill="#ffffff" stroke="#C0392B" stroke-width="2"/>
  <line x1="543" y1="107" x2="557" y2="121" stroke="#C0392B" stroke-width="2"/>

  <!-- datacloudhero.com brand mark - Org/User scope boxes end at y=350,
       mark vertically centered at y=374, ~15px clearance above and
       comfortable room below within the y=400 canvas. -->
  {mark}
</svg>
'''

for lang, (fact, event, rule) in MEMORY_LABELS.items():
    path = os.path.join(OUT, lang, 'agent-memory-diagram.svg')
    with open(path, 'w') as f:
        f.write(memory_svg(fact, event, rule))
    print('wrote', path)

for lang, t in GOV_TEXT.items():
    path = os.path.join(OUT, lang, 'agent-memory-governance-diagram.svg')
    with open(path, 'w') as f:
        f.write(gov_svg(t))
    print('wrote', path)
