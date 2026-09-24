import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.3
signal_frequency = 10
sampling_frequency = 1000


try:
    dac = mcp.MCP4725(4.221, verbose=False)
    
    while True:
        dac.set_voltage(amplitude * sg.get_triangle_wave_amplitude(signal_frequency, time.time()))
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()