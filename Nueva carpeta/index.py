from tkinter import *
from datetime import datetime
from tkinter import ttk
import tkinter as tk
import sqlite3


class Tab_Control:
    db_name = 'database.db'

    def __init__(self, root):
        self.root = root
        self.root.title("Tab Control")
        # self.root.geometry("1350x800+0+0")
        self.root.configure(background='gainsboro')

        notebook = ttk.Notebook(self.root)
        self.TabControl1 = ttk.Frame(notebook)
        self.TabControl2 = ttk.Frame(notebook)
        self.TabControl3 = ttk.Frame(notebook)
        notebook.add(self.TabControl1, text='Pedidos en curso')
        notebook.add(self.TabControl2, text='Historial de Pedidos')
        notebook.add(self.TabControl3, text='Ajustes')
        notebook.grid()

        # ////////////////////////////
        # ////////////////////////////
        # ////////////////////////////
        # //////////TAB 1/////////////
        # ////////////////////////////
        # ////////////////////////////
        # ////////////////////////////

        frame = LabelFrame(self.TabControl1, text='Registro de pedidos', fg="blue")
        frame.grid(row=0, columnspan=5, pady=10)

        # Name Input
        '''Label(frame, text='Producto: ').grid(row=1, column=0)
        self.programa = tk.StringVar(frame)  # Variable de control tipo cadena y lo guarda
        self.programa.set('-----------------')  # Tipo select
        programas = ("Ingeniería Industrial", "Ingeniería de Software", "Finanzas y Comercio Exterior",
                     "Negocios Internacionales")  # Opciones
        self.MenuPrograma = tk.OptionMenu(frame, self.programa, *programas).grid(row = 1, column = 1)'''

        Label(frame, text='Cliente: ').grid(row=1, column=0)
        self.client = Entry(frame)
        self.client.grid(row=1, column=1)

        Label(frame, text='Producto: ').grid(row=2, column=0)
        self.product = Entry(frame)
        self.product.focus()  # The cursor will appear hear
        self.product.grid(row=2, column=1)

        Label(frame, text='Cantidad: ').grid(row=3, column=0)
        self.amount = Entry(frame)
        self.amount.grid(row=3, column=1)

        Label(frame, text='Fecha de entrega: ').grid(row=1, column=2)
        self.date_of_delivery = Entry(frame)
        self.date_of_delivery.grid(row=1, column=3)

        Label(frame, text='Vendedor: ').grid(row=2, column=2)
        self.seller = Entry(frame)
        self.seller.grid(row=2, column=3)

        # Price Input
        Label(frame, text='Total: ').grid(row=3, column=2)
        self.total = Entry(frame)
        self.total.grid(row=3, column=3)

        # Button Add Product
        ttk.Button(frame, text='Agregar pedido', command=self.add_product).grid(row=4, columnspan=4, sticky=W + E)

        # Output Messages
        self.message = Label(self.TabControl1, text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # Table
        def width(colunm, text, width):
            num_column = "#" + str(colunm)
            self.tree.column(num_column, width=width)
            self.tree.heading(num_column, text=text, anchor=W)
            return

        self.tree = ttk.Treeview(self.TabControl1, height=10, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        self.tree.grid(row=4, column=0, columnspan=2)
        width(0, 'Codigo', 60)
        width(1, 'Cliente', 100)
        width(2, 'Producto', 100)
        width(3, 'Cantidad', 100)
        width(4, 'Fecha de pedido', 100)
        width(5, 'Fecha de entrega', 100)
        width(6, 'Vendedor', 100)
        width(7, 'Total', 100)

        # Buttons
        ttk.Button(self.TabControl1, text='Marcar como entregado', command=self.mark_as_done).grid(row=5, column=0,
                                                                                                   sticky=W + E)
        ttk.Button(self.TabControl1, text='Editar', command=self.edit_product).grid(row=5, column=1, sticky=W + E)

        def width_tab2(colunm, text, width):
            num_column = "#" + str(colunm)
            self.tree_tab2.column(num_column, width=width)
            self.tree_tab2.heading(num_column, text=text, anchor=W)
            return

        self.tree_tab2 = ttk.Treeview(self.TabControl2, height=15, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        self.tree_tab2.grid(row=4, column=0, columnspan=2)
        width_tab2(0, 'Codigo', 60)
        width_tab2(1, 'Cliente', 100)
        width_tab2(2, 'Producto', 100)
        width_tab2(3, 'Cantidad', 100)
        width_tab2(4, 'Fecha de pedido', 100)
        width_tab2(5, 'Fecha de entrega', 100)
        width_tab2(6, 'Vendedor', 100)
        width_tab2(7, 'Total', 100)

        # Filling the Rows
        self.get_products()
        self.get_products_tab2()

        # Function to Execute Database Querys

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

        # Get Products from Database

    def get_products(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM product ORDER BY id DESC'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('', 0, text=str(row[0]), values=(row[1:]))

    def get_products_tab2(self):
        # cleaning Table
        records = self.tree_tab2.get_children()
        for element in records:
            self.tree_tab2.delete(element)
        # getting data
        query = 'SELECT * FROM history_of_ ORDER BY id DESC'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree_tab2.insert('', 0, text=str(row[0]), values=(row[1:]))

        # User Input Validation

    def validation(self):
        return len(self.product.get()) != 0 and len(self.total.get()) != 0

    def add_product(self):
        if self.validation():
            self.actual_date = datetime.now().strftime('%d-%m-%Y')
            query = 'INSERT INTO product VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.client.get(), self.product.get(), self.amount.get(), self.actual_date,
                          self.date_of_delivery.get(),
                          self.seller.get(), self.total.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Pedido {} tomado exitosamente'.format(self.product.get())
            self.product.delete(0, END)
            self.amount.delete(0, END)
            self.client.delete(0, END)
            self.date_of_delivery.delete(0, END)
            self.seller.delete(0, END)
            self.total.delete(0, END)
        else:
            self.message['text'] = 'Faltan datos'
        self.get_products()

    def mark_as_done(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Porfavor seleccione un pedido'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'INSERT INTO history_of_ SELECT * FROM product WHERE id = ?'
        cut_query = 'DELETE FROM product WHERE id = ?'
        self.run_query(query, (name,))
        self.run_query(cut_query, (name,))
        self.message['text'] = 'Pedido "{}" marcado como entregado'.format(name)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            self.message['text'] = 'Please, select Record'
            return

        client = self.tree.item(self.tree.selection())["values"][0]  # Valor que va a tomar de la DB
        product = self.tree.item(self.tree.selection())["values"][1]  # Valor que va a tomar de la DB
        amount = self.tree.item(self.tree.selection())["values"][2]  # Valor que va a tomar de la DB
        actual_day = self.tree.item(self.tree.selection())["values"][3]  # Valor que va a tomar de la DB
        date_of_delivery = self.tree.item(self.tree.selection())["values"][4]  # Valor que va a tomar de la DB
        seller = self.tree.item(self.tree.selection())["values"][5]  # Valor que va a tomar de la DB
        total = self.tree.item(self.tree.selection())["values"][6]

        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'

        # Old Name
        Label(self.edit_wind, text='Old Name:').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=client), state='readonly').grid(row=0,
                                                                                                           column=2)
        # New Name
        Label(self.edit_wind, text='New Price:').grid(row=1, column=1)
        client_edit = Entry(self.edit_wind)
        client_edit.grid(row=1, column=2)

        # Old Price
        Label(self.edit_wind, text='Old Price:').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=product), state='readonly').grid(row=2,
                                                                                                            column=2)
        # New Price
        Label(self.edit_wind, text='New Name:').grid(row=3, column=1)
        product_edit = Entry(self.edit_wind)
        product_edit.grid(row=3, column=2)

        Label(self.edit_wind, text='Old Name:').grid(row=4, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=amount), state='readonly').grid(row=4,
                                                                                                           column=2)
        # New Name
        Label(self.edit_wind, text='New Price:').grid(row=5, column=1)
        amount_edit = Entry(self.edit_wind)
        amount_edit.grid(row=5, column=2)

        # Old Price
        Button(self.edit_wind, text='Update',
               command=lambda: self.edit_records(client_edit.get(), client, product_edit.get(), product,
                                                 amount_edit.get(), amount)).grid(row=14,
                      column=2,
                      sticky=W)
        self.edit_wind.mainloop()

    def edit_records(self, client_edit, client, product_edit, product, amount_edit,
                     amount):
        query = 'UPDATE product SET Cliente = ?, Producto = ? , Cantidad = ? WHERE Cliente = ? AND Producto = ? AND Cantidad = ?'
        parameters = (client_edit, product_edit, amount_edit, client, product,
                      amount)
        self.run_query(query, parameters)
        self.message['text'] = 'Record {} updated successfylly'.format(client)
        self.get_products()

        # ////////////////////////////
        # ////////////////////////////
        # ////////////////////////////
        # //////////TAB 2/////////////
        # ////////////////////////////
        # ////////////////////////////
        # ////////////////////////////


if __name__ == '__main__':
    root = Tk()
    application = Tab_Control(root)
    root.mainloop()
