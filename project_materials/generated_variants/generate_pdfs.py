import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas as rl_canvas

W, H = A4

# ─── VARIANTS: layout + color paired together ───────────────────────────────
VARIANTS = [
    {
        'num':      '01',
        'layout':   'centralny',
        'label':    'Wariant 1 — Hero centralny',
        'color_name': 'Bialy + Granatowy Indygo',
        'desc':     'Hero wycentrowany, uslugi 2x2, kroki poziome, kontakt pionowo.',
        'P':  '#1B3A6B', 'L':  '#EBF0FB', 'M':  '#C3CFEA',
        'BG': '#FFFFFF',  'B2': '#F0F4FF', 'TX': '#1B2A45',
        'swatches': [('#1B3A6B','Glowny'), ('#EBF0FB','Karty'), ('#C3CFEA','Muted'),
                     ('#FFFFFF','Tlo'), ('#F0F4FF','Sekcje'), ('#1B2A45','Tekst')],
        'filename': 'DMSolutions_W1_Centralny_Granat.pdf',
    },
    {
        'num':      '02',
        'layout':   'podzielony',
        'label':    'Wariant 2 — Hero podzielony',
        'color_name': 'Bialy + Klasyczny Antracyt',
        'desc':     'Hero split (tekst + foto), uslugi karuzela, kroki z obrazem, kontakt 2-kolumny.',
        'P':  '#1F1F1F', 'L':  '#EFEFEF', 'M':  '#AAAAAA',
        'BG': '#FFFFFF',  'B2': '#EEEEEE', 'TX': '#111111',
        'swatches': [('#1F1F1F','Glowny'), ('#EFEFEF','Karty'), ('#AAAAAA','Muted'),
                     ('#FFFFFF','Tlo'), ('#EEEEEE','Sekcje'), ('#111111','Tekst')],
        'filename': 'DMSolutions_W2_Podzielony_Antracyt.pdf',
    },
    {
        'num':      '03',
        'layout':   'pelny',
        'label':    'Wariant 3 — Hero pelny ekran',
        'color_name': 'Bialy + Zielen Lesna',
        'desc':     'Hero fullscreen z nawigacja, uslugi 4 karty, os czasu, kontakt centralny.',
        'P':  '#1A4731', 'L':  '#E2F0E8', 'M':  '#9ABFAA',
        'BG': '#FFFFFF',  'B2': '#EAF2ED', 'TX': '#0F2818',
        'swatches': [('#1A4731','Glowny'), ('#E2F0E8','Karty'), ('#9ABFAA','Muted'),
                     ('#FFFFFF','Tlo'), ('#EAF2ED','Sekcje'), ('#0F2818','Tekst')],
        'filename': 'DMSolutions_W3_Pelny_Zielen.pdf',
    },
]


# ─── SHARED DRAWING HELPERS ─────────────────────────────────────────────────
def hc(h): return HexColor(h)

