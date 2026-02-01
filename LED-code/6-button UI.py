#
# Demo of some basic animations, using the CPB's buttons to cycle thru them.
#
import board
import time
import digitalio
import neopixel
from adafruit_debouncer import Debouncer

# Define buttons using the Adafruit Debouncer library
l_pin = digitalio.DigitalInOut(board.D4)
l_pin.switch_to_input(pull=digitalio.Pull.DOWN)
left = Debouncer(l_pin)
r_pin = digitalio.DigitalInOut(board.D5)
r_pin.switch_to_input(pull=digitalio.Pull.DOWN)
right = Debouncer(r_pin)

# Define NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL,10)

# Define starting state
state = 0

# Function to check if a button has been pressed and if so set the state appropriately
def check_buttons(st):
    right.update()
    left.update()
    if right.fell:
        st = 0
        pixels.fill(0)
        print("right")
    if left.fell:
        st = st + 1
        print("left")
    return(st)

# Loop thru a number of different animations based on state, checking for button presses as we go
while True:
    state = check_buttons(state)
    while state == 1:
        pixels.fill(0x110000)
        state = check_buttons(state)
    while state == 2:
        pixels.fill(0x001100)
        state = check_buttons(state)
    while state == 3:
        pixels.fill(0x000011)
        state = check_buttons(state)
    while state == 4:
        pixels.fill(0x001100)
        time.sleep(0.1)
        state = check_buttons(state)
        pixels.fill(0)
        time.sleep(0.1)
        state = check_buttons(state)
    #
    # Note states 5 and 6 have nexted while statements, one to cover initialization and one for the actual animations
    #
    while state == 5:
        offset = 0
        increment = 1
        while state == 5:
            state = check_buttons(state)
            pixels[offset] = 0x110011
            time.sleep(0.1)
            pixels.fill(0x000000)
            offset = (offset + increment) % 10
            if (offset == 0 or offset == 9):
                increment = -increment
    # For this animation, the loop will exit after EITHER a button press or when the
    # time has exipired.
    while state == 6:
        start = time.monotonic()
        while state == 6:
            for i in range(18):
                pixels.fill((i,i,0))
                time.sleep(0.1)
                state = check_buttons(state)
                if (time.monotonic() - start > 10):
                    state = state + 1
                    pixels.fill(0)
                    break
    #
    # The last state goes back to the start.
    if state == 7:
        state = 1



	
