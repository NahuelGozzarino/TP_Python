""" Creación de la base de datos, tablas y funciones que interactúan con ellas """

import sqlite3

def crear_db():

    conexion = sqlite3.connect("tickers.db")

    cursor = conexion.cursor()

    try:
        cursor.execute("""
            CREATE TABLE tickers(
                nombre VARCHAR (10),
                fecha DATE (15),
                volumen INTEGER (10),
                precio_apertura FLOAT (10),
                precio_cierre FLOAT (10),
                precio_mas_alto FLOAT (10),
                precio_mas_bajo FLOAT (10))""")

        cursor.execute("""
            CREATE TABLE resumen(
                ticker VARCHAR (10) PRIMARY KEY,
                fecha_inicio DATE (10),
                fecha_fin DATE (10))""")

    except sqlite3.OperationalError:
        print("Las tablas de tickers y resumen ya existen.")
    else:
        print("Las tablas de tickers y resumen se han creado correctamente.")

    conexion.close()

def is_ticker_in_db(valor):

    conexion = sqlite3.connect("tickers.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT ticker FROM resumen")

    data = cursor.fetchall()

    tickers = []

    for ticker in data:
        tickers.append(ticker[0])

    conexion.close()

    if valor in tickers:
        return True
    else: return False

def tabla_tickers_db(valores):

    conexion = sqlite3.connect("tickers.db")
    cursor = conexion.cursor()

    cursor.executemany("INSERT INTO tickers VALUES (?,?,?,?,?,?,?)", valores)
    
    conexion.commit()
    conexion.close()

def tabla_resumen_db(valores):

    conexion = sqlite3.connect("tickers.db")
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO resumen VALUES (?,?,?)", valores)

    conexion.commit()
    conexion.close()

def actualizar_resumen_db(valores):

    conexion = sqlite3.connect("tickers.db")
    cursor = conexion.cursor()

    cursor.execute("UPDATE resumen SET fecha_inicio= ?, fecha_fin= ? WHERE ticker= ?", valores)
    
    conexion.commit()
    conexion.close()

def mostrar_resumen_db():

    conexion = sqlite3.connect("tickers.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM resumen")

    tickers = cursor.fetchall()

    print("Los tickers guardados en la base de datos son:")

    for ticker in tickers:
        print(f"{ticker[0]:4} - {ticker[1]} <-> {ticker[2]}")

    conexion.close()




