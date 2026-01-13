"""
Clase Medicamento para gestión de stock de medicamentos
"""

from datetime import datetime


class Medicamento:
    """
    Representa un medicamento con sus atributos básicos.
    
    Atributos:
        id_medicamento (str): Identificador único del medicamento
        nombre (str): Nombre del medicamento
        cantidad (int): Cantidad en stock (debe ser >= 0)
        fecha_caducidad (str): Fecha en formato YYYY-MM-DD
    """
    
    def __init__(self, id_medicamento, nombre, cantidad, fecha_caducidad):
        """
        Constructor de la clase Medicamento.
        
        Args:
            id_medicamento (str): Identificador único del medicamento
            nombre (str): Nombre del medicamento
            cantidad (int o str): Cantidad en stock
            fecha_caducidad (str): Fecha en formato YYYY-MM-DD
            
        Raises:
            ValueError: Si la cantidad es negativa o la fecha tiene formato incorrecto
        """
        self.id_medicamento = id_medicamento
        self.nombre = nombre
        
        # Validar cantidad (convertir a int si es string)
        if isinstance(cantidad, str):
            cantidad = int(cantidad)
        
        if cantidad < 0:
            raise ValueError(f"La cantidad no puede ser negativa: {cantidad}")
        self.cantidad = cantidad
        
        # Validar formato de fecha
        self._validar_fecha(fecha_caducidad)
        self.fecha_caducidad = fecha_caducidad
    
    def _validar_fecha(self, fecha):
        """
        Valida que la fecha tenga el formato correcto YYYY-MM-DD.
        
        Args:
            fecha (str): Fecha a validar
            
        Raises:
            ValueError: Si la fecha no tiene el formato correcto
        """
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Formato de fecha incorrecto: {fecha}. Debe ser YYYY-MM-DD")
    
    def mostrar_info(self):
        """
        Devuelve la información del medicamento en una sola línea legible.
        
        Returns:
            str: Información del medicamento formateada
        """
        return f"ID: {self.id_medicamento}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Caducidad: {self.fecha_caducidad}"
    
    def __str__(self):
        """
        Representación en string del medicamento.
        
        Returns:
            str: Información del medicamento
        """
        return self.mostrar_info()
    
    def __repr__(self):
        """
        Representación formal del medicamento.
        
        Returns:
            str: Representación formal del objeto
        """
        return f"Medicamento('{self.id_medicamento}', '{self.nombre}', {self.cantidad}, '{self.fecha_caducidad}')"