#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Show biorhythm warnings like the KOSMOS-1 calculator with Conky
P: physical
E: emotional
I: intellectual

2013-08-13

Red: critical days
Orange: mini-critical days
See http://decodesystems.com/kosmos-1.html

argument 1: Skip x days ahead (0 = today). Useful to output the next several days in Conky;
                 just call bioconky several times with offsets 0,1,2,3,...

"""

dd,mm,yy=1,1,1990

from datetime import date
from sys import argv

t0 = date(yy,mm,dd).toordinal()
t1 = date.today().toordinal()

wa=(
((1,12,13),(7,18)),
((1,15),(8,22)),
((1,17,18),(9,26))
)

s = {'_': '${color green}●${color}', 'y': '${color yellow}●${color}', 'r': '${color red}●${color}'}

out = ""

try:
    dt = int(argv[1])
except:
    dt = 0
t = t1 + dt

w = ['_','_','_']
o = ['*','*','*']
for c in range(3):
    p = 23+5*c
    v = ((t-t0) % p)+1
    if (v-1) <= p/2:
        o[c] = 'H'
    if (v-1) >= p/2:
        o[c] = 'T'
    if v in wa[c][0]:
        w[c] = 'r'
        o[c] = 'K'
    if v in wa[c][1]:
        w[c] = 'y'
for x in w:
    out += s[x] + ' '
for x in o:
    out += x + ' '

print(out)
