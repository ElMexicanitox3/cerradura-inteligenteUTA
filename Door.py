#  _____                     ______           _              
#  |_   _|                    | ___ \         | |             
#    | | ___  __ _ _ __ ___   | |_/ /_ __ ___ | | _____ _ __  
#    | |/ _ \/ _` | '_ ` _ \  | ___ \ '__/ _ \| |/ / _ \ '_ \ 
#    | |  __/ (_| | | | | | | | |_/ / | | (_) |   <  __/ | | |
#    \_/\___|\__,_|_| |_| |_| \____/|_|  \___/|_|\_\___|_| |_|
# 
# Updated By: Gerardo Matadama Peralta
# Created: 21/03/2021
# Las Updated:
# Version: 1.0
# Script to open the door

import RPi.GPIO as GPIO
from datetime import time
from datetime import datetime
import time


# PINDOOR = 32

# GPIO.setwarnings(False)

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(PINDOOR,GPIO.OUT)
# GPIO.output(PINDOOR, True)


# Funcion para abrir y cerrar puerta automatica, y esperar 1 segundo
class doorsetting:

    def AutoOC(self):
        
        PINDOOR = 32
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PINDOOR,GPIO.OUT)
        GPIO.output(PINDOOR, False)
        time.sleep(1)
        GPIO.output(PINDOOR, True)


# def Close():
#     GPIO.output(PINDOOR, True)

# def Open():
#     GPIO.output(PINDOOR, False)

# Open():