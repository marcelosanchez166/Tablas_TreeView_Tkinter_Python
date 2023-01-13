import imp
from pydoc import text
from tkinter import *
from tkinter import ttk


raiz=Tk()
raiz.geometry("600x500")
raiz.title("Treeview")


"""Creacion de un menu tipo Arbol con Treeview"""
# arbol=ttk.Treeview(raiz)
# menu1=arbol.insert("", END, text="Menu 1")# Menu 2 padre de los subelemntos del menu 1
# arbol.insert(menu1,END,text="SubElemento del menu 1")#Menu hijo del menu padre 1
# arbol.insert(menu1,END,text="SubElemento 2 del menu 1")#Menu hijo del menu padre 1
# menu2=arbol.insert("",END,text="Menu 2") # Menu 2 padre de los subelemntos del menu 2 
# submenu2=arbol.insert(menu2, END, text="SubElemento del menu 2")#Menu hijo del menu padre 2
# arbol.insert(submenu2, END,text="SubElemento del submenu del menu 2")#Menu hijo del submenu 1 del menu 2
# arbol.place(x=10, y=10)

"""Creando tablas para mostrar datos de una base de datos"""
arbol=ttk.Treeview(raiz, columns=("Precio", "Cantidad"))
arbol.heading("#0",text="Producto")
arbol.heading("Precio", text="Precio")
arbol.heading("Cantidad", text="Cantidad")
arbol.insert("", END, text="Galletas pricipe", values=("$0.60", "56"))
arbol.insert("", END, text="Papas lays", values=("$0.45", "34"))
#arbol.insert(raiz,END, text="Nachos Diana", values=("$0.10", "34"))

arbol.place(x=10, y=10)

raiz.mainloop()