#
# Blink onboard LED
#
import time
import board
import digitalio

# Setup onboard LED as a digital output
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output()

# Loop forever turning the LED on and off
while True:
    led.value = True #on
    time.sleep(1)
    led.value = False # that bitch shleeep
    time.sleep(1)
