import RPi.GPIO as GI

import time as t

GI.setmode(GI.BCM)
GI.setwarnings(False)

led=[16, 12, 25, 17, 27, 23, 22, 24]
shutdown=13
period=0.2
on=[0]*8
up=9
down=10

GI.setup(led, GI.OUT)
GI.setup([up, down], GI.IN)
GI.setup(shutdown, GI.IN)
state=0
time1=t.time()
timeshim=t.time()
num=0



while not(GI.input(shutdown)):
    if t.time()-time1>period and not state:
        time1=t.time()
        num+=1
        if num>6:
            state=1
        on=[0]*8
        on[num]=1

    if t.time()-time1>period and state:
        time1=t.time()
        num-=1
        if num<1:
            state=0
        on=[0]*8
        on[num]=1

    

    for i in range(8):
        GI.output(led[i], on[i])
    

GI.output(led, 0)