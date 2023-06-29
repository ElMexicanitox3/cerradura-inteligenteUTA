#  _____                     ______           _              
#  |_   _|                    | ___ \         | |             
#    | | ___  __ _ _ __ ___   | |_/ /_ __ ___ | | _____ _ __  
#    | |/ _ \/ _` | '_ ` _ \  | ___ \ '__/ _ \| |/ / _ \ '_ \ 
#    | |  __/ (_| | | | | | | | |_/ / | | (_) |   <  __/ | | |
#    \_/\___|\__,_|_| |_| |_| \____/|_|  \___/|_|\_\___|_| |_|
# 
# Updated By: Gerardo Matadama Peralta
# Created: 26/02/2021
# Las Updated:
# Version: 1.0
#Script to show messages to the employee

import LCD_Driver
LCD = LCD_Driver.lcd()


LCD.lcd_display_string("Cerradura", 2, 6)
LCD.lcd_display_string("Bloqueada", 3, 6)
# LCD.lcd_display_string("Ingrese Token", 1, 3)


# def ShowData(data, row, column):
#     LCD.lcd_display_string(data, row, column)

# def LCDClean():
#     LCD.lcd_clear()

