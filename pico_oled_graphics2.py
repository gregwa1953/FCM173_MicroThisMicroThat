from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import gfx
from time import sleep
i2c=I2C(0)
oled_width = 128
oled_height = 64

        
oled=SSD1306_I2C(oled_width,oled_height,i2c)
graphics = gfx.GFX(oled_width, oled_height, oled.pixel)

oled.text("MTMT #7",1,1)
oled.show()
sleep(2)
oled.fill(0)
oled.show()



oled.fill(0)
oled.show()
# Line
graphics.line(0, 0, 127, 20, 1)
oled.show()
sleep(2)
oled.fill(0)

# Rectangle
graphics.rect(0, 0, 50, 20, 1)
oled.show()
sleep(2)
oled.fill(0)

# Filled Rectangle
graphics.fill_rect(0, 0, 50, 20, 1)
oled.show()
sleep(2)
oled.fill(0)

# Circle (x0,y0,radius,colour)
graphics.circle(64, 10, 10, 1)
oled.show()
sleep(2)
oled.fill(0)

# Filled Circle
graphics.fill_circle(64, 10, 10, 1)
oled.show()
sleep(2)
oled.fill(0)

# Triangle  (x0, y0, x1, y1, x2, y2, color)
graphics.triangle(0,0,55,20,5,32,1)
oled.show()
sleep(2)
oled.fill(0)
oled.show()

# Filled Triangle
graphics.fill_triangle(0,0,55,20,5,32,1)
oled.show()
sleep(2)
oled.fill(0)
# Clear the display
oled.show()

# oled.fill(0)