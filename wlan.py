"""Use WiFi on an ESP-32 microcontroller with essid and password stored in NVS."""
from esp32 import NVS
from network import WLAN, STA_IF
from machine import idle

UTF8 = 'utf8'

ns = NVS('WiFi')
buffer = bytearray(16)

len = ns.get_blob('essid', buffer)
essid = buffer[:len].decode(UTF8)
len = ns.get_blob('password', buffer)
password = buffer[:len].decode(UTF8)

wlan = WLAN(STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print(f'connecting to {essid}.')
    wlan.connect(essid, password)
    while not wlan.isconnected():
        idle()

addr = wlan.ifconfig()
print(f'id: {addr[0]}, netmask: {addr[1]}, gw: {addr[3]}, ns: {addr[3]}')
