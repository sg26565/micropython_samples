"""Use a relais module connected to pin 5 on an ESP-32 microcontroller."""
from machine import Pin, lightsleep

p = Pin(5, Pin.OUT, value=1)

while True:
    p.value(0)
    lightsleep(1000)
    p.value(1)
    lightsleep(1000)