from random import randint
nombre=input("Escribe tu nombre: \n")
print("\n")
print("Tienes 8 intestos")
numero_secreto=randint(1,100)
for intento in range(8):
    if intento==0:
        respuesta=int(input("Introduce el numero que crees que es: \n"))
    else:
        respuesta=int(input("Introduce tu nueva respuesta\n"))
    if respuesta <1 or respuesta> 100:
        print("numero fuera de rango, rango permitido [1,100]")
    else:
        if respuesta<numero_secreto:
            if intento<7:
                print("el numero que ingresaste es menor intenta de nuevo con uno mas grande")
        elif respuesta>numero_secreto:
            if intento<7:
                print("el numero que ingresaste es mas grande, intenta con uno mas pequeño")
        else:
            print(f"Felicidades {nombre} Adivinaste el numero ¡Ganaste!, te tomo {intento+1} intentos")
            break
    if intento==6:
        print("Piensa bien tu respuesta, Ultimo intento")