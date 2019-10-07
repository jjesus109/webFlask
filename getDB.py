
import pymysql


def getFromDB(peticiones, host = "localhost",user = "admin", password = "1029", db = "dataP"):
    connection  = pymysql.connect(host=host, user=user, password=password,
                                 db=db, cursorclass=pymysql.cursors.DictCursor)
    resultados = []
    try:
        cursor = connection.cursor()
        for peticion in peticiones:
            cursor.execute(peticion)
            resultados.append(cursor.fetchall())
    finally:
        connection.close()
    return resultados
