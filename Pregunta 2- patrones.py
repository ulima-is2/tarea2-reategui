import sys

class Entrada: //SINGLETON
    def __init__(self, pelicula_id, funcion, cantidad, cine):
        self.pelicula_id = pelicula_id
        self.funcion = funcion
        self.cantidad = cantidad
	self.cine = cine

class Pelicula:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class Funcion:  // FACHADA
 
    def __init__( self, id, hora, cine)
	seld.id = id
	self.hora = hora
	self.cine = cine

	def pelicula_funcion_cine(self, pelicula_id, funcion_id, cine_id)
		return self.lista_funcion[int(pelicula_id)].funciones

class CinePlaneta:
    def __init__(self):
   

        self.lista_peliculas = [pelicula_id, funicon_id]
        self.entradas = []


    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)


class CineStark:
    def __init__(self):
        

        self.lista_peliculas = [pelicula_id, funcion_id]
        self.entradas = []




    def guardar_entrada(self, id_pelicula_elegida, funcion_elegida, cantidad):
        self.entradas.append(Entrada(id_pelicula_elegida, funcion_elegida, cantidad))
        return len(self.entradas)	

class Cine:  //FACTORY
    def __init__(self, id, nombre):
	self.id = id
	self.nombre = nombre

	cine_id[0]=null


	   def obtener_cine(self, cine_ID):
               if cine_id == '1':
           	 nombre = "CinePlaneta"
		 return nombre()
               elif cine_id == '2':
            	 nombre = "CineStark"
		 return nombre()


        
        
        def listar_peliculas(self, id):
            return self.lista_peliculas[int(cine_id)].peliculas

        def listar_funciones(self, pelicula_id, hora, cine):
            return self.lista_peliculas[int(cine_id)].funciones      

        def guardar_entrada(self, Entrada):
            return self.listar_entradas(entrada.pelicula_id, entrada.funcion_id)




def main():
    terminado = False;
    while not terminado:
        print('Ingrese la opción que desea realizar')
        print('(1) Listar cines')
        print('(2) Listar cartelera')
        print('(3) Comprar entrada')
        print('(0) Salir')
        opcion = input('Opción: ')

        if opcion == '1':
            print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')

        elif opcion == '2':
            print('********************')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')

            cine = input('Primero elija un cine:')
            if cine == '1':
                # CinePlaneta
                cine = CinePlaneta()
            elif cine == '2':
                cine = CineStark()

            peliculas = cine.listar_peliculas()
            print('********************')
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            print('********************')

        elif opcion == '3':
            print('********************')
            print('COMPRAR ENTRADA')
            print('Lista de cines')
            print('1: CinePlaneta')
            print('2: CineStark')
            print('********************')
            cine = input('Primero elija un cine:')
            if cine == '1':
                # CinePlaneta
                cine = CinePlaneta()
            elif cine == '2':
                cine = CineStark()

            peliculas = cine.listar_peliculas()
            for pelicula in peliculas:
                print("{}. {}".format(pelicula.id, pelicula.nombre))
            pelicula_elegida = input('Elija pelicula:')
            #pelicula = obtener_pelicula(id_pelicula)
            print('Ahora elija la función (debe ingresar el formato hh:mm): ')
            for funcion in cine.listar_funciones(pelicula_elegida):
                print('Función: {}'.format(funcion))
            funcion_elegida = input('Funcion:')
            cantidad_entradas = input('Ingrese cantidad de entradas: ')
            codigo_entrada = cine.guardar_entrada(pelicula_elegida, funcion_elegida, cantidad_entradas)
            print('Se realizó la compra de la entrada. Código es {}'.format(codigo_entrada))
        elif opcion == '0':
            terminado = True
        else:
            print(opcion)



if __name__ == '__main__':
    main()