class Draw:
    def __init__(self, cv, v, fx, fw):
        self.cv = cv
        self.P, self.L, self.M = v['P'], v['L'], v['M']
        self.BG, self.B2, self.TX = v['BG'], v['B2'], v['TX']
        self.fx = fx
        self.fw = fw
        self.ix = fx + 3*mm
        self.iw = fw - 6*mm

    def sec_tag(self, text, y, dark=False):
        th = 5*mm
        self.cv.setFillColor(hc(self.P) if dark else hc(self.L))
        self.cv.rect(self.fx, y - th, self.fw, th, fill=1, stroke=0)
        self.cv.setFillColor(hc('#FFFFFF') if dark else hc(self.P))
        self.cv.setFont('Helvetica-Bold', 5)
        self.cv.drawString(self.ix, y - th + 1.6*mm, text.upper())
        self.cv.setStrokeColor(hc(self.M))
        self.cv.setLineWidth(0.3)
        self.cv.line(self.fx, y - th, self.fx + self.fw, y - th)
        return y - th

    def section_bg(self, y, h, alt=False):
        self.cv.setFillColor(hc(self.B2) if alt else hc(self.BG))
        self.cv.rect(self.fx, y - h, self.fw, h, fill=1, stroke=0)

    def photo(self, x, y, w, h, tone=0):
        palettes = [
            [hc('#C5D0E4'), hc('#B0BED8'), hc('#9AAEC8')],
            [hc('#C8C0B0'), hc('#B8B0A0'), hc('#A8A090')],
            [hc('#B8D0BE'), hc('#A8C0AE'), hc('#98B09E')],
        ]
        cols = palettes[tone % 3]
        self.cv.setFillColor(cols[0])
        self.cv.roundRect(x, y, w, h, 1*mm, fill=1, stroke=0)
        self.cv.setFillColor(cols[1])
        self.cv.roundRect(x, y, w, h * 0.55, 1*mm, fill=1, stroke=0)
        self.cv.setFillColor(cols[2])
        self.cv.roundRect(x, y, w, h * 0.28, 1*mm, fill=1, stroke=0)

    def card(self, x, y, w, h, with_photo=False):
        self.cv.setFillColor(hc(self.BG))
        self.cv.setStrokeColor(hc(self.M))
        self.cv.setLineWidth(0.4)
        self.cv.roundRect(x, y, w, h, 1.5*mm, fill=1, stroke=1)
        if with_photo:
            self.photo(x + 0.5*mm, y + h - 0.5*mm - 10*mm, w - 1*mm, 10*mm)
            oy = y + h - 13*mm
        else:
            self.cv.setFillColor(hc(self.L))
            self.cv.roundRect(x + 2*mm, y + h - 7.5*mm, 5*mm, 5.5*mm, 1*mm, fill=1, stroke=0)
            oy = y + h - 10.5*mm
        self.cv.setFillColor(hc('#C0C0C0'))
        self.cv.rect(x + 2*mm, oy, w * 0.6, 1.8*mm, fill=1, stroke=0)
        self.cv.rect(x + 2*mm, oy - 2.5*mm, w * 0.85, 1.4*mm, fill=1, stroke=0)
        self.cv.rect(x + 2*mm, oy - 4.5*mm, w * 0.65, 1.4*mm, fill=1, stroke=0)

    def card_dark(self, x, y, w, h):
        self.cv.setFillColor(hc(self.P + '22'))
        self.cv.roundRect(x, y, w, h, 1.5*mm, fill=1, stroke=0)
        self.cv.setFillColor(hc(self.L))
        self.cv.roundRect(x + 2*mm, y + h - 7.5*mm, 5*mm, 5.5*mm, 1*mm, fill=1, stroke=0)
        self.cv.setFillColor(hc('#FFFFFF'))
        self.cv.rect(x + 2*mm, y + h - 10.5*mm, w*0.6, 1.8*mm, fill=1, stroke=0)
        self.cv.rect(x + 2*mm, y + h - 13*mm, w*0.85, 1.4*mm, fill=1, stroke=0)

    def btn(self, x, y, w, h=5*mm):
        self.cv.setFillColor(hc(self.P))
        self.cv.roundRect(x, y, w, h, 1.5*mm, fill=1, stroke=0)
        self.cv.setFillColor(hc('#FFFFFF'))
        self.cv.rect(x + w*0.25, y + h*0.38, w*0.5, 1.5, fill=1, stroke=0)

    def btn_outline(self, x, y, w, h=5*mm):
        self.cv.setFillColor(hc(self.BG))
        self.cv.setStrokeColor(hc(self.P))
        self.cv.setLineWidth(0.6)
        self.cv.roundRect(x, y, w, h, 1.5*mm, fill=1, stroke=1)
        self.cv.setFillColor(hc(self.P))
        self.cv.rect(x + w*0.22, y + h*0.38, w*0.56, 1.5, fill=1, stroke=0)

    def field(self, x, y, w, h=4.5*mm):
        self.cv.setFillColor(hc('#FFFFFF'))
        self.cv.setStrokeColor(hc(self.M))
        self.cv.setLineWidth(0.4)
        self.cv.roundRect(x, y, w, h, 1*mm, fill=1, stroke=1)

    def gmap(self, x, y, w, h):
        self.cv.setFillColor(hc('#E4EEF8'))
        self.cv.setStrokeColor(hc(self.M))
        self.cv.setLineWidth(0.4)
        self.cv.roundRect(x, y, w, h, 1*mm, fill=1, stroke=1)
        self.cv.setStrokeColor(hc(self.M))
        self.cv.setLineWidth(0.2)
        for i in range(1, 4):
            self.cv.line(x, y + h*i/4, x+w, y + h*i/4)
            self.cv.line(x + w*i/4, y, x + w*i/4, y+h)
        self.cv.setFillColor(hc(self.P))
        self.cv.circle(x + w/2, y + h*0.55, 2.5, fill=1, stroke=0)

    def step_dot(self, x, y, n):
        self.cv.setFillColor(hc(self.P))
        self.cv.circle(x, y, 3*mm, fill=1, stroke=0)
        self.cv.setFillColor(hc('#FFFFFF'))
        self.cv.setFont('Helvetica-Bold', 5)
        self.cv.drawCentredString(x, y - 1.5, str(n))

    def icon_box(self, x, y, w=5*mm, h=5*mm):
        self.cv.setFillColor(hc(self.L))
        self.cv.roundRect(x, y, w, h, 1*mm, fill=1, stroke=0)

    def lines(self, x, y, specs, color='#C0C0C0'):
        # specs: list of (width_pct, height_mm)
        cy = y
        for wpct, hmm in specs:
            self.cv.setFillColor(hc(color))
            self.cv.rect(x, cy - hmm*mm, self.iw * wpct, hmm*mm, fill=1, stroke=0)
            cy -= (hmm + 1.4) * mm
        return cy

    def nav_bar(self, y, transparent=False):
        nh = 9*mm
        if not transparent:
            self.cv.setFillColor(hc(self.BG))
            self.cv.rect(self.fx, y - nh, self.fw, nh, fill=1, stroke=0)
        self.cv.setFillColor(hc(self.P))
        self.cv.roundRect(self.ix, y - nh + 2.5*mm, 7*mm, 4.5*mm, 1*mm, fill=1, stroke=0)
        self.cv.setFillColor(hc('#FFFFFF' if transparent else self.M))
        for i in range(4):
            self.cv.rect(self.ix + 14*mm + i*12*mm, y - nh + 3.8*mm, 9*mm, 1.8*mm, fill=1, stroke=0)
        self.btn(self.fx + self.fw - 3*mm - 16*mm, y - nh + 2.5*mm, 16*mm, 4.5*mm)
        if not transparent:
            self.cv.setStrokeColor(hc(self.M))
            self.cv.setLineWidth(0.3)
            self.cv.line(self.fx, y - nh, self.fx + self.fw, y - nh)
        return y - nh

    def trust_bar(self, y):
        th = 9*mm
        self.cv.setFillColor(hc(self.P))
        self.cv.rect(self.fx, y - th, self.fw, th, fill=1, stroke=0)
        for i in range(3):
            tx_i = self.fx + self.fw*(0.2 + i*0.3) - 9*mm
            self.cv.setFillColor(hc('#FFFFFF'))
            self.cv.rect(tx_i, y - th + 3.8*mm, 11*mm, 2.2*mm, fill=1, stroke=0)
            self.cv.setFillColor(hc('#FFFFFF55'))
            self.cv.rect(tx_i + 1*mm, y - th + 1*mm, 8*mm, 1.4*mm, fill=1, stroke=0)
        return y - th

    def footer_bar(self, y):
        fh = 8*mm
        self.cv.setFillColor(hc(self.TX))
        self.cv.rect(self.fx, y - fh, self.fw, fh, fill=1, stroke=0)
        self.cv.setFillColor(hc(self.BG))
        self.cv.roundRect(self.ix, y - fh + 2*mm, 7*mm, 4*mm, 1*mm, fill=1, stroke=0)
        self.cv.setFillColor(hc('#FFFFFF33'))
        self.cv.rect(self.ix + 9*mm, y - fh + 3*mm, 14*mm, 1.5*mm, fill=1, stroke=0)
        return y - fh


