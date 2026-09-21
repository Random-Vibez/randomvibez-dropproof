#!/usr/bin/env python3
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
h=(root/'index.html').read_text(); js=(root/'app.js').read_text(); css=(root/'styles.css').read_text(); ht=(root/'.htaccess').read_text()
for f in ['index.html','app.js','styles.css','cookie-banner.js','README.md','SECURITY.md','LICENSE','.htaccess']: assert (root/f).exists(),f
for x in ['incident','seller','carrier','reference','expected','delivered','evidence','notes','next','print','export','import','cookie-banner.js']: assert x in h,x
for x in ['localStorage','MAXSTATE','MAXIMPORT','textContent','createElement','window.print','application/json','valid'] : assert x in js,x
for x in ['browser','Not encrypted','No automatic contact','not legal advice']: assert x.lower() in (h+(root/'README.md').read_text()+(root/'SECURITY.md').read_text()).lower(),x
for x in ["connect-src 'none'",'X-Content-Type-Options','X-Frame-Options','Cache-Control']: assert x in ht,x
assert 'prefers-reduced-motion' in css and '@media print' in css
for x in ['fetch(','XMLHttpRequest','innerHTML','document.write']: assert x not in js,x
print('PASS DropProof static contract')
