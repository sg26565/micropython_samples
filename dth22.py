from dht import DHT22
from machine import Pin, lightsleep

d = DHT22(Pin(21, Pin.IN, Pin.PULL_UP))

while True:
    d.measure()
    print(f'Humidity: {d.humidity()} %\tTemperature: {d.temperature()} °C')
    lightsleep(1000)