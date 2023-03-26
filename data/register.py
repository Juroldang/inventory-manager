from datetime import datetime

class Register():
  
  def __init__(self):
    self._listChanges = []

  @property
  def listChanges(self):
    return self._listChanges
  def setListChanges(self, newList):
    self._listChanges = newList
    
  def date(self):
    dateNow = datetime.now()
    months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    date = " el "+str(dateNow.day) + " de " + months[dateNow.month-1]+ " del "+str(dateNow.year)
    return date
  
  def newChange(self, change):
    finalChange = change + self.date()
    self.listChanges.append(finalChange)