''' Librerias
datetime para los métodos de fecha en eliminar_caducados
os.path de sistema operativo para comprobar que exista el fichero
stock_medicamentos antes de llamarlo
'''

from datetime import datetime
from os.path import exists


'''Atributos'''
''' self.datos=[] lista para guardar las lineas del fichero a cargar '''
''' self.contador int para llevar la cuenta de las llamadas recursivas '''

class GestorStock:
    def __init__(self):
        self.datos=[]
        self.contador=0

    ''' cargar_datos() Método que busca el fichero actividad3_stock_medicamentos.csv y lo guarda en una lista de listas'''
    ''' Lee el fichero linea a linea excepto la primera '''
    ''' limpia el fin de linea '\n' '''
    ''' rompe la linea en 4 items y los agrega a una lista de listas'''
    ''' Salida: Bool= True si bien o Error si no puede procesar el fichero '''

    def cargar_datos(self):
        self.datos = []
        if (exists("./actividad3_stock_medicamentos.csv")):
            with open('./actividad3_stock_medicamentos.csv', 'r',encoding='utf-8') as fichero:
                datos=fichero.readlines()[1:]
                for dato in datos:
                    dato = dato.strip('\n')
                    dato = dato.split(";")
                    self.datos.append(dato)
            
            return True
        else:
            raise FileNotFoundError("No se ha encontrado el archivo actividad3_stock_medicamentos.csv")

    ''' Método buscar_recursivo: Busca la linea correspondiente a un id dado de forma recursiva '''
    ''' Input: id a buscar de tipo string'''
    ''' Output: tupla formada por una lista con el medicamento y un int con el número de llamadas recursivas'''
    ''' Llamadas: El método llama al método busca()'''
    ''' Descripción: el método primero carga datos del fichero y luego llama a busca() para buscar recursivamente id'''
    ''' Cuando acaba, devuelve la tupla y deja la lista self.datos vacia y el contador a cero para nuevas búsquedas'''

    def buscar_recursivo(self, id):
        self.cargar_datos()
        retorna=self.busca(id)
        self.datos=[]
        pasos=self.contador
        self.contador=0
        return retorna,pasos


    ''' Método: actualizar_cantidad. dada una cantidad y un id de medicamento, el método carga datos
    y luego cambia el dato de cantidad por el dado en el medicamento referenciado por el id, luego salva los datos a fichero'''
    ''' Input: id,  string con el id'''
    ''' Input: cantidad, string/int con la cantidad a cambiar'''
    ''' Output. Bool True si la cosa va bien, error si no'''

    def actualizar_cantidad(self,id,cantidad):

        self.cargar_datos()
        if isinstance(cantidad, int):
            cantidad=str(cantidad)
        bandera=0
        for medicamento in self.datos:
            if medicamento[0]==id:
                bandera=1
                medicamento[2]=cantidad
                print('Se ha actualizado el stock del medicamento: ',medicamento[1],' con la cantidad:', medicamento[2])
        if bandera==0:
            print('Id de medicamento no encontrado')
        return self.guardar_datos()

    ''' Método: eliminar_caducados. El método carga datos de fichero y compara la fecha actual con la que está en fichero,
    si la fecha actual es posterior a la que figura borra el dato del medicamento (la línea) luego salva el fichero'''
    ''' Input: None'''
    ''' Output: Bool si realiza los cambios, error si no'''
    def eliminar_caducados(self):
        self.cargar_datos()
        fecha_actual=datetime.today()
        for medicamento in self.datos:
            fecha_que_consta=datetime.strptime(medicamento[3], "%Y-%m-%d")
            if fecha_actual>fecha_que_consta:
                self.datos.remove(medicamento)
                print('Se ha elimanado el medicamento caducado: ',medicamento[1],' que tenía fechas de: ',medicamento[3])
        return self.guardar_datos()

    ''' Método: guardar_datos. Guarda los datos de la lista de listas en el mismo fichero de donde se leyeron'''
    ''' Input: None'''
    ''' Output: Bool True si bien. OSError si no puede guardar el fichero'''
    ''' Descripción: Primero abre el fichero en modo escritura y escribe la primera línea'''
    ''' Luego: bucle por cada linea de la lista donde se guardan los datos'''
    ''' Por cada medicamento se construye una cadena de texto que incluye el item de la lista y el separador de texto ';' '''
    ''' Se lleva la cuenta de los items para no escribir el separador tras el último item'''
    ''' Si no hay datos que guardar informa y acaba'''


    def guardar_datos(self):
        if len(self.datos) > 0:
            try:
                ruta = r'./actividad3_stock_medicamentos.csv'
                with open(ruta, 'w+',encoding='utf-8') as fichero:
                    fichero.write('id_medicamento;nombre;cantidad;fecha_caducidad\n')
                    for medicamento in self.datos:
                       cadena=''
                       contador=0
                       longi=len(medicamento)
                       for item in medicamento:
                           if contador<longi-1:
                            cadena=cadena+item+';'
                           else:
                               cadena=cadena+item
                           contador=contador+1
                       fichero.write(cadena)
                       fichero.write('\n')
                
                print('Datos guardados')
                return True
            except OSError:
                return ('Fallo al slavar el fichero')
        else:
            print ('No hay datos que guardar')
            return True

    ''' Método busca(id), método auxiliar para la búsqueda recursiva'''
    ''' Input: id, string con el id a buscar'''
    ''' Output: tupla con una lista con el medicamento y el número de llamadas'''
    ''' Output: String con "Dato no encontrado" si el id no está en el fichero + llamadas'''
    def busca(self, id):
        if len(self.datos) == 0:
            retorna="Dato no encontrado"

            return retorna
        dato=self.datos[0][0]
        if dato==id:
            retorna=self.datos[0]
            return retorna

        else:
            self.contador = self.contador + 1
            self.datos=self.datos[1:]
            return self.busca(id)



