from io import open
import pickle

class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    peliculas = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío")
            return
        for p in self.peliculas:
            print(p)
    def cargar(self):
        fichero=open('catalago.pckl','ab+')
        fichero.seek(0)
        try:
            self.peliculas=pickle.load(fichero)
        except:
            print("fichero sin datos")
        finally:
            fichero.close()
            del(fichero)
            print(f'se han cargado {len(self.peliculas)}')
    def guardar(self):
        fichero=open('catalago.pckl','wb')
        pickle.dump(self.peliculas,fichero)
        del(fichero)


c=Catalogo()
#c.agregar(Pelicula('El padrino',175, 1972))
#c.agregar(Pelicula('El padrino 2',202, 1974))
c.mostrar()