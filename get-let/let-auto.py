import RPi.GPIO as GI

import time as t

GI.setmode(GI.BCM)
GI.setwarnings(False)

led=23
photo=6
shutdown=10
GI.setup(led, GI.OUT)
GI.setup(photo, GI.IN)
GI.setup(shutdown, GI.IN)
state=0
time=t.time()
period=0.2
while not(GI.input(shutdown)):
    GI.output(led, not(GI.input(photo)))

GI.output(led, 0)