import RPi.GPIO as GPIO


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


dynamic_range = 3.18 # В


def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    print(voltage / dynamic_range * 255)
    return int(voltage / dynamic_range * 255)


GPIO.setmode(GPIO.BCM)

leds = [22, 27, 17, 26, 25, 21, 20, 16][::-1]

GPIO.setup(leds, GPIO.OUT)


def number_to_dac(number):
    GPIO.output(leds, dec2bin(number))


GPIO.output(leds, 0)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()