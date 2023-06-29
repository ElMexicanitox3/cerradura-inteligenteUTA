#!/usr/bin/python3

# Main script Where the main functions are saved electronic lock :v

import LCD_Driver
import Door
import Keyboard
import Button_exit
import DB_Connection
import multiprocessing 
import os
import psutil

import RPi.GPIO as GPIO
import time


from datetime import time
from datetime import datetime
import time

#ID DE GASOLINERA
IDGas = 1
IDCerradura = 1

LCD = LCD_Driver.lcd()


#Funcion para mostrar mensajes de bienvenida.
def Welcome():

    #Mientras este activo mostrara mensajes
    while True:

        #variables de informacion del dia y el tiempo
        today = datetime.today()
        now = datetime.now()

        #Formatos de fecha y hora
        Date = now.strftime('%d %b %Y')
        Time = now.strftime('%H:%M:%S')
        
        #imprimir en el LCD
        LCD.lcd_display_string("Gasosur Almacen", 1, 3)
        LCD.lcd_display_string(Date, 2, 4)
        LCD.lcd_display_string(Time, 3, 5)
        
        #esperar 1 segundo
        time.sleep(1)

pid=os.getpid()

P1 = multiprocessing.Process(target=Welcome)
P1.start()
Ps1 = psutil.Process(P1.pid)


#funcion para el teclado.

def KeyboardInput():

    print("Keyboard Active")

    PassCaptured = ""
    LoopNumber = 0
    while True:

        Key = Keyboard.KB()

        if(Key == "A"):
            
            PassCaptured = ""

            conx = DB_Connection.DB()
            check = conx.__connect__()
            if (check == "error"):
                Ps1.suspend()
                time.sleep(1)
                LCD.lcd_clear()
                LCD.lcd_display_string("Error Servidor", 1, 3)
                LCD.lcd_display_string("Sin Conexion", 3, 3)
                LCD.lcd_display_string("A Internet", 4, 4)
                time.sleep(3)
                LCD.lcd_clear()
                Ps1.resume()

            else:
                CerraduraInfo = conx.__CheckInfoDoor__(IDCerradura)
                now = datetime.now()
                Time = now.strftime('%H:%M:%S')
                strabierto = str(CerraduraInfo['cerradura_hora_abierto'])
                strcerrado = str(CerraduraInfo['cerradura_hora_cerrado'])
                statuscerradura = CerraduraInfo['cerradura_status']

                if (statuscerradura == 0):
                    Ps1.suspend()
                    LCD.lcd_clear()
                    time.sleep(1)
                    LCD.lcd_display_string("Cerradura", 2, 6)
                    LCD.lcd_display_string("Bloqueada", 3, 6)
                    time.sleep(3)
                    LCD.lcd_clear()
                    Ps1.resume()
                else:
                    Ps1.suspend()
                    LCD.lcd_clear()
                    time.sleep(1)
                    LCD.lcd_display_string("Ingrese Token", 1, 3)
                    LCD.lcd_display_string("B = Salir", 3, 0)
                    LCD.lcd_display_string("C = Borrar", 4, 0)


                    while True:

                        KeySave = Keyboard.KB()

                        if (KeySave == "*"):
                            ReststartLCD()
                            LoopNumber = 0
                            PassCaptured = ""
                            break
                        
                        if (KeySave != "A" or KeySave != "D"):

                            if (type(KeySave) == int or KeySave == "0"):
                                
                                LoopNumber = LoopNumber + 1

                                PassCaptured = PassCaptured + str(KeySave)

                                print(PassCaptured)
                                
                                if (LoopNumber == 1):
                                    LCD.lcd_display_string("*", 2, 10)

                                elif (LoopNumber == 2):
                                    LCD.lcd_display_string("* *", 2, 9)

                                elif (LoopNumber == 3):
                                    LCD.lcd_display_string("* * *", 2, 8)

                                elif (LoopNumber == 4):
                                    LCD.lcd_display_string("* * * *", 2, 7)
                                    check = conx.__connect__()
                                    DataUser = conx.__ConsultTokenUser__(IDGas, PassCaptured)
                                    time.sleep(1)

                                    if not DataUser:
                                        PassCaptured = ""
                                        LoopNumber = 0
                                        LCD.lcd_clear()
                                        time.sleep(1)
                                        LCD.lcd_display_string("Error", 1, 8)
                                        LCD.lcd_display_string("Usuario No", 2, 5)
                                        LCD.lcd_display_string("Encontrado", 3, 5)
                                        time.sleep(3)
                                        LCD.lcd_clear()
                                        time.sleep(1)
                                        Ps1.resume()
                                        break

                                    else:
                                        today = datetime.today()
                                        now = datetime.now()
                                        Date = now.strftime('%d/%m/%Y')
                                        Time = now.strftime('%H:%M:%S')
                                        user = DataUser['usuario_id']
                                        check = conx.__connect__()
                                        inserregister = conx.__EntryRegister__(user, IDCerradura, Time, Date)
                                        PassCaptured = ""
                                        LoopNumber = 0
                                        LCD.lcd_clear()
                                        time.sleep(1)
                                        LCD.lcd_display_string("Bienvenido", 1, 0)
                                        LCD.lcd_display_string(DataUser['usuario_nombre'], 3, 0)
                                        OCDoor = Door.doorsetting()
                                        OCDoor.AutoOC()
                                        time.sleep(3)
                                        LCD.lcd_clear()
                                        time.sleep(1)
                                        Ps1.resume()
                                        break
                                    
                            elif(KeySave == "C"):
                                PassCaptured = ""
                                LoopNumber = 0
                                LCD.lcd_clear()
                                time.sleep(1)
                                LCD.lcd_display_string("Ingrese Token", 1, 3)
                                LCD.lcd_display_string("B = Salir", 3, 0)
                                LCD.lcd_display_string("C = Borrar", 4, 0)

                            elif(KeySave == "B"):
                                PassCaptured = ""
                                LoopNumber = 0
                                LCD.lcd_clear()
                                time.sleep(1)
                                Ps1.resume()
                                break
        elif (Key == "*"):
            ReststartLCD()
            LoopNumber = 0
            PassCaptured = ""

        
        time.sleep(0.2)


