#
# Demo of FancyLED
#
import board
import neopixel
import time
import adafruit_fancyled.adafruit_fancyled as fancy

# Update to match the pin connected to your NeoPixels
pixel_pin = board.NEOPIXEL
# Update to match the number of NeoPixels you have connected
pixel_num = 10

# Define NeoPixels
pixels = neopixel.NeoPixel(pixel_pin, pixel_num)

# Show how to define a color in RGB and HSV models
color = fancy.CRGB(1.0, 0.48, 0.0)  # Orange
pixels.fill(color.pack())
print(color.pack())
time.sleep(2)
pixels.fill(0x000000)
time.sleep(0.5)
color = fancy.CHSV(0.08, 1.0, 1.0)  # Orange
pixels.fill(color.pack())
print(color.pack())
time.sleep(2)

# Show how to define and use a pallette
# This example gives a spinning effect thru the palette colors
# Included are a couple of different gamma correction options
palette = [fancy.CRGB(1.0,0,1.0),   # Purple
            fancy.CHSV(0.28),       # Green
            0x000045                # Blue
            ]
offset = 0
levels = (0.25, 0.3, 0.3)
while True:
    for i in range(10):
        color = fancy.palette_lookup(palette, offset + i/10)
#        color = fancy.gamma_adjust(color, brightness=levels)
#        color = fancy.gamma_adjust(color)
        pixels[i] = color.pack()
    offset = offset + 0.03



