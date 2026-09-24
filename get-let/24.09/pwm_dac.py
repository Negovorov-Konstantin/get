import RPi.GPIO as GI



class R2R:
    def __init__(self, gpio_pin, pwm_frequency,  dynamic_range, verbose = False):
        self.gpio_pin=gpio_pin
        self.dynamic_range=dynamic_range
        self.verbose=verbose
        GI.setmode(GI.BCM)
        GI.setup(self.gpio_pin, GI.OUT, initial=0)
        self.pwm=GI.PWM(self.gpio_pin, 200)
        self.pwm.start(100)
    
    def deinit(self):
        GI.output(self.gpio_pin, 0)
        GI.cleanup()

    def set_number(self, volt):
        
        if not(0.0 <= volt <=self.dynamic_range):
            print("Error", volt)
            self.pwm.ChangeDutyCycle(0)
        else:
            print('заполнение', volt/self.dynamic_range*100)
            self.pwm.ChangeDutyCycle(volt/self.dynamic_range*100)

    


try:
    dec=R2R(12, 500, 3.183, True)
    while 1:
        try:
            volt=float(input("введите напряжение в Вольтах: "))
            dec.set_number(volt)
        except ValueError:
            print("Неправельно, попробуй ещё раз\n")
    


finally:
    dec.deinit()