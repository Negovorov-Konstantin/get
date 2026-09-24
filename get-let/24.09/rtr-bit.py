import RPi.GPIO as GI



class R2R:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits=gpio_bits
        self.dynamic_range=dynamic_range
        self.verbose=verbose
        GI.setmode(GI.BCM)
        GI.setup(self.gpio_bits, GI.OUT, initial=0)
    
    def deinit(self):
        GI.output(self.gpio_bits, 0)
        GI.cleanup()

    def set_number(self, n):
        ans=[int(el) for el in bin(n)[2:].zfill(8)]
        for i in range(8):
            GI.output(self.gpio_bits[i], ans[i])

    def set_voltage(self, volt):
        if not(0.0 <= volt <=self.dynamic_range):
            print("Error", volt)
            self.set_number(volt)
            return 0
        self.set_number(int(volt/self.dynamic_range*255))
        return 0
    





try:
    dec=R2R([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
    while 1:
        try:
            volt=float(input("введите напряжение в Вольтах: "))
            dec.set_voltage(volt)
        except ValueError:
            print("Неправельно, попробуй ещё раз\n")
    


finally:
    dec.deinit()