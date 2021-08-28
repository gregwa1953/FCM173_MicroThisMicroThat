# rnerd ssd1306 demo - ESP32

from machine import Pin, I2C   # , TouchPad, Timer
import ssd1306
from time import sleep

# Setup I2C Bus(s)
i2c1 = I2C(0)
# i2c2 = I2C(1)

oled_width = 128
oled_height = 64
# oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c1)

screen1_row1 = "Screen 1, row 1"
screen1_row2 = "Screen 1, row 2"
screen1_row3 = "Screen 1, row 3"

screen2_row1 = "Screen 2, row 1"
screen2_row2 = "Screen 2, row 2"

screen3_row1 = "Screen 3, row 1"

screen1 = [[0, 0 , screen1_row1], [0, 16, screen1_row2], [0, 32, screen1_row3]]
screen2 = [[0, 0 , screen2_row1], [0, 16, screen2_row2]]
screen3 = [[0, 40 , screen3_row1]]

# Scroll in screen horizontally from left to right
def scroll_in_screen(screen):
  for i in range (0, oled_width+1, 4):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)

# Scroll out screen horizontally from left to right
def scroll_out_screen(speed):
  for i in range ((oled_width+1)/speed):
    for j in range (oled_height):
      oled.pixel(i, j, 0)
    oled.scroll(speed,0)
    oled.show()

# Continuous horizontal scroll
def scroll_screen_in_out(screen):
  for i in range (0, (oled_width+1)*2, 1):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)

# Scroll in screen vertically
def scroll_in_screen_v(screen):
  for i in range (0, (oled_height+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
      oled.fill(0)

# Scroll out screen vertically
def scroll_out_screen_v(speed):
  for i in range ((oled_height+1)/speed):
    for j in range (oled_width):
      oled.pixel(j, i, 0)
    oled.scroll(0,speed)
    oled.show()

# Continous vertical scroll
def scroll_screen_in_out_v(screen):
  for i in range (0, (oled_height*2+1), 1):
    for line in screen:
      oled.text(line[2], line[0], -oled_height+i+line[1])
    oled.show()
    if i!= oled_height:
      oled.fill(0)


for cntr in range(3):
            
    # Scroll in, stop, scroll out (horizontal)
    scroll_in_screen(screen1)
    sleep(2)
    scroll_out_screen(4)

    scroll_in_screen(screen2)
    sleep(2)
    scroll_out_screen(4)

    scroll_in_screen(screen3)
    sleep(2)
    scroll_out_screen(4)

    # Continuous horizontal scroll
    scroll_screen_in_out(screen1)
    scroll_screen_in_out(screen2)
    scroll_screen_in_out(screen3)

    # Scroll in, stop, scroll out (vertical)
    scroll_in_screen_v(screen1)
    sleep(2)
    scroll_out_screen_v(4)

    scroll_in_screen_v(screen2)
    sleep(2)
    scroll_out_screen_v(4)

    scroll_in_screen_v(screen3)
    sleep(2)
    scroll_out_screen_v(4)

    # Continuous verticall scroll
    scroll_screen_in_out_v(screen1)
    scroll_screen_in_out_v(screen2)
    scroll_screen_in_out_v(screen3)
    
# Clear the OLED
oled.fill(0)
