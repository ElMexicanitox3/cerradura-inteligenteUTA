import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Keypad = [[1,2,3,"A"],
#           [4,5,6,"B"],
#           [7,8,9,"C"],
#           ["*",0,"#","D"]]

Keypad = [[1,4,7,"*"],
          [2,5,8,"0"],
          [3,6,9,"#"],
          ["A","B","C","D"]]
ROW = [29,31,33,35]
COL = [37,36,38,40]

for i in range(4):
    GPIO.setup(COL[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
for j in range(4):
    GPIO.setup(ROW[j], GPIO.OUT)
    GPIO.output(ROW[j], True)

# def KB():
#     try:
#         while True:
#             for d in range(4):
#                 GPIO.output(ROW[d], False)

#                 for a in range(4):
#                     if GPIO.input(COL[a]) == 0:
#                         Key = Keypad[d][a]

#                         time.sleep(0.2)

#                         return Key
                            
#                 GPIO.output(ROW[d], True)
#                 time.sleep(0.01)
#     except KeyboardInterrupt:
#         GPIO.cleanup()




# def KB():
    # try:
while True:
    for d in range(4):
        GPIO.output(ROW[d], False)

        for a in range(4):
            if GPIO.input(COL[a]) == 0:
                Key = Keypad[d][a]

                time.sleep(0.2)

                print (Key)
                    
        GPIO.output(ROW[d], True)
        time.sleep(0.01)
    # except KeyboardInterrupt:
    #     GPIO.cleanup()