# ─── LAYOUT 1: Hero centralny ───────────────────────────────────────────────
def draw_layout_1(d, ft):
    cy = ft

    # NAV
    cy = d.sec_tag('Nawigacja', cy)
    cy = d.nav_bar(cy)

    # HERO — centered text, bg image
    cy = d.sec_tag('01 · Naglowek', cy)
    hh = 29*mm
    d.photo(d.fx, cy - hh, d.fw, hh, tone=0)
    d.cv.setFillColor(hc(d.P + '66'))
    d.cv.rect(d.fx, cy - hh, d.fw, hh, fill=1, stroke=0)
    cx_c = d.fx + d.fw / 2
    d.cv.setFillColor(hc('#FFFFFF'))
    for dw, dy in [(d.fw*0.6, 9), (d.fw*0.45, 14.5)]:
        d.cv.rect(cx_c - dw/2, cy - dy*mm, dw, 4*mm, fill=1, stroke=0)
    d.cv.setFillColor(hc('#FFFFFF77'))
    d.cv.rect(cx_c - d.fw*0.32, cy - 20*mm, d.fw*0.64, 2*mm, fill=1, stroke=0)
    d.cv.rect(cx_c - d.fw*0.26, cy - 23*mm, d.fw*0.52, 2*mm, fill=1, stroke=0)
    d.btn(cx_c - 20*mm, cy - hh + 3*mm, 18*mm, 5*mm)
    d.btn_outline(cx_c + 2.5*mm, cy - hh + 3*mm, 18*mm, 5*mm)
    cy -= hh

    # TRUST
    cy = d.sec_tag('Pasek zaufania', cy, dark=True)
    cy = d.trust_bar(cy)

    # SERVICES — 2x2 grid
    cy = d.sec_tag('02 · Nasze uslugi', cy)
    sh = 30*mm
    d.section_bg(cy, sh)
    d.cv.setFillColor(hc('#C8C8C8'))
    d.cv.rect(d.ix, cy - 5.5*mm, d.iw*0.38, 2.8*mm, fill=1, stroke=0)
    cw = (d.iw - 3*mm) / 2
    ch = 10*mm
    for row in range(2):
        for col in range(2):
            d.card(d.ix + col*(cw + 3*mm), cy - sh + 1*mm + row*(ch + 2*mm), cw, ch)
    cy -= sh

    # HOW IT WORKS — 4 steps horizontal
    cy = d.sec_tag('03 · Jak dzialamy', cy)
    hwh = 23*mm
    d.section_bg(cy, hwh, alt=True)
    d.cv.setFillColor(hc('#C8C8C8'))
    d.cv.rect(d.ix, cy - 5.5*mm, d.iw*0.35, 2.5*mm, fill=1, stroke=0)
    sw4 = d.iw / 4
    d.cv.setStrokeColor(hc(d.M))
    d.cv.setLineWidth(0.5)
    d.cv.setDash(2, 2)
    d.cv.line(d.ix + sw4*0.5, cy - 12*mm, d.ix + d.iw - sw4*0.5, cy - 12*mm)
    d.cv.setDash()
    for i in range(4):
        sx = d.ix + i*sw4 + sw4*0.5
        d.step_dot(sx, cy - 12*mm, i+1)
        d.cv.setFillColor(hc('#BBBBBB'))
        d.cv.rect(sx - sw4*0.3, cy - 16*mm, sw4*0.6, 1.8*mm, fill=1, stroke=0)
        d.cv.rect(sx - sw4*0.25, cy - 18.5*mm, sw4*0.5, 1.4*mm, fill=1, stroke=0)
    cy -= hwh

    # WHY US — photo left + bullets right
    cy = d.sec_tag('04 · Dlaczego my', cy)
    wyh = 24*mm
    d.section_bg(cy, wyh)
    d.cv.setFillColor(hc('#C8C8C8'))
    d.cv.rect(d.ix, cy - 5.5*mm, d.iw*0.4, 2.5*mm, fill=1, stroke=0)
    d.photo(d.ix, cy - wyh + 1*mm, d.iw*0.35, 20*mm, tone=0)
    bx = d.ix + d.iw*0.4
    for j in range(3):
        by_j = cy - 9*mm - j*5.5*mm
        d.icon_box(bx, by_j)
        d.cv.setFillColor(hc('#BBBBBB'))
        d.cv.rect(bx + 6.5*mm, by_j + 1.2*mm, d.iw*0.4, 1.8*mm, fill=1, stroke=0)
        d.cv.rect(bx + 6.5*mm, by_j - 0.8*mm, d.iw*0.3, 1.4*mm, fill=1, stroke=0)
    cy -= wyh

    # CONTACT — form stacked + map below
    cy = d.sec_tag('05 · Kontakt', cy)
    cnh = 27*mm
    d.section_bg(cy, cnh, alt=True)
    d.cv.setFillColor(hc('#C8C8C8'))
    d.cv.rect(d.ix, cy - 5*mm, d.iw*0.3, 2.5*mm, fill=1, stroke=0)
    d.field(d.ix, cy - 9.5*mm, d.iw)
    d.field(d.ix, cy - 14.5*mm, d.iw)
    d.btn(d.ix, cy - 19.5*mm, d.iw*0.35, 4*mm)
    d.gmap(d.ix, cy - 27*mm + 0.5*mm, d.iw, 7*mm)
    cy -= cnh

    # FOOTER
    cy = d.sec_tag('Stopka', cy, dark=True)
    cy = d.footer_bar(cy)
    return cy


