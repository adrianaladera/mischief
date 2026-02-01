#
# PWM control an external LED
import time
import board
import pwmio

# LED setup for most CircuitPython boards:
led = pwmio.PWMOut(board.A1, frequency=5000, duty_cycle=0)
# duty cycle is off
# lower frequency makes it look more jittery rather than a smooth pulse

# Loop forever pulsing the LED brightness up and down
while True:
    for i in range(100):
       # PWM LED up and down
        if i < 50:
            led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(0.01)
