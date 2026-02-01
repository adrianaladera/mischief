#
# Demo of some basic animations, using the Bluetooth to cycle thru them.  Use with the Bluefruit Connect app.
#
import board
import time
import neopixel
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.button_packet import ButtonPacket
from adafruit_bluefruit_connect.color_packet import ColorPacket

# Setup NeoPixels
pixels = neopixel.NeoPixel(board.NEOPIXEL,10)
state = 0

# Setup Bluetooth radio
ble = BLERadio()
uart_service = UARTService()
advertisement = ProvideServicesAdvertisement(uart_service)

# Function to check if a button in the Bluetooth Connect app has been pressed and if so set the state appropriately
def check_buttons(st):
    if ble.connected:
        if uart_service.in_waiting:
            packet = Packet.from_stream(uart_service)
            if isinstance(packet, ButtonPacket):
                if packet.pressed:
                    if packet.button == ButtonPacket.RIGHT:
                        st = 0
                        pixels.fill(0)
                        print("right")
                    if packet.button == ButtonPacket.LEFT:
                        st = st +1
                        print("left")
            if isinstance(packet, ColorPacket):
                pixels.fill(packet.color)
                st = 0
    elif not ble.connected:
        st = 0
        pixels.fill(0)
    return(st)

while True:
    # Start Bluetooth LE advertisement.
    ble.name = 'Blinkenlights'
    ble.start_advertising(advertisement)

    # Blink a pixel blue while waiting for a connection.
    while not ble.connected:
        pass
        pixels[0] = 0x000011
        time.sleep(0.1)
        pixels.fill(0x000000)
        time.sleep(0.2)

    # When connected, step thru various animations when left button is pressed.
    # Right button turns pixels off.
    while ble.connected:
        state = check_buttons(state)
        # Each while loop will need to check if a button has been pressed.
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
        # In this more complex case, one while statement covers the initial animation setup,
        # and the second inner while loop does the actual animation.
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
        if state == 7:
            state = 1



	
