#Pedir al usuario por el número de la tabla
print("Dime el número de la tabla de multiplicar")
num_tabla = int(input())
indice = 1
while(indice < 11):
    resultado = num_tabla * indice
    print(indice, " x ", num_tabla, " = ", resultado)
    indice = indice + 1
print("FIN")