import pymysql
from time import sleep
from pymysql.constants import ER

class DB: 

    ErrCodesMysql = {
        ER.BAD_DB_ERROR: "Unknown your database, check Configuration_Script.json file",
        ER.ACCESS_DENIED_ERROR: "Access denied, check access credentials in Configuration_Script.json file"
    }

    Error = []

    def __init__(self, Data = None):

        self.Host = "192.185.131.38"
        self.User = "ecompras_gasouser"
        self.Password = "gasosuruta"
        self.DB = "ecompras_gasosur"
        self.Charset = "utf8mb4"

        # self.__connect__()
        
    def __connect__(self):

        try:
            self.connection = pymysql.connect(host=self.Host, user=self.User, password=self.Password, db=self.DB, charset=self.Charset, cursorclass=pymysql.cursors.DictCursor)
            self.con = self.connection.cursor()
        except pymysql.err.MySQLError as err:
            code, args = err.args

            # print("error")
            # print("\x1b[1;31mERROR CODE: DB001")
            # print(self.ErrCodesMysql.get(code, args))
            msg = "error"
            return msg      

    def __disconnect__(self):
        print("Conexion terminada")

    def __check__(self):
        print("TODO BIEN :b")

    def __commit__(self, sql):
        result = self.con.execute(sql)
        self.connection.commit()
        return result

    def __ConsultTokenUser__(self, StorageId, Token):
        sql = "SELECT * FROM `usuario` WHERE usuario_gasolinera ="+str(StorageId)+" AND usuario_token ="+str(Token)+" AND usuario_status = 1"
        result = self.con.execute(sql)
        if (result == 1):
            data = []
            for result in self.con.fetchall():
                data.append(result)
            return result
        else:
            return False

    def __EntryRegister__(self, usuario, cerradura, hora, fecha):
        sql = "INSERT INTO `cerradura_movimientos` (`cerradura_movimientos_id`, `cerradura_movimientos_idx`, `cerradura_movimientos_usuario_id`, `cerradura_entrada`,  `cerradura_salida`, `cerradura_fecha`) VALUES (NULL, "+str(cerradura)+", "+str(usuario)+", '"+str(hora)+"', '', '"+str(fecha)+"')"
        result = self.con.execute(sql)
        self.connection.commit()
        if (result == 1):
            return True
        else:
            return False

    def __GetRegistro__(self, cerradura):
        idregistro = "SELECT * FROM `cerradura_movimientos` WHERE cerradura_movimientos_idx = "+str(cerradura)+" ORDER BY `cerradura_movimientos`.`cerradura_movimientos_id` DESC limit 1"
        result = self.con.execute(idregistro)
        if (result == 1):
            data = []
            for result in self.con.fetchall():
                data.append(result)
            return result
        else:
            return False
    
    def __UpdateClose__(self, ids, hora):
        sql = "UPDATE `cerradura_movimientos` SET `cerradura_salida` = '"+str(hora)+"'  WHERE `cerradura_movimientos`.`cerradura_movimientos_id` = "+str(ids)+""
        resultdoorupdate = self.con.execute(sql)
        self.connection.commit()
        if (resultdoorupdate == 1):
            return True
        else:
            return False

    def __UpdateStatusDB__(self, IDCerradura, Status):
        doorupdate = "UPDATE `cerradura` SET `cerradura_status` = "+str(Status)+" WHERE `cerradura`.`cerradura_id` = "+str(IDCerradura)+""
        resultdoorupdate = self.con.execute(doorupdate)
        self.connection.commit()
        if (resultdoorupdate == 1):
            return True
        else:
            return False

    def __CheckInfoDoor__(self, IDCerradura):
        checkstatusdoor = "SELECT * FROM `cerradura` WHERE cerradura_id = "+str(IDCerradura)+""
        result = self.con.execute(checkstatusdoor)
        if (result == 1):
            data = []
            for result in self.con.fetchall():
                data.append(result)
            return result
        else:
            return False

