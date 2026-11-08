import json, subprocess, urllib.parse, os
from pathlib import Path
root=Path(__file__).resolve().parent.parent
chrome='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
P=[
 ("06-always-cold","mug-blanket.jpg","30% 40%","For the one who's always cold","A plush they can warm up","Warmies Original heats in the microwave and smells softly of lavender."),
 ("07-microwave","sofa-bear.jpg","60% 50%","Cozy gift idea","Warm it, hug it, repeat","A lightly weighted plush, 13 inches and about 1.6 lb."),
 ("08-kids-bedtime","small-bear.jpg","50% 30%","Gifts for kids","A bedtime buddy with a little weight","Warmies Original, a lightly weighted plush. Read the label and heat only as directed."),
 ("09-winter-nights","knit-blanket.jpg","40% 60%","Long winter nights","The hot-water bottle, but huggable","A weighted plush you warm in the microwave."),
 ("10-black-friday","big-bear.jpg","50% 40%","Black Friday gift idea","A cozy gift they'll use all winter","A warm, weighted, lavender-scented plush they can heat up again and again."),
 ("11-cyber-monday","hero-sleep.jpg","50% 50%","Cyber Monday gift idea","Comfort for cold winter nights","A microwavable weighted plush with a soft lavender scent."),
 ("12-grandparents","mug-blanket.jpg","70% 60%","Gifts for grandparents","Warm hands, warm heart","An easy, cozy gift for anyone who runs cold."),
 ("13-still-shopping","sofa-bear.jpg","30% 60%","Still shopping?","A cozy gift for anyone on your list","Warmies Original: a weighted plush that warms in the microwave."),
]
out=[]
for slug,img,pos,k,h,p in P:
    q=urllib.parse.urlencode({'img':img,'pos':pos,'k':k,'h':h,'p':p})
    url=f"file://{root}/pins/template.html?{q}"
    dst=root/'pins'/f'{slug}.png'
    subprocess.run([chrome,'--headless=new','--disable-gpu','--hide-scrollbars','--force-device-scale-factor=1',
                    '--window-size=1000,1500','--virtual-time-budget=4000',f'--screenshot={dst}',url],
                   capture_output=True,timeout=90)
    out.append({'slug':slug,'img':img,'k':k,'h':h,'p':p,'exists':dst.exists()})
print(json.dumps([(o['slug'],o['exists']) for o in out]))
