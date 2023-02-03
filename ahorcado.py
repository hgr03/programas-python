from random import choice
palabras= ["nombre","fuerza","estrella","planeta","rosa","plantas","piedra"]
palabra=choice(palabras)
lista_palabra=list(palabra)
letra=""
item=0
intentos=10
nombre=input("Dame tu nombre: ")
lista_mostrada=["-" for n in range(len(lista_palabra))]
print(f"\n Muy bien {nombre}, empecemos tines {intentos} intentos\n")
for n in range(intentos):
    if n==0:
        letra=input("Introduce tu primer letra: ")
    else:
         letra=input("Intenta con otra letra: ")
    letra=letra.lower()
    if letra in lista_palabra:
            for i in range(lista_palabra.count(letra)):
                item=lista_palabra.index(letra)
                lista_mostrada[item]=letra
                lista_palabra[item]=0
                if item==0:
                     lista_mostrada[item]=letra.capitalize()
                     palabra=palabra.capitalize()
            print(" ".join(lista_mostrada))
            if palabra=="".join(lista_mostrada):
                 print(f"¡Felicidades {nombre}, Ganaste en {n+1} intentos!")
                 break

    else:
         if n<6:
              print("La letra no existe")
         else:
              print("Perdiste mejor suerte para la proxima")  