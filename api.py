""" Funciones que piden datos a la API """

import requests
from datetime import date, datetime, timedelta
import re

def input_ticker():

    ticker= input(">>> Ingrese el ticker:\n ").upper()

    return ticker


def validar_ticker():

    while True:

        ticker= input_ticker()
    
        validacion = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey=_i0PIv435ie2k6p6Oc6rT162DokO4cO6")
        
        val_data = validacion.json()
        
        if val_data.get('queryCount') > 0:

            print("Ticker válido")
            break

        print("El ticker ingresado no existe. Intente otra vez")

    return ticker

def validar_fechas(ticker):

    while True:

        while True:

            try:
                fecha_inicio = input(">>> Ingrese fecha de inicio (formato YYYY-MM-DD):\n")

                if re.match("[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha_inicio) and len(fecha_inicio) == 10:

                    fecha_inicio_datetime = datetime.strptime(fecha_inicio, "%Y-%m-%d")

                    primer_cotizacion = requests.get(f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey=_i0PIv435ie2k6p6Oc6rT162DokO4cO6')
                    primer_cotizacion_json = primer_cotizacion.json()
                    fecha_primera_cotizacion = primer_cotizacion_json.get('results').get('list_date')
                    date_prim_cot = datetime.strptime(fecha_primera_cotizacion, "%Y-%m-%d")
                    fecha_actual = datetime.now()

                    if fecha_inicio_datetime < date_prim_cot:
                    
                        print(f'La primera fecha de cotización para el ticker {ticker} fue el {datetime.date(date_prim_cot)}. No podrá visualizar nada antes de esta fecha!')
                        continue

                    if fecha_inicio_datetime <= (fecha_actual - timedelta(days=730)):

                        print(f'La fecha de inicio no pueder ser mayor a dos años de la fecha actual: {datetime.date(fecha_actual)}.')
                        continue

                    break
                print("Formato de fecha incorrecto")

            except ValueError: 
                print("Formato de fecha incorrecto")


        while True:

            try:

                fecha_fin = input(">>> Ingrese fecha de fin (formato YYYY-MM-DD):\n")

                if re.match("[0-9]{4}-[0-9]{2}-[0-9]{2}", fecha_fin) and len(fecha_fin) == 10:
                
                    fecha_fin_datetime = datetime.strptime(fecha_fin, "%Y-%m-%d")

                    ultima_cotizacion = requests.get(f'https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey=_i0PIv435ie2k6p6Oc6rT162DokO4cO6').json()
                    date_ult_cot = datetime.fromtimestamp(ultima_cotizacion["results"][0]["t"]/1000)

                    if fecha_fin_datetime > date_ult_cot:

                        print(f'La ultima fecha de cotizacion para el ticker {ticker} fue el {datetime.date(date_ult_cot)}. No podras visualizar nada despues de esta fecha!')
                        continue

                    break
                print("Formato de fecha incorrecto")

            except ValueError:
                print("Formato de fecha incorrecto")

        if fecha_fin_datetime >= fecha_inicio_datetime:

            break
        print("La fecha de inicio no puede ser más reciente que la fecha de finalización. Intente de nuevo")    

    return fecha_inicio, fecha_fin

def request_api(ticker,fecha_inicio,fecha_fin):

    res = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{fecha_inicio}/{fecha_fin}?adjusted=true&sort=asc&limit=50000&apiKey=_i0PIv435ie2k6p6Oc6rT162DokO4cO6")
    
    data = res.json()
    
    datos_a_cargar = []

    for i in data["results"]:
        datos = (ticker, date.fromtimestamp(i["t"]/1000), i["v"], i["o"], i["c"], i["h"], i["l"])
        datos_a_cargar.append(datos)
    
    return datos_a_cargar