# ─── LAYOUT 2: Hero podzielony ──────────────────────────────────────────────
def draw_layout_2(d, ft):
    cy = ft

    # NAV
    cy = d.sec_tag('Nawigacja', cy)
    cy = d.nav_bar(cy)

    # HERO — text left + photo right
    cy = d.sec_tag('01 · Naglowek', cy)
    hh = 30*mm
    d.section_bg(cy, hh)
    half_hero = (d.iw - 4*mm) / 2
    # text side
    ty = cy - 6*mm
    d.cv.setFillColor(hc(d.M))
    d.cv.rect(d.ix, ty, d.iw*0.35, 2*mm, fill=1, stroke=0)
    ty -= 3.5*mm
    for wpct in [0.9, 0.75, 0.6]:
        d.cv.setFillColor(hc(d.TX))
        d.cv.rect(d.ix, ty, half_hero*wpct, 3.5*mm, fill=1, stroke=0)
        ty -= 5*mm
    d.cv.setFillColor(hc('#C0C0C0'))
    d.cv.rect(d.ix, ty, half_hero*0.85, 1.8*mm, fill=1, stroke=0)
    ty -= 3*mm
    d.cv.rect(d.ix, ty, half_hero*0.7, 1.8*mm, fill=1, stroke=0)
    ty -= 5*mm
    d.btn(d.ix, ty, half_hero*0.42, 5*mm)
    d.btn_outline(d.ix + half_hero*0.46, ty, half_hero*0.38, 5*mm)
    # photo side
    d.photo(d.ix + half_hero + 4*mm, cy - hh + 1*mm, half_hero, hh - 2*mm, tone=1)
    cy -= hh

    # TRUST
    cy = d.sec_tag('Pasek zaufania', cy, dark=True)
    cy = d.trust_bar(cy)

    # SERVICES — carousel 3 cards with photo top
    cy = d.sec_tag('02 · Nasze uslugi (karuzela)', cy)
    sh = 30*mm
    d.section_bg(cy, sh, alt=True)
    d.cv.setFillColor(hc('#C8C8C8'))
    d.cv.rect(d.ix, cy - 5.5*mm, d.iw*0.4, 2.5*mm, fill=1, stroke=0)
    cw3 = (d.iw - 2*3*mm) / 3
    photos = [0, 1, 2]
    for i in range(3):
        cx_c = d.ix + i*(cw3 + 3*mm)
        alpha = 1.0 if i < 2 else 0.35
        # card bg
        d.cv.setFillColor(hc(d.BG))
        d.cv.setStrokeColor(hc(d.M))
        d.cv.setLineWidth(0.4)
        d.cv.roundRect(cx_c, cy - sh + 1*mm, cw3, sh - 8*mm, 1.5*mm, fill=1, stroke=1)
        if alpha < 1:
            # fade last card
            d.cv.setFillColor(HexColor(d.BG + '88'))
            d.cv.roundRect(cx_c, cy - sh + 1*mm, cw3, sh - 8*mm, 1.5*mm, fill=1, stroke=0)
        d.photo(cx_c + 0.5*mm, cy - sh + 1*mm + (sh-8*mm) - 10.5*mm, cw3 - 1*mm, 10*mm, tone=photos[i])
        d.cv.setFillColor(hc('#C0C0C0'))
        d.cv.rect(cx_c + 2*mm, cy - sh + 9.5*mm, cw3*0.65, 1.8*mm, fill=1, stroke=0)
        d.cv.rect(cx_c + 2*mm, cy - sh + 7*mm, cw3*0.85, 1.4*mm, fill=1, stroke=0)
    # carousel dots
    dot_y = cy - sh + 3*mm
    dot_x = d.fx + d.fw/2 - 8*mm
    for i in range(4):
        dw = 5*mm if i == 0 else 2*mm
        dh = 2*mm
        d.cv.setFillColor(hc(d.P) if i == 0 else hc(d.M))
        d.cv.roundRect(dot_x, dot_y, dw, dh, 1*mm, fill=1, stroke=0)
        dot_x += dw + 2*mm
    cy -= sh

    # HOW IT WORKS — numbered list left + photo right
    cy = d.sec_tag('03 · Jak dzialamy', cy)
    hwh = 27*mm
    d.section_bg(cy, hwh)
    half_hw = (d.iw - 4*mm) / 2
    d.cv.setFillColor(hc('#C8C8C8'))
    d.cv.rect(d.ix, cy - 5.5*mm, half_hw*0.65, 2.5*mm, fill=1, stroke=0)
    for i in range(4):
        sy_i = cy - 10*mm - i*4.5*mm
        d.step_dot(d.ix + 3*mm, sy_i + 1.5*mm, i+1)
        d.cv.setFillColor(hc('#C0C0C0'))
        d.cv.rect(d.ix + 8.5*mm, sy_i + 1*mm, half_hw*0.55, 1.8*mm, fill=1, stroke=0)
        d.cv.rect(d.ix + 8.5*mm, sy_i - 1.2*mm, half_hw*0.45, 1.4*mm, fill=1, stroke=0)
    d.photo(d.ix + half_hw + 4*mm, cy - hwh + 1*mm, half_hw, hwh - 2*mm, tone=1)
    cy -= hwh

    # WHY US — dark bg, 3 icon cards + photo strip
    cy = d.sec_tag('04 · Dlaczego my', cy, dark=True)
    wyh = 25*mm
    d.cv.setFillColor(hc(d.P))
    d.cv.rect(d.fx, cy - wyh, d.fw, wyh, fill=1, stroke=0)
    d.cv.setFillColor(hc('#FFFFFF'))
    d.cv.rect(d.ix, cy - 5.5*mm, d.iw*0.42, 2.5*mm, fill=1, stroke=0)
    cw3d = (d.iw - 2*3*mm) / 3
    for i in range(3):
        d.card_dark(d.ix + i*(cw3d+3*mm), cy - 16*mm, cw3d, 9*mm)
    # photo strip
    strip_w = (d.iw - 3*3*mm) / 4
    for i in range(4):
        d.photo(d.ix + i*(strip_w+3*mm), cy - wyh + 1.5*mm, strip_w, 6*mm, tone=i%3)
    cy -= wyh

    # CONTACT — form left + info+map right
    cy = d.sec_tag('05 · Kontakt', cy)
    cnh = 27*mm
    d.section_bg(cy, cnh, alt=True)
    half_c = (d.iw - 4*mm) / 2
    d.cv.setFillColor(hc('#C8C8C8'))
    d.cv.rect(d.ix, cy - 5*mm, d.iw*0.3, 2.5*mm, fill=1, stroke=0)
    d.field(d.ix, cy - 10*mm, half_c)
    d.field(d.ix, cy - 15*mm, half_c)
    d.cv.setFillColor(hc('#FFFFFF'))
    d.cv.setStrokeColor(hc(d.M))
    d.cv.setLineWidth(0.4)
    d.cv.roundRect(d.ix, cy - 21.5*mm, half_c, 5.5*mm, 1*mm, fill=1, stroke=1)
    d.btn(d.ix, cy - 26.5*mm, half_c*0.48, 4.5*mm)
    # right: icon rows + map
    rx = d.ix + half_c + 4*mm
    for j in range(2):
        ry_j = cy - 9*mm - j*5*mm
        d.icon_box(rx, ry_j, 4*mm, 4*mm)
        d.cv.setFillColor(hc('#BBBBBB'))
        d.cv.rect(rx + 5.5*mm, ry_j + 1*mm, half_c*0.65, 1.8*mm, fill=1, stroke=0)
    d.gmap(rx, cy - cnh + 1.5*mm, half_c, 13*mm)
    cy -= cnh

    # FOOTER
    cy = d.sec_tag('Stopka', cy, dark=True)
    cy = d.footer_bar(cy)
    return cy


