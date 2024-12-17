def sumar(n1, n2):
    res = n1 + n2
    return res

print("La suma es", sumar(4,9))

def multiplicar(x1, x2):
    res = x1 * x2
    return res

print("La multiplicación es", multiplicar(3,5))

def siguiente(x):
    res = x + 1 
    return res 

def contar_vocales(texto):
    for caracter in texto:
        if(caracter == "o"):
            print(caracter)
        elif(caracter == "e"):
            print(caracter)
        elif(caracter == "i"):
            print(caracter)
        elif(caracter == "a"):
            print(caracter)
        elif(caracter == "u"):
            print(caracter)
    return caracter


print(contar_vocales("Hola Mundo"))