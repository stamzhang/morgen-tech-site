import os, subprocess
NAVY='#0D2340'; BLUE='#1A6FD4'; GOLD='#f0c040'; WHITE='#FFFFFF'
SW=14  # stroke
W=70; H=100; GAP=34

def letter(ch):
    # each returns list of path 'd' strings in local coords (0..W x 0..H)
    if ch=='M': return ["M0,100 V0 H70 V100","M35,0 V100"]
    if ch=='R': return ["M0,100 V0 H45 a27,27 0 0 1 0,54 H0","M38,54 L70,100"]
    if ch=='G': return ["M70,22 A38,38 0 1 0 70,58 H40"]
    if ch=='E': return ["M70,0 H0 V100 H70","M0,50 H56"]
    if ch=='N': return ["M0,100 V0 L70,100 V0"]
    if ch=='T': return ["M0,0 H70","M35,0 V100"]
    if ch=='C': return ["M70,22 A38,38 0 1 0 70,78"]
    if ch=='H': return ["M0,0 V100","M70,0 V100","M0,50 H70"]
    raise KeyError(ch)

def mark(cx,cy,r,ring,spike,sw=SW):
    p=[]
    p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{ring}" stroke-width="{sw}"/>')
    s=r*0.74
    # damped ringing transient: flat, sharp rise, undershoot, smaller overshoot, settle
    pts=[(-1.0,0),(-0.55,0),(-0.42,-0.92),(-0.22,0.55),(-0.02,-0.30),(0.16,0.14),(0.32,-0.05),(0.5,0),(1.0,0)]
    d="M"+" L".join(f"{cx+x*s:.1f},{cy+y*s:.1f}" for x,y in pts)
    p.append(f'<path d="{d}" fill="none" stroke="{spike}" stroke-width="{sw*0.72}" stroke-linecap="round" stroke-linejoin="round"/>')
    return "\n".join(p)

def wordmark(x0,y0,color,ring,spike,scale=1.0,tech=True):
    out=[]; x=x0
    word="MORGEN"
    for i,ch in enumerate(word):
        if ch=='O':
            out.append(mark(x+W/2, y0+H/2, 50-SW/2+0, ring, spike))
            # O is a bit wider than W: use circle diameter 100
            x+=100+GAP-  (100-W)/2  # keep optical spacing
            continue
        for d in letter(ch):
            out.append(f'<path transform="translate({x},{y0})" d="{d}" fill="none" stroke="{color}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round"/>')
        x+=W+GAP
    width=x-GAP-x0
    if tech:
        # TECH: small tracked letters right-aligned under? place after word, baseline aligned, smaller
        tx=x0+width+40; ty=y0+H-54; sc=0.54
        tw=0
        for ch in "TECH":
            for d in letter(ch):
                out.append(f'<path transform="translate({tx+tw},{ty}) scale({sc})" d="{d}" fill="none" stroke="{ring}" stroke-width="{SW/sc*0.8}" stroke-linecap="round" stroke-linejoin="round"/>')
            tw+=(W+GAP-8)*sc
        width=tx+tw-(GAP-8)*sc-x0
    return "\n".join(out), width

# fix O spacing: circle centered so its left edge aligns like other letters
def wordmark2(x0,y0,color,ring,spike,tech=True):
    out=[]; x=x0
    for ch in "MORGEN":
        if ch=='O':
            D=104
            out.append(mark(x+D/2, y0+H/2, (D-SW)/2, ring, spike))
            x+=D+GAP-6
            continue
        for d in letter(ch):
            out.append(f'<path transform="translate({x},{y0})" d="{d}" fill="none" stroke="{color}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round"/>')
        x+=W+GAP
    width=x-GAP-x0
    if tech:
        tx=x0+width+44; sc=0.5; ty=y0+H-H*sc
        tw=0
        for ch in "TECH":
            for d in letter(ch):
                out.append(f'<path transform="translate({tx+tw},{ty}) scale({sc})" d="{d}" fill="none" stroke="{ring}" stroke-width="{SW/sc*0.75}" stroke-linecap="round" stroke-linejoin="round"/>')
            tw+=(W+GAP+6)*sc
        width=tx+tw-(GAP+6)*sc-x0
    return "\n".join(out), width

def svg(w,h,body,bg=None):
    b=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{b}\n{body}\n</svg>'

variants={}
# horizontal, light bg
body,wd=wordmark2(60,60,NAVY,BLUE,GOLD); variants['morgen-tech_horizontal_color']=(svg(wd+120,220,body),None)
body,wd=wordmark2(60,60,WHITE,'#5fa8f8',GOLD); variants['morgen-tech_horizontal_white']=(svg(wd+120,220,body),NAVY)
body,wd=wordmark2(60,60,NAVY,NAVY,NAVY); variants['morgen-tech_horizontal_mono-black']=(svg(wd+120,220,body),None)
body,wd=wordmark2(60,60,WHITE,WHITE,WHITE); variants['morgen-tech_horizontal_mono-white']=(svg(wd+120,220,body),NAVY)
# wordmark only (no TECH)
body,wd=wordmark2(60,60,NAVY,BLUE,GOLD,tech=False); variants['morgen_wordmark_color']=(svg(wd+120,220,body),None)
# mark only
variants['mark_color']=(svg(160,160,mark(80,80,52,BLUE,GOLD,sw=16)),None)
variants['mark_white']=(svg(160,160,mark(80,80,52,'#5fa8f8',GOLD,sw=16)),NAVY)
variants['mark_mono']=(svg(160,160,mark(80,80,52,NAVY,NAVY,sw=16)),None)
# stacked: mark above wordmark
variants['favicon']=(svg(64,64,mark(32,32,24,BLUE,GOLD,sw=9)),None)

os.makedirs('svg',exist_ok=True); os.makedirs('png',exist_ok=True)
for k,(s,bg) in variants.items():
    open(f'svg/{k}.svg','w').write(s)
print(list(variants))
