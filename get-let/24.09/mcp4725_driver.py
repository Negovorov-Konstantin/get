import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose=True):
        self.bus=smbus.SMBus(1)

        self.address=address
        self.wm=0x00
        self.pds=0x00
        self.verbose=verbose
        self.dynamic_range=dynamic_range
    def deinit(self):
        self.bus.close()
    
    def set_number(self, number):
        if not isinstance(number, int):
            print("на цап можно подавать только целые числа")
        elif not(0<=number<=4095):
            print("тумач")
        else:
            first=self.wm | self.pds | number >> 8
            second=number & 0xFF
            self.bus.write_byte_data(0x61, first, second)
            print(f"Число {number}, отправленные по I2C данные:")

    def set_voltage(self, volt):
        if not(0.0 <= volt <=self.dynamic_range):
            print("Error", volt)
            self.set_number(volt)
            return 0
        self.set_number(int(volt/self.dynamic_range*4095))
        return 0



try:
    dec=MCP4725(5)
    while 1:
        try:
            volt=float(input("введите напряжение в Вольтах: "))
            dec.set_voltage(volt)
        except ValueError:
            print("Неправельно, попробуй ещё раз\n")
    


finally:
    dec.deinit()
