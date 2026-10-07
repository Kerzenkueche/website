import sys, numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageEnhance, ImageFont
W,H=1200,1500
def background():
    y=np.linspace(0,1,H)[:,None]
    top=np.array([248,244,237.]); mid=np.array([238,231,220.]); table=np.array([226,214,197.])
    hz=0.80
    bg=np.where(y<hz, top+(mid-top)*(y/hz), mid+(table-mid)*((y-hz)/(1-hz)))
    bg=np.broadcast_to(bg.reshape(H,1,3),(H,W,3)).copy()
    xx=np.linspace(-1,1,W)[None,:]; yy=np.linspace(-1,1,H)[:,None]
    bg*=(1-0.07*(xx**2+0.5*yy**2))[:,:,None]
    return Image.fromarray(np.clip(bg,0,255).astype(np.uint8)).convert('RGBA')
def compose(png, out, bright=1.0, maxw=0.78, maxh=0.84, base=0.92):
    fg=Image.open(png).convert('RGBA'); fg=fg.crop(fg.split()[3].getbbox())
    if bright!=1.0:
        a=fg.split()[3]; rgb=ImageEnhance.Brightness(fg.convert('RGB')).enhance(bright); fg=rgb.convert('RGBA'); fg.putalpha(a)
    s=min(maxw*W/fg.width, maxh*H/fg.height); fg=fg.resize((int(fg.width*s),int(fg.height*s)),Image.LANCZOS)
    c=background(); x=(W-fg.width)//2; b=int(H*base); y0=b-fg.height
    sh=Image.new('L',(W,H),0); d=ImageDraw.Draw(sh)
    d.ellipse((x+fg.width*0.04, b-max(14,fg.width*0.05), x+fg.width*0.96, b+max(12,fg.width*0.04)), fill=115)
    sh=sh.filter(ImageFilter.GaussianBlur(18)); shadow=Image.new('RGBA',(W,H),(80,60,45,0)); shadow.putalpha(sh)
    c=Image.alpha_composite(c,shadow); c.alpha_composite(fg,(x,y0))
    c.convert('RGB').save(out,'JPEG',quality=84,optimize=True,progressive=True)
JOBS={
 'kommunionkerze-regenbogen-kreuz': dict(bright=1.08),
 'kommunionkerze-holy-communion': dict(bright=1.06),
 'kerze-herz-haende': dict(maxw=0.74),
 'formkerze-spirale': dict(),
 'sechseckkerze-blau-weiss': dict(maxh=0.70),
 'muschelkerze-pink': dict(maxw=0.74),
 'perlenkerzen-rot-weiss': dict(maxw=0.84),
}
for n,kw in JOBS.items(): compose(n+'.png', n+'.jpg', **kw); print(n)
# Kontaktbogen
T=400; names=list(JOBS); sheet=Image.new('RGB',(T*4,int(T*1.25)*2),'white')
for i,n in enumerate(names):
    im=Image.open(n+'.jpg'); im.thumbnail((T,int(T*1.25))); sheet.paste(im,((i%4)*T,(i//4)*int(T*1.25)))
sheet.save('bogen.jpg',quality=85)
