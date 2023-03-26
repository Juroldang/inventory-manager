from os import system

class UI():
  
  def menu(self):
    system("clear")
    print("¡COMAMIERDABienvenido al inventario de la tienda de Juroldang & Navendano!\n\n1. Añadir un producto nuevo\n2. Registrar una venta\n3. Información de los productos\n4. Eliminar un producto\n5. Eliminar todos los productos\n6. Salir")
    
  def choice(self,options):
    if options == False:
      print("\n¿Qué desea hacer?\n")
    else:
      for i in range(len(options)):
        print(str(i+1),options[i],sep=". ")
      print("\n¿Qué desea hacer?\n")
    
  def warning(self, action):
    print("¿Está seguro que desea",action,"?",sep="")
    
  def itemCreationMenu(self):
    system("clear")
    print("Estás a punto de crear un nuevo elemento para tu inventario, ten en cuenta los siguientes aspectos:\n\n1. El nombre del elemento debe servirte para reconocerlo fácilmente y distinguirlo de los demás elementos.\n\n2.El comentario asociado al elemento es opcional y te servirá para realizar anotaciones y/o consideraciones para el elemento en cuestión\n\n3. Puedes modificar todo lo anterior en cualquier momento.\n")
    
  def message(self, message):
    print(message,"\n")
  
  def importantMessage(self, message):
    system("clear")
    print("-----------------------------------------\n\n",message,"\n\n-----------------------------------------\n")

  def succes(self, action):
    system("clear")
    print("¡",action," exitosamente!.\n",sep="")
    
  def back(self):
    print("Presione cualquier tecla para continuar.\n")

  def invalidChoice(self):
    system("clear")
    print("Opción invalida, intente nuevamente.")