""" Función para ingreso de datos y envío de información a las tablas """

import sqlite3
from datetime import date, timedelta
import db
import api

def ticker():

    ticker = api.validar_ticker()

    fecha_inicio, fecha_fin = api.validar_fechas(ticker)

    if not db.is_ticker_in_db(ticker):

        print(">>> Pidiendo datos...")

        datos = api.request_api(ticker,fecha_inicio,fecha_fin)

        db.tabla_tickers_db(datos)

        db.tabla_resumen_db((ticker, fecha_inicio, fecha_fin))

        print(">>> Datos guardados correctamente")

    else: 

        fecha_inicio_consulta =date.fromisoformat(fecha_inicio)
        fecha_fin_consulta =date.fromisoformat(fecha_fin)

        conexion = sqlite3.connect("tickers.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT fecha_inicio, fecha_fin FROM resumen WHERE ticker= ?", (ticker,))

        data = cursor.fetchall()

        fecha_inicio_db = date.fromisoformat(data[0][0])
        fecha_fin_db = date.fromisoformat(data[0][1])

        conexion.close()

        print(">>> Pidiendo datos...")

        if fecha_inicio_db <= fecha_inicio_consulta <= fecha_fin_db and fecha_fin_consulta > fecha_fin_db:

            fecha_inicio_request = str(fecha_fin_db + timedelta(days=1))
            fecha_fin_request = str(fecha_fin_consulta)

            fecha_nueva_inicio_db = str(fecha_inicio_db)
            fecha_nueva_fin_db = fecha_fin_request

            datos = api.request_api(ticker,fecha_inicio_request,fecha_fin_request)

            db.tabla_tickers_db(datos)

            db.actualizar_resumen_db((fecha_nueva_inicio_db,fecha_nueva_fin_db,ticker))

            print(">>> Datos guardados correctamente")

        elif fecha_inicio_consulta < fecha_inicio_db and fecha_inicio_db <= fecha_fin_consulta <= fecha_fin_db:

            fecha_inicio_request = str(fecha_inicio_consulta)
            fecha_fin_request = str(fecha_inicio_db - timedelta(days=1))

            fecha_nueva_inicio_db = fecha_inicio_request
            fecha_nueva_fin_db = str(fecha_fin_db)

            datos = api.request_api(ticker,fecha_inicio_request,fecha_fin_request)

            db.tabla_tickers_db(datos)

            db.actualizar_resumen_db((fecha_nueva_inicio_db,fecha_nueva_fin_db,ticker))

            print(">>> Datos guardados correctamente")

        elif fecha_inicio_consulta > fecha_fin_db:

            fecha_inicio_request = str(fecha_fin_db + timedelta(days=1))
            fecha_fin_request = str(fecha_fin_consulta)

            fecha_nueva_inicio_db = str(fecha_inicio_db)
            fecha_nueva_fin_db = fecha_fin_request

            datos = api.request_api(ticker,fecha_inicio_request,fecha_fin_request)

            db.tabla_tickers_db(datos)

            db.actualizar_resumen_db((fecha_nueva_inicio_db,fecha_nueva_fin_db,ticker))

            print(">>> Datos guardados correctamente")

        elif fecha_fin_consulta < fecha_inicio_db:

            fecha_inicio_request = str(fecha_inicio_consulta)
            fecha_fin_request = str(fecha_inicio_db - timedelta(days=1))

            fecha_nueva_inicio_db = fecha_inicio_request
            fecha_nueva_fin_db = str(fecha_fin_db)

            datos = api.request_api(ticker,fecha_inicio_request,fecha_fin_request)

            db.tabla_tickers_db(datos)

            db.actualizar_resumen_db((fecha_nueva_inicio_db,fecha_nueva_fin_db,ticker))

            print(">>> Datos guardados correctamente")

        elif fecha_inicio_consulta < fecha_inicio_db and fecha_fin_consulta > fecha_fin_db:

            fecha_inicio_request_1 = str(fecha_inicio_consulta)
            fecha_fin_request_1 = str(fecha_inicio_db - timedelta(days=1))

            fecha_inicio_request_2 = str(fecha_fin_db + timedelta(days=1))
            fecha_fin_request_2 = str(fecha_fin_consulta)

            fecha_nueva_inicio_db = fecha_inicio_request_1
            fecha_nueva_fin_db = fecha_fin_request_2

            datos = api.request_api(ticker,fecha_inicio_request_1,fecha_fin_request_1)

            db.tabla_tickers_db(datos)

            datos = api.request_api(ticker,fecha_inicio_request_2,fecha_fin_request_2)

            db.tabla_tickers_db(datos)

            db.actualizar_resumen_db((fecha_nueva_inicio_db,fecha_nueva_fin_db,ticker))

            print(">>> Datos guardados correctamente")

        elif fecha_inicio_consulta >= fecha_inicio_db and fecha_fin_consulta <= fecha_fin_db:

            print("Datos guardados correctamente")


       

    




    








    
    
    

