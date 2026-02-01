#
# Basic NeoPixel demo
#
import board
import time
import neopixel

# Number and pin for the NeoPixels
NUM_LEDS = 10                   # change to reflect your LED strip
NEOPIXEL_PIN = board.NEOPIXEL        # change to reflect your wiring

# Define NeoPixel object.  Second line has some optional arguments.
pixels = neopixel.NeoPixel(NEOPIXEL_PIN, NUM_LEDS, brightness=0.5)
#pixels = neopixel.NeoPixel(NEOPIXEL_PIN, NUM_LEDS, brightness=0.5, auto_write=False, pixel_order='GRB')

# Light up some pixels!  Using a variety of ways to define color.
pixels[0] = 0xff0000
pixels[1] = (0,0,255)
#pixels.show()
time.sleep(2)
pixels.fill((0,255,0))
#pixels.show()
time.sleep(2)
