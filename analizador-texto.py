#programa que analiza un texto, del cual determina lo siguiente
#numero de veces que se repite una letra
#numero de letras que existe en el texto
#muestra el texto con las palabras invertidas 
#primera letra del texto
#ultima letra del texto
texto=input("introduce el texto a analizar:\n")
letra1=input("ingresa una letra:\n")
letra2=input("ingresa otra letra:\n")
letra3=input("ingresa la ultima letra:\n")
texto_minuscula=texto.lower()

def buscar_letra(texto,letra):#funcion que cuenta la cantidad que una letra se repite
    try:
        return texto.count(letra)
    except:
        print("no hay texto para analizar")
def contar_palabras(texto):#funcion que determina la cantidad de palabras en un texto
    try:
        lista_texto=texto.split()
        print(f'la cantidad de palabras en el texto es {len(lista_texto)}')
    except:
        print("no hay texto para analizar")


print(f'la cantidad de veces que aparece la letra {letra1} en el texto es: {buscar_letra(texto_minuscula,letra1)}')
print(f'la cantidad de veces que aparece la letra {letra2} en el texto es: {buscar_letra(texto_minuscula,letra2)}')
print(f'la cantidad de veces que aparece la letra {letra3} en el texto es: {buscar_letra(texto_minuscula,letra3)}')
contar_palabras(texto_minuscula)

print("Texto invertido")
texto_lista=texto.split()
texto_lista.reverse()
texto_invertido=" "
print(texto_invertido.join(texto_lista))

print(f"Primera letra: {texto[0]}")
print(f"ultima letra: {texto[-1]}")
print("Buscando la frase python en el texto: ")
if "python" in texto:
    print("Existe")
else:
    print("no existe")
