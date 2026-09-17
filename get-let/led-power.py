import RPi.GPIO as GI

import time as t

GI.setmode(GI.BCM)
GI.setwarnings(False)

led=23
button=13
shutdown=10
period=3
shim=10**-2
light=0
maxlight=1
disp=100

GI.setup(led, GI.OUT)
GI.setup(button, GI.IN)
GI.setup(shutdown, GI.IN)
state=0
time1=t.time()
timeshim=t.time()

while not(GI.input(shutdown)):
    if t.time()-time1>period/disp:
        light=(light+maxlight/disp)%maxlight
        time1=t.time()


    if t.time()-timeshim>shim:
        state=1
        timeshim=t.time()
    
    if t.time()-timeshim>shim*light:
        state=0
    
    GI.output(led, state)

GI.output(led, 0)