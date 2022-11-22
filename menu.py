""" Menú del programa """

import helpers
import manager
import db
import grafico

def loop():

    while True:

        helpers.clear() # LIMPIA LA TERMINAL

        print("==========================")
        print("   BIENVENIDO AL GESTOR   ")
        print("==========================")
        print("[1] Actualización de datos")
        print("[2] Visualización de datos")
        print("[3] Salir                 ")
        print("==========================")

        option = input("> ")
        
        helpers.clear() # LIMPIA LA TERMINAL

        if option == '1':
            manager.ticker()
            
        elif option == '2':
            loop2()
           
        elif option == '3':
            print("Saliendo...\n")
            break
        else:
            print("Opción incorrecta")

        input("\nPresiona ENTER para continuar...")

def loop2():

    while True:

        helpers.clear() # LIMPIA LA TERMINAL
        
        print("=====================")
        print("[1] Resumen          ")
        print("[2] Gráfico de ticker")
        print("[3] Volver           ")
        print("=====================")

        option = input("> ")
        
        helpers.clear() # LIMPIA LA TERMINAL

        if option == '1':
            db.mostrar_resumen_db()
            
        elif option == '2':

            while True:

                helpers.clear() # LIMPIA LA TERMINAL

                print("===============================================")
                print("          SELECCIONE TIPO DE GRÁFICO           ")
                print("===============================================")
                print("[1] Evolución Lineal de Precios                ")
                print("[2] Gráfico de Velas (Precio Apertura y Cierre)")
                print("[3] Volver                                     ")
                print("===============================================")

                option = input("> ")
            
                helpers.clear() # LIMPIA LA TERMINAL
            
                if option == '1':
                    grafico.graficar_ticker_1()

                elif option == '2':
                    grafico.graficar_ticker_2()

                elif option == '3': 
                    print("Volviendo al menú anterior...\n")
                    break 

                else:
                    print("Opción incorrecta")

                input("\nPresiona ENTER para continuar...")

        elif option == '3':
            print("Volviendo al menú anterior...\n")
            break 
            
        else:
            print("Opción incorrecta")

        input("\nPresiona ENTER para continuar...")

    
        