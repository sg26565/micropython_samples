"""Use a ssd-1306 type OLED display connected to I2C port 0 on an ESP-32 microcontroller."""
from machine import I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0)
display = SSD1306_I2C(128, 64, i2c)
display.contrast(0)

for i in range(0,8):
    display.text(f'{i}: Hello, World',0, i*8)

# display.rect(0,0,128,64,1)
# display.line(0,0,127,63,1)
# display.line(0,63,127,0,1)
display.show()
