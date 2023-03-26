from bussinessLogic.controller import Controller
from bussinessLogic.inventory import Inventory
from userInterface.ui import UI
from userInterface.gui import GUI
#from tkinter import ttk
from tkinter import *

def main():
  ui = UI()
  inventory = Inventory(ui)
  window = Tk()
  runApp = GUI (window, inventory)
  window.mainloop()
main() 