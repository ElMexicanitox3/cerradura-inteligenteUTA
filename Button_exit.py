#  _____                     ______           _              
#  |_   _|                    | ___ \         | |             
#    | | ___  __ _ _ __ ___   | |_/ /_ __ ___ | | _____ _ __  
#    | |/ _ \/ _` | '_ ` _ \  | ___ \ '__/ _ \| |/ / _ \ '_ \ 
#    | |  __/ (_| | | | | | | | |_/ / | | (_) |   <  __/ | | |
#    \_/\___|\__,_|_| |_| |_| \____/|_|  \___/|_|\_\___|_| |_|
# 
# Updated By: Gerardo Matadama Peralta
# Created: 23/05/2021
# Las Updated:
# Version: 1.0
# Script to open the door and mark exit

import RPi.GPIO as GPIO
import time

class button:
    def botton_action(self):
        GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        while True:
            input_state=GPIO.input(23)
            if input_state==False:
                return True;
