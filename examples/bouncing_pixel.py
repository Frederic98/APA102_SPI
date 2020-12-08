import time
import signal
from apa102_spi import APA102

num_leds = 60
led = APA102(3, 0, num_leds)
running = True
def sigint(signalNumber, frame):
    global running
    running = False


signal.signal(signal.SIGINT, sigint)

direction = 1
position = 0
while running:
    if position + direction >= num_leds or position + direction < 0:
        direction *= -1

    position += direction
    led[:] = 0
    led[position] = 255,0,0
    led.update()
    time.sleep(0.05)

led[:] = 0
led.update()