import RPi.GPIO as GI

import time as t

GI.setmode(GI.BCM)
GI.setwarnings(False)

led=23
button=13
shutdown=10
GI.setup(led, GI.OUT)
GI.setup(button, GI.IN)
GI.setup(shutdown, GI.IN)
state=0
time=t.time()
period=0.2
while not(GI.input(shutdown)):
    if GI.input(button) and t.time()-time>period:
        state=not(state)
        time=t.time()
    GI.output(led, state)

GI.output(led, 0)