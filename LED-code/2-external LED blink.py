#
# Blink an external LED
#
import time
import board
import digitalio

# Setup a GPIO pin as a digital output
led = digitalio.DigitalInOut(board.A1)
led.switch_to_output()

# Loop forever turning the LED on and off
while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
