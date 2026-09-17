import RPi.GPIO as GI

import time as t

GI.setmode(GI.BCM)
GI.setwarnings(False)
led=23

GI.setup(led, GI.OUT)

state=0
time=t.time()
period=1

while 1:
    if t.time()-time>period:
        state=not(state)
        time=t.time()
    GI.output(led, state)