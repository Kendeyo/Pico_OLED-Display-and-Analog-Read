from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from oled import Write, GFX, SSD1306_I2C
from oled.fonts import ubuntu_mono_15, ubuntu_mono_20
import utime

pot_Val = machine.ADC(26)

WIDTH = 128
HEIGHT = 64

i2c = I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)

conversion_factor = 3.3/65535
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
while True:
    reading = pot_Val.read_u16()
    data = reading* conversion_factor
    oled.fill(0)
    #write15 = Write(oled, ubuntu_mono_15)
    write20 = Write(oled, ubuntu_mono_20)
    write20.text("Pot Val", 0,0)
    write20.text(str(round(data,1)),0,20)
    oled.show()