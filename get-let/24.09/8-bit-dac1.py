import RPi.GPIO as GI







GI.setmode(GI.BCM)
GI.setwarnings(False)

led=[16, 12, 25, 17, 27, 23, 22, 24]


GI.setup(led, GI.OUT)
ranger=3.3



def number_to_dac(v):
    ans=[int(el) for el in bin(v)[2:].zfill(8)]
    for i in range(8):
        GI.output(led[i], ans[i])
    

def Volt(v):
    if not(0.0 <= v <=ranger):
        print("Error", v)
        return 0
    return int(v/ranger*255)


try:
    while 1:
        try:
            volt=float(input("введите напряжение в Вольтах: "))
            num=Volt(volt)
            number_to_dac(num)
        except ValueError:
            print("Неправельно, попробуй ещё раз\n")
    


finally:
    GI.output(led, 0)
    GI.cleanup()