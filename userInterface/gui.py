from tkinter import ttk
from tkinter import *
class GUI:
    def __init__(self,window, inventory):
        self._window = window
        self._inventory = inventory
        self._window.title("Adminventory Juroldang & Navendano")
        frame = LabelFrame(self._window, text = "Registrar un nuevo Producto")
        frame.grid(row=0, column=0, columnspan=4, pady=20)
        Label(frame, text="Ingrese el nombre:").grid(row=1,column=0)
        self._name = Entry(frame)
        self._name.grid(row=1,column=1)
        Label(frame, text="Ingrese el precio:").grid(row=2,column=0)
        self._price = Entry(frame)
        self._price.grid(row=2, column=1)
        self.message = Label(text="", fg="red")
        self.message.grid(row=3, column=0, columnspan=4, sticky=W+E)

        ttk.Button(frame, text="Registrar producto", command=self.registerProduct).grid(row=3,columnspan=2, sticky=W+E)
        ttk.Button(text="Eliminar", command=self.delete).grid(row=5, column=0, sticky=W+E)
        ttk.Button(text="Editar", command=self.edit).grid(row=5, column=1, sticky=W+E)
        ttk.Button(text="Ver información", command=self.showInfo).grid(row=5, column=2, sticky=W+E)
        ttk.Button(text="Vender", command=self.sell).grid(row=5, column=3, sticky=W+E)

        self._table = ttk.Treeview(height = 10, columns = ('#1','#2',"#3"))
        self._table.grid(row=4, column=0, columnspan=4)
        self._table.heading("#0", text="Nombre del producto",anchor=CENTER)
        self._table.heading("#1", text="Precio del producto",anchor=CENTER)
        self._table.heading("#2", text="Existencias del producto",anchor=CENTER)
        self._table.heading("#3", text="Unidades vendidas",anchor=CENTER)
        self.getProducts()
    def getProducts(self):
        products = self._table.get_children()
        for product in products:
            self._table.delete(product)
        nameProducts = list(self._inventory.itemsDict.keys())
        for productKey in nameProducts:
            name = self._inventory.itemsDict[productKey].name
            price = self._inventory.itemsDict[productKey].prize
            amount = self._inventory.itemsDict[productKey].amount
            sales = self._inventory.itemsDict[productKey].sales
            self._table.insert("", 0, text=name, values=[price, amount, sales])
    def validateItem(self):
        if len(self._name.get()) != 0 and len(self._price.get()) != 0:
            try:
                self._price = int(self._price.get())
                return True
            except:
                self.message["text"]="El precio debe ser un valor númerico."
                return False
        else:
            self.message["text"]="Los campos anteriores son obligatorios."
            return False
    def registerProduct(self):
        if self.validateItem():
            self.creationWindow = Toplevel()
            self.creationWindow.title = "Registrar nuevo producto"
        else:
            pass
    def delete(self):
        try:
            item = str(self._table.item(self._table.selection()[0])["text"])
            self._inventory.delete(item)
            self.message["text"]="El producto {} fue eliminado correctamente.".format(item)
            self.getProducts()
        except:
            self.message["text"]="Seleccione un producto."
    def edit(self):
        try:
            item = str(self._table.item(self._table.selection())["text"])
            price = float(self._table.item(self._table.selection())["values"][0])
            self.editWindow = Toplevel()
            self.editWindow.title = "Editar producto"
            Label(self.editWindow, text="Nombre actual: ").grid(row=0, column=1)
            Entry(self.editWindow, textvariable= StringVar(self.editWindow, value=item), state="readonly").grid(row=0,column=2)
            Label(self.editWindow, text="Precio actual: ").grid(row=2, column=1)
            Entry(self.editWindow, textvariable= StringVar(self.editWindow, value=price), state="readonly").grid(row=2,column=2)
            Label(self.editWindow, text="Nombre nuevo: ").grid(row=1, column=1)
            newName = Entry(self.editWindow)
            newName.grid(row=1,column=2)
            Label(self.editWindow, text="Precio nuevo: ").grid(row=3, column=1)
            newPrize = Entry(self.editWindow)
            newPrize.grid(row=3,column=2)
            commentary = self._inventory.itemsDict[item].commentary
            Label(self.editWindow, text="Comentario actual: ").grid(row=4, column=1)
            Entry(self.editWindow, textvariable= StringVar(self.editWindow, value=commentary), state="readonly").grid(row=4,column=2)
            Label(self.editWindow, text="Comentario Nuevo").grid(row=5,column=1)
            newCommentary = Entry(self.editWindow)
            newCommentary.grid(row=5, column=2)
            amount = self._inventory.itemsDict[item].amount
            Label(self.editWindow, text="Cantidad de existencias: ").grid(row=6, column=1)
            Entry(self.editWindow, textvariable= StringVar(self.editWindow, value=amount), state="readonly").grid(row=6,column=2)
            Label(self.editWindow, text="Nueva cantidad de existencias: ").grid(row=7, column=1)
            newAmount = Entry(self.editWindow)
            newAmount.grid(row=7, column=2)
            self.message2 = Label(self.editWindow, text="", fg="red")
            self.message2.grid(row=8, column=2, columnspan=2, sticky=W+E)
            Button(self.editWindow, text="Guardar cambios",command= lambda: self.saveEdit(item, newName.get(), newPrize.get(), newCommentary.get(), newAmount.get())).grid(row=9, column=2, sticky=W)
        except:
            self.message["text"]="Seleccione un producto."
    def showInfo(self): 
        try:
            item = str(self._table.item(self._table.selection())["text"])
            price = float(self._table.item(self._table.selection())["values"][0])
            amount = int(self._table.item(self._table.selection())["values"][1])
            self.infoWindow = Toplevel()
            self.infoWindow.title = "Información producto"
            Label(self.infoWindow, text="Nombre del producto: ").grid(row=0, column=1)
            Entry(self.infoWindow, textvariable= StringVar(self.infoWindow, value=item), state="readonly").grid(row=0,column=2)
            Label(self.infoWindow, text="Precio del producto: ").grid(row=1, column=1)
            Entry(self.infoWindow, textvariable= StringVar(self.infoWindow, value=price), state="readonly").grid(row=1,column=2)
            Label(self.infoWindow, text="Existencias del producto: ").grid(row=2, column=1)
            Entry(self.infoWindow, textvariable= StringVar(self.infoWindow, value=amount), state="readonly").grid(row=2,column=2)
            commentary = self._inventory.itemsDict[item].commentary
            Label(self.infoWindow, text="Comentario del producto: ").grid(row=3, column=1)
            Entry(self.infoWindow, textvariable= StringVar(self.infoWindow, value=commentary), state="readonly").grid(row=3,column=2)
            self._tableRegister = ttk.Treeview(self.infoWindow, height = 4)
            self._tableRegister.grid(row=4, column=0, columnspan= 5)
            self._tableRegister.column('#0', width=400, anchor=CENTER)
            self._tableRegister.heading("#0", text="Historial del producto", anchor=CENTER)
            product = self._inventory.itemsDict[item]
            history = product.register.listChanges
            for change in history:
                self._tableRegister.insert("", 0, text=change)
        except:
            self.message["text"]="Seleccione un producto."
    def  sell(self):
        try: 
            item = str(self._table.item(self._table.selection())["text"])
            product = self._inventory.itemsDict[item]
            self.sellWindow = Toplevel()
            Label(self.sellWindow, text="Nombre del producto: ").grid(row=0, column=1)
            Entry(self.sellWindow, textvariable= StringVar(self.sellWindow, value=item), state="readonly").grid(row=0,column=2)
            Label(self.sellWindow, text="Existencias del producto: ").grid(row=1, column=1)
            Entry(self.sellWindow, textvariable= StringVar(self.sellWindow, value=product.amount), state="readonly").grid(row=1,column=2)
            Label(self.sellWindow, text="Unidades a vender: ").grid(row=2, column=1)
            sell = Entry(self.sellWindow)
            sell.grid(row=2, column=2)
            self.message2 = Label(self.sellWindow, text="", fg="red")
            self.message2.grid(row=3, column=0, columnspan=2, sticky=W+E)
            Button(self.sellWindow, text="Vender", command=lambda: self.sellProduct(item, sell)).grid(row=4, columnspan=2, sticky=W)
        except:
            self.message["text"]="Seleccione un producto."
    def sellProduct(self, item, amount):
        product = self._inventory.itemsDict[item]
        try:
            amount = amount.get()
            if product.amount < amount:
                self.message2["text"]="Ingrese un valor válido"
            else:
                amountDelta = ((self._itemsDict[item].amount)-amount)
                self._itemsDict[item].setAmount(amountDelta)
                self._itemsDict[item].checkStatus()
                (self._itemsDict[item]).register.newChange((str(amount)+" vendido(s)"))
                (self._itemsDict[item]).setSales(amount)
                (self._itemsDict[item]).checkStatus()
                self._register.newChange((str(amount)+item+"(s)"+" vendidos(s)."))
                self.message["text"]=(("Se han vendido "+str(amount)+" de "+item+"(s)"+" por un total de "+str(((self._itemsDict[item]).prize)*amount)))
                self.sellWindow.destroy()
        except:
            self.message2["text"]="ingrese valor valido"
    def saveEdit(self, item, newName, newPrize, newCommentary, newAmount):
        try:
            product = self._inventory.itemsDict[item]
            if newName != "":
                product.setName(newName)
                self._inventory.itemsDict[product.name]=product
                del self._inventory.itemsDict[item]
            else:
                pass
            if newPrize != "":
                newPrize = float(newPrize)
                product.setPrize(newPrize)
            else:
                pass
            if newCommentary != "":
                product.setCommentary(newCommentary)
            else:
                pass
            if newAmount != "":
                newAmount = int(newAmount)
                product.setAmount(newAmount)
            self.editWindow.destroy()
            self.message["text"]="El producto {} ha sido editado correctamente.".format(item)
            self.getProducts()
        except:
            self.message2["text"]="Los valores de Precio y Cantidad deben ser númericos."