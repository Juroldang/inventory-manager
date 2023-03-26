from datetime import datetime
from data.register import Register

class Item():
  
  def __init__(self, name, amount, commentary, prize, sales):
    self._name = name
    self._date = datetime.now()
    self._amount = int(amount)
    self._commentary = commentary
    self._prize = float(prize)
    self._register = Register()
    self._register.newChange("Creado")
    self._sales = sales
    self._profits = self._sales * self._prize
    self._status = "Disponible"

  def checkStatus(self):
    self._profits = self._sales * self._prize
    if self._amount == 0:
      self._status = "No disponible"

  @property
  def sales(self):
    return self._sales
  def setSales(self, amount):
    self._sales = self._sales + amount

  @property
  def profits(self):
    return self._profits

  @property
  def register(self):
    return self._register

  @property
  def status(self):
    return self._status

  @property
  def name(self):
    return self._name
  def setName(self, newName):
    self._name = newName
    
  @property
  def amount(self):
    return self._amount
  def setAmount(self, newAmount):
    self._amount=newAmount
    
  @property
  def commentary(self):
    return self._commentary
  def setCommentary(self, newCommentary):
    self._commentary = newCommentary
    
  @property
  def prize(self):
    return self._prize
  def setPrize(self, newPrize):
    self._prize = newPrize