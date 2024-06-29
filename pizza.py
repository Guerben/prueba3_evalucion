import json
from datetime import datetime
ruta = 'ventapizza.json'
venta = []
fecha_hora = datetime.now().strftime('%y-%M-%d %H-%M-%S')
precio_pizzas = {
    'Margarita':{'pequeña':5500,'Mediana':8500,'Familia':11000},
    'Mexicana':{'pequeña':7000,'Mediana':10000,'Familia':13000},
    'Barbacoa':{'pequeña':6500,'Mediana':9500,'Familia':12500},
    'Vegetariana':{'pequeña':5000,'Mediana':8000,'Familia':10500}
}


def registrar_venta():

  nombre_cliente = input("Nombre del cliente: ")

  tipo_cliente = input('Tipo de cliente (Estudiante diurno/Estudiante vespertino/Administrativo').lower()
  tipo_pizza = input('Tipo de pizza (Mexicana/Margarita/Barbacoa/vegetariana): ').lower()

  tamaño_pizza = input("Tamaño de la pizza (pequeña/mediana/familia): ").lower()

  cantidad = int(input("Cantidad de pizzas: "))

  if tipo_pizza not in precio_pizzas or tamaño_pizza not in precio_pizzas[tipo_pizza]:

      print("Tipo o tamaño de pizza inválido.")

      return
  
  
  precio_unitario = precio_pizzas[tipo_pizza][tamaño_pizza]

  descuento = 0

  if tipo_cliente == 'Estudiante diurno ':
     descuento = 0.15

  elif tipo_cliente == 'Estudiante vespertino':
     descuento = 0.18

  elif tipo_cliente == 'Administrativo':
     descuento = 0.11

  precio_total = precio_unitario * cantidad
  precio_final = precio_total*(1-descuento)


  ventas = {
  'fecha_hora':fecha_hora,
  'nombre_cliente':nombre_cliente,
  'tipo_cliente':tipo_cliente,
  'tipo_pizza':tipo_pizza,
  'tamaño_pizza':tamaño_pizza,
  'cantidad':cantidad,
  'precio_unitario':precio_unitario,
  'descuento':descuento,
  'precio_total':precio_total,
  'precio_final':precio_final

  }
  venta.append(ventas)
  print('venta registrada con exito!')
  



def mostrar_venta():
   nombre_cliente = input('ingrese el nombre del cliente :')
   ventas_cliente = [ventas for ventas in venta if ventas["nombre_cliente"] == nombre_cliente]
   if not venta :
      print('no hay venta registrada!')
   else :
      print(ventas_cliente)   
  

def buscar_venta():
   nombre_cliente = input('ingrese el nombre del cliente :')
   ventas_cliente = [ventas for ventas in venta if ventas["nombre_cliente"] == nombre_cliente]
   if not venta :
      print('no hay venta registrada!')
   else :
      print(ventas_cliente)
 
      
def guardar_venta():
   with open(ruta,'w') as file:
      json.dump(venta,file)     
      print('venta guardada con exito!')   

def cargar_venta():
   global venta
   try:
      with open(ruta,'r') as file:
         venta = json.load(file)
         print(f'venta cargada desde el archivo {ruta}')

   except FileNotFoundError :
      print(f'no se encontro el archivo {ruta}')     
        
def generar_boleta(ventas):
   for venta in ventas :
      print(venta)
    



def menu():
   while True:
      print("\n--- Sistema de Ventas de Pizzas ---")

      print("1. Registrar una venta")

      print("2. Mostrar todas las ventas")

      print("3. Buscar ventas por cliente")

      print("4. Guardar las ventas en un archivo")

      print("5. Cargar las ventas desde un archivo")

      print("6. Salir")

      opcion = int(input('ingrese una opcion :'))

      return opcion
   

def main():
   while True:
      opcion = menu()
      if opcion == '1':
         registrar_venta()

      elif opcion == '2':
         mostrar_venta()
      elif opcion == '3':
         buscar_venta()
      elif opcion == '4':
         guardar_venta()
      elif opcion == '5':
         cargar_venta()
      elif opcion == '6':
         generar_boleta()
      elif opcion == '7':
         break
          
      elif opcion == '8':
         print('saliendo del programa')
         break
      



if __name__ == "__main__":
   main()
         