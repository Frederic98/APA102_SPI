import colorsys
import time
import signal
from apa102_spi import APA102


def sigint(signalNumber, frame):
    global running
    running = False


signal.signal(signal.SIGINT, sigint)

num_leds = 60
led = APA102(3, 0, num_leds)
running = True
while running:
    for i in range(256):
        for j in range(num_leds):
            r,g,b = colorsys.hsv_to_rgb((i / 256 + j / num_leds) % 1, 1, 1)
            led[j] = (r*255, g*255, b*255)
        led.update()
        time.sleep(0.01)
        if not running:
            break

led[:] = 0
led.update()
