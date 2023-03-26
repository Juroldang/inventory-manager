import time
from os import system
class Controller():
  def __init__(self, ui, inventory):
    self._ui = ui
    self._inventory = inventory

  def loop(self):
    while True:
      self._ui.menu()
      self._ui.choice(0)
      choice = input()
      if choice in ["1","2","3","4","5","6"]:
        if choice == "1":
          self._inventory.newItem()
          self._ui.back()
          input()
          continue
        elif choice == "2":
          if len(self._inventory.itemsDict) == 0:
            system("clear")
            self._ui.importantMessage("No hay productos registrados.")
            self._ui.back()
            input()
            continue
          else:
            while True:
              system("clear")
              self._ui.importantMessage("VENTA DE ELEMENTOS.")
              self._ui.message("Seleccione el elemento a vender: ")
              self._ui.choice(list(self._inventory.itemsDict.keys()))
              choiceItem = input()
              numItems = len(self._inventory.itemsDict.keys())
              listNumItems=[]
              for num in range(numItems):
                listNumItems.append(str(num+1))
              if choiceItem in listNumItems:
                item = self._inventory.itemsDict[list(self._inventory.itemsDict.keys())[int(choiceItem)-1]]
                self._ui.importantMessage("Venta de "+item.name)
                self._ui.message("Hay "+str(item.amount)+" unidad(es) de "+item.name+" disponibles, ¿cuántas se van a vender?: ")
                amount = int(input())
                self._inventory.sale(item, amount)
                while True:
                  self._ui.importantMessage("Venta de "+item.name)
                  self._ui.message("Hay "+str(item.amount)+" unidad(es) de "+item.name+" disponibles, ¿cuántas se van a vender?: ")
                  try:
                    amount = int(input())
                    if self._inventory.sale(item, amount):
                      self._ui.back()
                      break
                    else:
                      raise
                  except:
                    self._ui.invalidChoice()
                    time.sleep(2)
                    continue
                break
              else:
                self._ui.invalidChoice()
                time.sleep(2)
                continue
            continue
        elif choice == "3":
          self._inventory.showItems()
          self._ui.back()
        elif choice == "4":
          if len(self._inventory.itemsDict) == 0:
            system("clear")
            self._ui.importantMessage("No hay productos registrados.")
            self._ui.back()
            input()
            continue
          else:
            while True:
              system("clear")
              self._ui.importantMessage("Seleccione el elemento a eliminar:")
              self._ui.choice(list(self._inventory.itemsDict.keys()))
              choiceItem = input()
              numItems = len(self._inventory.itemsDict.keys())
              listNumItems=[]
              for num in range(numItems):
                listNumItems.append(str(num+1))
              if choiceItem in listNumItems:
                self._inventory.delete(self._inventory.itemsDict[list(self._inventory.itemsDict.keys())[int(choiceItem)-1]])
                time.sleep(2)
                break
              else:
                self._ui.invalidChoice()
                time.sleep(2)
                continue
            continue
        elif choice == "5":
          system("clear")
          self._ui.importantMessage("ELIMINAR TODOS LOS DATOS.")
          self._ui.warning("eliminar todos los datos")
          self._ui.message("Digite 1 si la respuesta es SÍ o cualquier otra tecla si es NO.")
          choice = input()
          if choice == "1":
            self._inventory.deleteAll()
            self._ui.importantMessage("DATOS ELIMINADOS CORRECTAMENTE.")
            self._ui.back()
            input()
            continue
          else:
            self._ui.importantMessage("ELIMINACIÓN DE DATOS CANCELADA, VOLVIENDO AL MENÚ...")
            time.sleep(2)
            continue
        elif choice == "6":
          self._ui.importantMessage("¡HASTA LA PRÓXIMA!")
          break
      else:
        self._ui.invalidChoice()
        time.sleep(2)
        continue