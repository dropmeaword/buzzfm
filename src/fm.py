#!/usr/bin/python
import time
import Adafruit_CharLCD as LCD

lcd_color = (1, 0, 0)
freq_range = (87.5, 108.0)
freq = 104.7
state = 'init'
refresh = False

def display(msg):
	# Button is pressed, change the message and backlight.
	lcd.clear()
	lcd.set_color(lcd_color[0], lcd_color[1], lcd_color[2])
	lcd.message( msg )

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

# create some custom characters
lcd.create_char(1, [2, 3, 2, 2, 14, 30, 12, 0])
lcd.create_char(2, [0, 1, 3, 22, 28, 8, 0, 0])
lcd.create_char(3, [0, 14, 21, 23, 17, 14, 0, 0])
lcd.create_char(4, [31, 17, 10, 4, 10, 17, 31, 0])
lcd.create_char(5, [8, 12, 10, 9, 10, 12, 8, 0])
lcd.create_char(6, [2, 6, 10, 18, 10, 6, 2, 0])
lcd.create_char(7, [31, 17, 21, 21, 21, 21, 17, 31])

display('BuzzFM \ninitializing... \x01')
time.sleep(3.0)

# Make list of button value, text, and backlight color.
buttons = ( (LCD.SELECT, 'Select', (1,1,1)),
            (LCD.LEFT,   'Left'  , (1,0,0)),
            (LCD.UP,     'Up'    , (0,0,1)),
            (LCD.DOWN,   'Down'  , (1,1,0)),
            (LCD.RIGHT,  'Right' , (1,0,1)) )

display("BuzzFM @ {0}\nBroadcasting...".format(freq))

print 'Press Ctrl-C to quit.'
while True:
	if lcd.is_pressed(LCD.RIGHT):
		freq += 1
		refresh = True
	if lcd.is_pressed(LCD.LEFT):
		freq -= 1
		refresh = True
	if lcd.is_pressed(LCD.UP):
		freq += 0.1
		refresh = True
	if lcd.is_pressed(LCD.DOWN):
		freq -= 0.1
		refresh = True

	# make sure frequency value is in range
	if freq > freq_range[1]:
		freq = freq_range[0]

	if freq < freq_range[0]:
		freq = freq_range[1]

	# refresh display
	if refresh:
		display("BuzzFM @ {0}\nBroadcasting...".format(freq))
		refresh = False

	time.sleep(0.1)
