import DB_Connection
from datetime import time
from datetime import datetime, timedelta
import time
conx = DB_Connection.DB()
# class_instance = DB()
idcerradura = "1"
status = "9"
check = conx.__connect__()
# aver = conx.__UpdateStatusDB__(idcerradura, status)
CerraduraInfo = conx.__CheckInfoDoor__(idcerradura)
now = datetime.now()
Time = now.strftime('%H:%M:%S')
strabierto = str(CerraduraInfo['cerradura_hora_abierto'])
strcerrado = str(CerraduraInfo['cerradura_hora_cerrado'])

Time = "05:00:00"
print("Tiempo Ahorita: "+Time)
print("Horario Abierto: "+strabierto)
print("Horario Cerrado: "+strcerrado) 
print("\n")

(h, m, s) = Time.split(':')
resultnow = int(h) * 3600 + int(m) * 60 + int(s)

(h, m, s) = strabierto.split(':')
resultabierto = int(h) * 3600 + int(m) * 60 + int(s)

(h, m, s) = strcerrado.split(':')
resultcerrado = int(h) * 3600 + int(m) * 60 + int(s)

if(resultnow >= resultabierto and resultnow <= resultcerrado):
    print("Abierto")
elif(resultnow >= resultcerrado or resultnow <= resultabierto):
    print("Cerrado")