#Funcion para cambiar el status en la BD cada 3 min
def AutoClose():
    while True:
        conxs = DB_Connection.DB()
        checks = conxs.__connect__()
        if (checks != "error"):
            conxs = DB_Connection.DB()
            check = conxs.__connect__()
            o = conxs.__CheckInfoDoor__(IDCerradura)
            n = datetime.now()
            t = n.strftime('%H:%M:%S')
            sta = str(o['cerradura_hora_abierto'])
            stc = str(o['cerradura_hora_cerrado'])
            stcst = o['cerradura_status']
            snl = o['cerradura_signal']

            (h, m, s) = t.split(':')
            resultnow = int(h) * 3600 + int(m) * 60 + int(s)

            (h, m, s) = sta.split(':')
            resultabierto = int(h) * 3600 + int(m) * 60 + int(s)

            (h, m, s) = stc.split(':')
            resultcerrado = int(h) * 3600 + int(m) * 60 + int(s)


            #condicional para abrir cerradura por horario
            if((stcst == 0 and snl == 0) and (resultnow >= resultabierto and resultnow <= resultcerrado)):
                print("Abriendo Cerradura Por Horario de apertura")
                check = conxs.__connect__()
                update = conxs.__UpdateStatusDB__(IDCerradura, 1)
                time.sleep(5)
                
            #condicional para ver si mandaron señal de abrir en horario de cuando este cerrado
            elif((stcst == 1 and snl == 1) and (resultnow >= resultcerrado or resultnow <= resultabierto)):
                sql = "UPDATE `cerradura` SET `cerradura_status` = '1', `cerradura_signal` = '0' WHERE `cerradura`.`cerradura_id` = "+str(IDCerradura)+""
                check = conxs.__connect__()
                update = conxs.__commit__(sql)
                print("5 min para volver a bloquear")
                time.sleep(300)

            #condicional de cierre automatico por horario
            elif((stcst == 1) and (resultnow >= resultcerrado or resultnow <= resultabierto)):
                print("bloqueando cerradura por horario de cierre")
                check = conxs.__connect__()
                update = conxs.__UpdateStatusDB__(IDCerradura, 0)
                time.sleep(5)
        

    time.sleep(10)

P3 = multiprocessing.Process(target=AutoClose)
P3.start()

def boton():
    #funcion para marcar salida cuando oprimes el boton
    # GPIO.setmode(GPIO.BCM)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    while True:
        # print("esperando boton")
        conxs = DB_Connection.DB()
        checks = conxs.__connect__()
        input_state=GPIO.input(16)
        if input_state==False:
            print("boton")
            OCDoor = Door.doorsetting()
            OCDoor.AutoOC()
            if (checks != "error"):
                conxs = DB_Connection.DB()
                check = conxs.__connect__()
                o = conxs.__GetRegistro__(IDCerradura)
                if (o["cerradura_salida"] == ""):
                    conxs = DB_Connection.DB()
                    check = conxs.__connect__()
                    today = datetime.today()
                    now = datetime.now()
                    Time = now.strftime('%H:%M:%S')
                    ids = o["cerradura_movimientos_id"]
                    up = conxs.__UpdateClose__(ids, Time)
                print(o)
        time.sleep(0.5)


P4 = multiprocessing.Process(target=boton)
P4.start()


def ReststartLCD():
    #funcion para reiniciar el LCD
    Ps1.suspend()
    LCD.lcd_clear()
    PassCaptured = ""
    time.sleep(2)
    Ps1.resume()

P2 = multiprocessing.Process(target=KeyboardInput)
P2.start()
Ps2 = psutil.Process(P2.pid)
    