""" Archivo principal del programa"""

import menu
import db

db.crear_db()

def main():
    menu.loop()

if __name__ == "__main__":
    main()
    