# ─── LAYOUT 3: Hero pelny ekran ─────────────────────────────────────────────
def draw_layout_3(d, ft):
    cy = ft

    # HERO fullscreen (nav inside)
    cy_tag = d.sec_tag('Nawigacja + 01 · Naglowek', cy)
    hh = 38*mm
    d.photo(d.fx, cy_tag - hh, d.fw, hh, tone=2)
    d.cv.setFillColor(hc(d.P + '88'))
    d.cv.rect(d.fx, cy_tag - hh, d.fw, hh, fill=1, stroke=0)
    # nav inside
    nav_inside_y = cy_tag
    d.cv.setFillColor(hc('#FFFFFF22'))
    d.cv.rect(d.fx, nav_inside_y - 9*mm, d.fw, 9*mm, fill=1, stroke=0)
    d.cv.setFillColor(hc('#FFFFFF'))
    d.cv.roundRect(d.ix, nav_inside_y - 9*mm + 2.5*mm, 7*mm, 4.5*mm, 1*mm, fill=1, stroke=0)
    for i in range(4):
        d.cv.setFillColor(hc('#FFFFFF88'))
        d.cv.rect(d.ix + 14*mm + i*12*mm, nav_inside_y - 9*mm + 3.8*mm, 9*mm, 1.8*mm, fill=1, stroke=0)
    d.cv.setFillColor(hc('#FFFFFF'))
    d.cv.setStrokeColor(hc('#FFFFFF'))
    d.cv.setLineWidth(0.5)
    d.cv.roundRect(d.fx + d.fw - 3*mm - 16*mm, nav_inside_y - 9*mm + 2.5*mm, 16*mm, 4.5*mm, 1.5*mm, fill=0, stroke=1)
    # hero text centered
    cx_c = d.fx + d.fw/2
    d.cv.setFillColor(hc('#FFFFFF55'))
    d.cv.rect(cx_c - d.fw*0.18, cy_tag - 12*mm, d.fw*0.36, 1.8*mm, fill=1, stroke=0)
    d.cv.setFillColor(hc('#FFFFFF'))
    for dw, dy in [(d.fw*0.65, 17), (d.fw*0.5, 22)]:
        d.cv.rect(cx_c - dw/2, cy_tag - dy*mm, dw, 4*mm, fill=1, stroke=0)
    d.cv.setFillColor(hc('#FFFFFF66'))
    d.cv.rect(cx_c - d.fw*0.3, cy_tag - 27*mm, d.fw*0.6, 1.8*mm, fill=1, stroke=0)
    d.btn(cx_c - 11*mm, cy_tag - hh + 3.5*mm, 22*mm, 5*mm)
    cy = cy_tag - hh

    # TRUST
    cy = d.sec_tag('Pasek zaufania', cy, dark=True)
    cy = d.trust_bar(cy)

    # SERVICES — 4 cards in row with photo tops
    cy = d.sec_tag('02 · Nasze uslugi', cy)
    sh = 28*mm
    d.section_bg(cy, sh)
    d.cv.setFillColor(hc('#C8C8C8'))
    d.cv.rect(d.fx + d.fw/2 - d.iw*0.2, cy - 5.5*mm, d.iw*0.4, 2.5*mm, fill=1, stroke=0)
    cw4 = (d.iw - 3*3*mm) / 4
    for i in range(4):
        d.card(d.ix + i*(cw4+3*mm), cy - sh + 1*mm, cw4, 19*mm, with_photo=True)
    cy -= sh

    # HOW IT WORKS — timeline
    cy = d.sec_tag('03 · Jak dzialamy', cy)
    hwh = 22*mm
    d.section_bg(cy, hwh, alt=True)
    d.cv.setFillColor(hc('#C8C8C8'))
    d.cv.rect(d.fx + d.fw/2 - d.iw*0.18, cy - 5.5*mm, d.iw*0.36, 2.5*mm, fill=1, stroke=0)
    sw4 = d.iw / 4
    d.cv.setStrokeColor(hc(d.M))
    d.cv.setLineWidth(1)
    d.cv.line(d.ix + sw4*0.5, cy - 12*mm, d.ix + d.iw - sw4*0.5, cy - 12*mm)
    for i in range(4):
        sx = d.ix + i*sw4 + sw4*0.5
        d.cv.setFillColor(hc(d.BG))
        d.cv.setStrokeColor(hc(d.P))
        d.cv.setLineWidth(1)
        d.cv.circle(sx, cy - 12*mm, 3.5*mm, fill=1, stroke=1)
        d.cv.setFillColor(hc(d.P))
        d.cv.setFont('Helvetica-Bold', 5.5)
        d.cv.drawCentredString(sx, cy - 12*mm - 2, str(i+1))
        d.cv.setFillColor(hc('#BBBBBB'))
        d.cv.rect(sx - sw4*0.28, cy - 17*mm, sw4*0.56, 1.8*mm, fill=1, stroke=0)
        d.cv.rect(sx - sw4*0.23, cy - 19.5*mm, sw4*0.46, 1.4*mm, fill=1, stroke=0)
    cy -= hwh

    # WHY US — text left + photo mosaic right
    cy = d.sec_tag('04 · Dlaczego my', cy)
    wyh = 25*mm
    d.section_bg(cy, wyh)
    half_w = (d.iw - 4*mm) / 2
    d.cv.setFillColor(hc('#C8C8C8'))
    d.cv.rect(d.ix, cy - 5.5*mm, half_w*0.6, 2.5*mm, fill=1, stroke=0)
    for j in range(3):
        by_j = cy - 10*mm - j*5*mm
        d.icon_box(d.ix, by_j)
        d.cv.setFillColor(hc('#BBBBBB'))
        d.cv.rect(d.ix + 6.5*mm, by_j + 1.2*mm, half_w*0.65, 1.8*mm, fill=1, stroke=0)
        d.cv.rect(d.ix + 6.5*mm, by_j - 0.8*mm, half_w*0.5, 1.4*mm, fill=1, stroke=0)
    # mosaic right
    mx = d.ix + half_w + 4*mm
    d.photo(mx, cy - wyh + 9.5*mm, half_w, wyh - 10*mm, tone=2)   # large top
    d.photo(mx, cy - wyh + 1*mm, half_w*0.47, 7*mm, tone=0)        # small bottom left
    d.photo(mx + half_w*0.53, cy - wyh + 1*mm, half_w*0.47, 7*mm, tone=1)  # small bottom right
    cy -= wyh

    # CONTACT — centered CTA + form + map
    cy = d.sec_tag('05 · Kontakt', cy)
    cnh = 27*mm
    d.section_bg(cy, cnh, alt=True)
    cx_c = d.fx + d.fw/2
    d.cv.setFillColor(hc('#C8C8C8'))
    d.cv.rect(cx_c - d.iw*0.2, cy - 5.5*mm, d.iw*0.4, 2.5*mm, fill=1, stroke=0)
    d.cv.rect(cx_c - d.iw*0.3, cy - 9*mm, d.iw*0.6, 1.8*mm, fill=1, stroke=0)
    form_w = d.iw * 0.7
    form_x = cx_c - form_w/2
    d.field(form_x, cy - 13.5*mm, form_w)
    d.field(form_x, cy - 18.5*mm, form_w)
    d.btn(cx_c - 11*mm, cy - 23.5*mm, 22*mm, 4.5*mm)
    d.gmap(form_x, cy - cnh + 0.5*mm, form_w, 3*mm)
    cy -= cnh

    # FOOTER
    cy = d.sec_tag('Stopka', cy, dark=True)
    cy = d.footer_bar(cy)
    return cy


