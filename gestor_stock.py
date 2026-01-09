from datetime import datetime
from os.path import exists




class GestorStock:
    def __init__(self):
        self.datos=[]
        self.contador=0

    def cargar_datos(self):
        if (exists("./actividad3_stock_medicamentos.csv")):
            with open('./actividad3_stock_medicamentos.csv', 'r',encoding='utf-8') as fichero:
                datos=fichero.readlines()[1:]
            for dato in datos:
                dato = dato.strip('\n')
                dato = dato.split(";")
                self.datos.append(dato)
            fichero.close()
        else:
            raise TypeError("No se ha encontrado el arcivo actividad3_stock_medicamentos.csv")

    def buscar_recursivo(self, id):
        self.cargar_datos()
        retorna=self.busca(id)
        self.datos=[]
        pasos=self.contador
        self.contador=0
        return retorna,pasos

    def actualizar_cantidad(self,id,cantidad):
        self.cargar_datos()
        for medicamento in self.datos:
            if medicamento[0]==id:
                medicamento[2]=cantidad
        self.guardar_datos()


    def eliminar_caducados(self):
        self.cargar_datos()
        fecha_actual=datetime.today()
        for medicamento in self.datos:
            fecha_que_consta=datetime.strptime(medicamento[3], "%Y-%m-%d")
            if fecha_actual>fecha_que_consta:
                self.datos.remove(medicamento)
        self.guardar_datos()


    def guardar_datos(self):
        self.cargar_datos()
        with open('actividad3_stock_medicamentos.csv', 'w+',encoding='utf-8') as fichero:
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
        fichero.close()


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

