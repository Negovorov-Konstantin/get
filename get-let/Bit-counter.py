import RPi.GPIO as GI

import time as t

GI.setmode(GI.BCM)
GI.setwarnings(False)

led=[16, 12, 25, 17, 27, 23, 22, 24]
shutdown=13
period=0.2

up=9
down=10

GI.setup(led, GI.OUT)
GI.setup([up, down], GI.IN)
GI.setup(shutdown, GI.IN)
state=0
time1=t.time()
timeshim=t.time()
num=0


def bi(v):
    return [int(el) for el in bin(v)[2:].zfill(8)]

while not(GI.input(shutdown)):
    if t.time()-time1>period and GI.input(up):
        time1=t.time()
        num=(num+1)%256
    if t.time()-time1>period and GI.input(down):
        num=(num+255)%256
        time1=t.time()
    

    for i in range(8):
        GI.output(led[i], bi(num)[i])
    

GI.output(led, 0)