LAYOUT_FUNCS = [draw_layout_1, draw_layout_2, draw_layout_3]


# ─── MAIN PDF BUILDER ────────────────────────────────────────────────────────
def build_pdf(v, layout_fn):
    path = f'C:/Users/Admin/Desktop/project/dmsolutions/{v["filename"]}'
    cv = rl_canvas.Canvas(path, pagesize=A4)

    # BG
    cv.setFillColor(hc('#F2F4F7'))
    cv.rect(0, 0, W, H, fill=1, stroke=0)

    # Top bar
    cv.setFillColor(hc(v['P']))
    cv.rect(0, H - 26*mm, W, 26*mm, fill=1, stroke=0)
    cv.setFillColor(hc('#FFFFFF'))
    cv.setFont('Helvetica', 6.5)
    cv.drawString(14*mm, H - 9*mm, 'NODE48  |  Propozycja graficzna dla DMSolutions')
    cv.setFont('Helvetica-Bold', 6.5)
    cv.drawRightString(W - 14*mm, H - 9*mm, v['num'])

    # Title
    cv.setFillColor(hc(v['TX']))
    cv.setFont('Helvetica-Bold', 16)
    cv.drawString(14*mm, H - 40*mm, v['label'])
    cv.setFont('Helvetica-Bold', 9)
    cv.drawString(14*mm, H - 47*mm, v['color_name'])
    cv.setFillColor(hc('#555555'))
    cv.setFont('Helvetica', 7.5)
    cv.drawString(14*mm, H - 53*mm, v['desc'])

    # Palette swatches
    sw_y = H - 66*mm
    sw_w = 25*mm
    sw_h = 10*mm
    for i, (col, lbl) in enumerate(v['swatches']):
        sx = 14*mm + i * (sw_w + 3*mm)
        cv.setFillColor(hc(col))
        cv.setStrokeColor(hc('#C8C8C8'))
        cv.setLineWidth(0.5)
        cv.roundRect(sx, sw_y, sw_w, sw_h, 2*mm, fill=1, stroke=1)
        cv.setFillColor(hc('#444444'))
        cv.setFont('Helvetica', 5.5)
        cv.drawString(sx, sw_y - 4*mm, lbl)
        cv.setFont('Helvetica', 5)
        cv.drawString(sx, sw_y - 7*mm, col.upper())

    # Wireframe frame
    fx = 14*mm
    fw = W - 28*mm
    ft = H - 80*mm

    # shadow
    cv.setFillColor(hc('#D0D0D0'))
    cv.roundRect(fx + 1.5*mm, ft - 155*mm - 1.5*mm, fw, 155*mm, 2*mm, fill=1, stroke=0)
    # white bg
    cv.setFillColor(hc(v['BG']))
    cv.setStrokeColor(hc('#BBBBBB'))
    cv.setLineWidth(0.5)
    cv.roundRect(fx, ft - 155*mm, fw, 155*mm, 2*mm, fill=1, stroke=1)

    d = Draw(cv, v, fx, fw)
    layout_fn(d, ft)

    # Bottom note
    cv.setFillColor(hc('#888888'))
    cv.setFont('Helvetica', 7)
    cv.drawString(14*mm, 14*mm, 'Propozycja wstepna — kolory i uklad zostana dopracowane po Twojej decyzji.')
    cv.drawRightString(W - 14*mm, 14*mm, 'NODE48  ·  node48.pl')

    # Border
    cv.setStrokeColor(hc(v['P']))
    cv.setLineWidth(1.5)
    cv.roundRect(4*mm, 4*mm, W - 8*mm, H - 8*mm, 3*mm, fill=0, stroke=1)

    cv.save()
    print(f'OK: {v["filename"]}')


for v, fn in zip(VARIANTS, LAYOUT_FUNCS):
    build_pdf(v, fn)
