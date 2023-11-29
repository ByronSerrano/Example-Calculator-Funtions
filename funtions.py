# Funtions of Option and Get Option

def postOption():
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4.Dividir\n5. Salir")

def getOption():
    option = int(input("- "))
    return option


# Funtions to obtein the numbers

def showMessageNumbers():
    print("Ingrese un número: ")
    num1 = int(input("- "))
    print("Ingrese otro número: ")
    num2 = int(input("- "))
    resultNum = [num1, num2]
    return resultNum

def getNumbers():
    return showMessageNumbers()[0], showMessageNumbers()[1]

# Matematics Funtions

def getSum(x,y):
    result = x + y
    return result
