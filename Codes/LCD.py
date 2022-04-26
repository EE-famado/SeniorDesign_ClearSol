import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

def lcdscreen():
    
    lcd_columns = 16
    lcd_rows = 2
    
    lcd_rs        = digitalio.DigitalInOut(board.D25) # Note this might need to be changed to 21 for older revision Pi's.
    lcd_en        = digitalio.DigitalInOut(board.D24)
    lcd_d4        = digitalio.DigitalInOut(board.D23)
    lcd_d5        = digitalio.DigitalInOut(board.D17)
    lcd_d6        = digitalio.DigitalInOut(board.D18)
    lcd_d7        = digitalio.DigitalInOut(board.D22)
    lcd_backlight =digitalio.DigitalInOut(board.D4)
    
    # Initialize the LCD 
    lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                            lcd_columns, lcd_rows, lcd_backlight)
    return lcd;
    
    
    