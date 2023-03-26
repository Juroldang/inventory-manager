from data.item import Item
from os import system
from data.register import Register
import time

class Inventory():
  def __init__(self, ui):
    self._itemsDict={}
    self._register = Register()
    self._register.newChange("Creado")
    self._ui = ui
    newItem = Item("Caja", 3, "Hola", 15000, 0)
    newItem1 = Item("Ca213", 33, "Hola", 150000, 0)
    newItem2 = Item("Cagserfg", 34, "Hola", 158000, 0)
    self._itemsDict[newItem.name] = newItem
    self._itemsDict[newItem1.name] = newItem1
    self._itemsDict[newItem2.name] = newItem2
  @property
  def itemsDict(self):
    return self._itemsDict

  @property
  def register(self):
    return self._register
    
  def newItem(self):
    self._ui.itemCreationMenu()
    self._ui.message("Nombre del elemento: ")
    name = input()
    while True:
      try:
        self._ui.itemCreationMenu()
        self._ui.message("Cantidad de existencias: ")
        amount = int(input())
        if amount < 0:
          raise
        else:
          break
      except:
        self._ui.invalidChoice()
        time.sleep(2)
        continue
    while True:
      self._ui.itemCreationMenu()
      self._ui.message("¿Desea agregar un comentario?")
      options=["Sí","No"]
      self._ui.choice(options)
      choice = input()
      if choice == "2":
        commentary = "No hay comentarios."
        break
      elif choice == "1":
        self._ui.itemCreationMenu()
        self._ui.message("Escriba el comentario:")
        commentary = input()
        break
      else: 
        system("clear")
        self._ui.message("Opción no valida, intente nuevamente.")
        time.sleep(2)
    while True:
      self._ui.itemCreationMenu()
      self._ui.message("Precio del elemento:")
      try:
        prize = int(input())
        if prize < 0:
          raise
        else:
          break
      except:
        self._ui.invalidChoice()
        time.sleep(2)
        continue
    newItem = Item(name, amount, commentary, prize, 0)
    self._itemsDict[newItem.name] = newItem
    self._register.newChange("Creado")
    self._ui.succes("Elemento creado")

  def delete(self, item):
    del self._itemsDict[item]
    self._register.newChange((item + " eliminado"))
  
  def deleteAll(self):
    self._itemsDict = {}
    self._register.setListChanges([])
    self._ui.importantMessage("¡TODOS LOS DATOS HAN SIDO ELIMINADOS EXITOSAMENTE!")

  def sale(self, item, amount):
    if self._itemsDict[item.name].amount >= amount:
      amountDelta = ((self._itemsDict[item.name].amount)-amount)
      self._itemsDict[item.name].setAmount(amountDelta)
      self._itemsDict[item.name].checkStatus()
      self._ui.succes((item.name+" vendido(s) "))
      (self._itemsDict[item.name]).register.newChange((str(amount)+" vendido(s)"))
      (self._itemsDict[item.name]).setSales(amount)
      (self._itemsDict[item.name]).checkStatus()
      self._register.newChange((str(amount)+item.name+"(s)"+" vendidos(s)."))
      self._ui.message(("Se han vendido "+str(amount)+" de "+item.name+"(s)"+" por un total de "+str(((self._itemsDict[item.name]).prize)*amount)))
      self._ui.back()
      input()
      return True
    else:
      return False

  def showItems(self):
    system("clear")
    if len(self._itemsDict) == 0:
      self._ui.importantMessage("No hay productos registrados.")
      self._ui.back()
      input()
    else:
      sorted_items = dict(sorted(self._itemsDict.items(), key=lambda item:item[1].sales,reverse=True))
      soldestItem = self._itemsDict[list(sorted_items.keys())[0]]
      leastSoldItem = self._itemsDict[list(sorted_items.keys())[len(list(sorted_items.keys()))-1]]
      sorted_items = dict(sorted(self._itemsDict.items(), key=lambda item:item[1].profits,reverse=True))
      mostProfitsItem = self._itemsDict[list(sorted_items.keys())[0]]
      lessProfitsItem = self._itemsDict[list(sorted_items.keys())[len(list(sorted_items.keys()))-1]]
      print("+--------------------+----------+----------+----------+")
      print("| Nombre de Producto |Vendido/s |  Precio  | Ingresos |")
      print("+--------------------+----------+----------+----------+")
      total = 0
      for item in self._itemsDict:
        item = self._itemsDict[item]
        name = item.name
        prize = item.prize
        sales = item.sales
        profits = item.profits
        print("|{:<20}|{:>10.2f}|{:>10.2f}|{:>10.2f}|".format(name, sales, prize, profits))
        print("+--------------------+----------+----------+----------+")
      total += profits
      print("|--------------------|----------|TOTAL:    |{:>10.2f}|".format(total))
      print("+--------------------+----------+----------+----------+")
      print(f"\nProducto más vendido: {soldestItem.name}, con {soldestItem.sales} unidades")
      print(
        f"\nProducto menos vendido: {leastSoldItem.name}, con {leastSoldItem.sales} unidades")
      print(
        f"\nProducto de mayores ingresos: {mostProfitsItem.name}, con {mostProfitsItem.profits} pesos"
      )
      print(
        f"\nProducto de menores ingresos: {lessProfitsItem.name}, con {lessProfitsItem.profits} pesos\n"
      )
      self._ui.back()
      input()