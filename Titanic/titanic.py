# Importamos las librerías necesarias
from os import getcwd
from pathlib import Path
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree

# Configuramos la ruta de acceso a los datos y leemos el archivo CSV en un DataFrame de Pandas
path = Path(str(getcwd())+'/DB')
df_titanic = pd.read_csv(Path(str(path)+'/DataSet_Titanic.csv'))

# Separamos las variables explicativas de la variable objetivo
variables = df_titanic.drop('Sobreviviente', axis=1)
salida = df_titanic.Sobreviviente

# Entrenamos el modelo de árbol de decisión con las variables explicativas y la variable objetivo
arbol = DecisionTreeClassifier(max_depth=4,random_state=50)
arbol.fit(variables, salida)

# Realizamos la predicción sobre el conjunto de datos de entrenamiento y calculamos el porcentaje de acierto
prediccion1 = arbol.predict(variables)
porcentaje = accuracy_score(prediccion1, salida)

# Calculamos la matriz de confusión y visualizamos la evaluación del modelo a través de gráficos
cm = confusion_matrix(salida, prediccion1)

def ver_graficas(arbol, cm, variables):
    # Visualizamos la matriz de confusión
    display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=arbol.classes_)
    display.plot()

    # Visualizamos el árbol de decisión
    plt.figure(figsize=(10,8))
    tree.plot_tree(arbol, filled=True, feature_names=variables.columns)

    # Visualizamos la importancia de cada variable en el modelo
    df = pd.DataFrame(dict(importancia=arbol.feature_importances_, columnas=variables.columns))
    grafica = px.bar(df, x='columnas', y='importancia')
    grafica.show()
    plt.title('Relevancia de cada atributo')
    plt.show()

# Función para mostrar si un pasajero dado sobrevivirá o no, dado su información personal
def mostrar_sobrevive(arbol, clase, genero, edad, hermesp, padhij, porcentaje):
    columnas = ['Clase', 'Genero', 'Edad', 'HermEsp', 'PadHij']
    datos = [[clase, genero, edad, hermesp, padhij]]
    b = pd.DataFrame(datos, columns=columnas)
    prediccion2 = arbol.predict(b)
    if prediccion2[0] == 1:
        print(f"Tienes un {round(porcentaje*100,2)}% de sobrevivir")
    else:
        print(f"Tienes un {round(porcentaje*100,2)}% de no sobrevivir")

# Función para pedir información personal de un pasajero y mostrar si sobrevivirá o no
def datos_usuario(arbol,porcentaje):
    clase=int(input("dame el numero de clase en el que viajaras [1,2,3]: "))
    genero=int(input("dame el numero correspondiente a tu genero 0: hombre 1: mujer: "))
    edad=int(input("dame el numero correspondiente a tu edad: "))
    hermesp=int(input("introduce 1 si tienes hermanos especiales y 0 si no: "))
    padhij=int(input("introduce 1 si eres padre o madre y 0 si no: "))
    mostrar_sobrevive(arbol,clase,genero,edad,hermesp,padhij,porcentaje)

repetir='ai'
print("Bienvenido - verifcaremos si sobrevives en el Titanic")
print('Empecemos\n')
while(repetir!='no'):
    datos_usuario(arbol,porcentaje)
    repetir=input("Deseas calcular alguno otro pasajero si/no: ")
    repetir=repetir.lower()