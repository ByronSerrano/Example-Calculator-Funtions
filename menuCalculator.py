# Imports
from funtions import *


# Show the message of Welcome
print("------------ Bienvenido a la Calculadora ------------")
print("Seleccione una de las opciones ")


def menu():
    option = getOption()[0]
    while option < 5:
        postOption()
        match getOption()[0]:
            case 1:
                print("Hola uwu")
                break


menu()

# getNumbers()