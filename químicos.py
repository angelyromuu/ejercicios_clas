def bucle_infinito():
    while True:
        respuesta = input("EScribe algo:")
        if (respuesta == "Hola"):
            print("Has dicho hola")
        elif(respuesta== "fin"):
            print("Has terminado")
            break
bucle_infinito()