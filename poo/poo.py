from datetime import datetime

class Vehiculo:
    def __init__(self, placa):
        self.placa = placa  

    def tiene_restriccion(self, fecha):
        """"
        """
        
        dia_semana = fecha.weekday()
        
        ultimo_digito = int(self.placa[-1])
        
       
        if dia_semana % 2 == 0:  
            if ultimo_digito in [6, 7, 8, 9, 0]:
                return True  
        else:  
            if ultimo_digito in [1, 2, 3, 4, 5]:
                return True  
        
        
        return False


placa = "ABC123"
vehiculo = Vehiculo(placa)
fecha_actual = datetime.now() 
placa = "ABC678"
vehiculo = Vehiculo(placa)
fecha_actual = datetime.now()  


if vehiculo.tiene_restriccion(fecha_actual):
    print(f"El vehículo con placa {vehiculo.placa} tiene restricción de pico y placa hoy.")
else:
    print(f"El vehículo con placa {vehiculo.placa} no tiene restricción de pico y placa hoy.")



