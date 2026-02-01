#
# Demo controlling an analog RGB LED with PWM
#
import time
import board
import adafruit_rgbled
from rainbowio import colorwheel

# Pins for each RGB LED color
RED_LED = board.A1
GREEN_LED = board.A2
BLUE_LED = board.A3

# Define the RGB LED.  As it's common anode we invert the PWM signal
led = adafruit_rgbled.RGBLED(RED_LED,GREEN_LED,BLUE_LED,invert_pwm=True)

# A helper function to do a rainbow color cycle
def rainbow_cycle(wait):
    for i in range(255):
        i = (i + 1) % 256
        led.color = colorwheel(i)
        time.sleep(wait)

# Loop forever thru the basic colors and then the rainbow
while True:
    led.color = (255,0,0)
    time.sleep(0.5)
    led.color = (0,255,0)
    time.sleep(0.5)
    led.color = 0x0000ff
    time.sleep(0.5)

    led.color = 0
    time.sleep(1)

    rainbow_cycle(0.1)

    led.color = 0
    time.sleep(1)
