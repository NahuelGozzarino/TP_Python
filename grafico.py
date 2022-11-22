""" Función para graficar """

import db
import api
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc 
import pandas as pd 
import matplotlib.dates as mp_dates 
import sqlite3

def graficar_ticker_1():
    
    ticker = api.input_ticker()

    if db.is_ticker_in_db(ticker):

        conexion = sqlite3.connect('tickers.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tickers WHERE nombre= ? ORDER BY fecha ASC", (ticker,))
        column_names = [row[0] for row in cursor.description]
        df = cursor.fetchall()
        conexion.close()
        data = pd.DataFrame(df,columns = column_names)

        df = pd.DataFrame(data,columns=['fecha','precio_cierre'])

        df['fecha'] = pd.to_datetime(df['fecha']) 

        df['fecha'] = df['fecha'].map(mp_dates.date2num)

        fig, ax = plt.subplots()
        ax.grid(True)

        # Formatting Date

        date_format = mp_dates.DateFormatter('%d-%m-%Y')
        ax.xaxis.set_major_formatter(date_format)
        fig.autofmt_xdate()

        fig.tight_layout()

        ax.set_title("Evolución de Precio de Cierre")
        ax.plot(df['fecha'], df['precio_cierre'])

        plt.show()

    else: print(f"No hay información del ticker {ticker} en la base de datos para graficar.")


def graficar_ticker_2():
    
    ticker = api.input_ticker()

    if db.is_ticker_in_db(ticker):

        conexion = sqlite3.connect('tickers.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tickers WHERE nombre= ? ORDER BY fecha ASC", (ticker,))
        column_names = [row[0] for row in cursor.description]
        df = cursor.fetchall()
        conexion.close()

        data = pd.DataFrame(df,columns = column_names)  

        df = pd.DataFrame(data,columns=['fecha', 'precio_apertura', 'precio_mas_alto', 'precio_mas_bajo', 'precio_cierre'])  

        df['fecha'] = pd.to_datetime(df['fecha']) 

        df['fecha'] = df['fecha'].map(mp_dates.date2num)

        fig, ax = plt.subplots() 

        candlestick_ohlc(ax, df.values, width = 1, colorup = 'green', colordown = 'red', alpha=0.8)

        ax.grid(True)

        # Formatting Date

        date_format = mp_dates.DateFormatter('%d-%m-%Y')
        ax.xaxis.set_major_formatter(date_format)
        fig.autofmt_xdate()

        fig.tight_layout()
        
        ##Titulos

        ax.set_title("Altas y Bajas de Cotización")
        
        ax.set_ylabel("Precio")

        ax.plot()

        plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)

        plt.show()

    else: print(f"No hay información del ticker {ticker} en la base de datos para graficar.")
