#Programa que me ayude a ver el interes dentro de una sucesión

#Declarar la funcion

def menu():
    print("-------- Bienvenido a la Calculadora --------")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4.Dividir\n5.Salir")
    option = int(input("¿Qué operacion quiere realizar: \n"))
    return option
  
def option(option):
    return int(option)
    
def num():
    x = int(input("Ingrese un número:\n"))
    y = int(input("\nIgrese otro número diferente al anterior: \n"))
    return x, y

def sumNum(x,y):
    result = x + y
    return result


def loop():
    item=option(menu())
    while item < 5:
        match item:
            case 1:
                result = sumNum(num()[0], num()[1])
                print(result)
            

loop()

# def returnExample():
#     x = 1
#     y = 2
#     return x

# def suma(x, y):
#     result = x + y
#     print(result)

# def draw():
#     print(returnExample())

# draw()

