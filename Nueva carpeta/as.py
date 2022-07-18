from tkinter import ttk
from tkinter import *
from datetime import datetime

import sqlite3

class Tab1:
    # connection dir property
    db_name = 'database.db'

    def __init__(self, window):
        # Initializations
        self.wind = window
        self.wind.title('PiedraFiel')
        self.wind.geometry("1920x1080+0+0")

        # Creating a Frame Container
        frame = LabelFrame(self.wind, text = 'Registro de pedidos')
        frame.grid(row = 0, columnspan = 5, pady = 10)

        # Name Input
        Label(frame, text = 'Producto: ').grid(row = 1, column = 0)
        self.product = Entry(frame)
        self.product.focus() # The cursor will appear hear
        self.product.grid(row = 1, column = 1)

        Label(frame, text='Cantidad: ').grid(row=2, column=0)
        self.amount = Entry(frame)
        self.amount.grid(row=2, column=1)

        Label(frame, text='Cliente: ').grid(row=3, column=0)
        self.client = Entry(frame)
        self.client.grid(row=3, column=1)

        Label(frame, text='Fecha de entrega: ').grid(row=1, column=2)
        self.date_of_delivery = Entry(frame)
        self.date_of_delivery.grid(row=1, column=3)

        Label(frame, text='Vendedor: ').grid(row=2, column=2)
        self.seller = Entry(frame)
        self.seller.grid(row=2, column=3)

        # Price Input
        Label(frame, text = 'Total: ').grid(row = 3, column = 2)
        self.total = Entry(frame)
        self.total.grid(row = 3, column = 3)

        # Button Add Product
        ttk.Button(frame, text = 'Agregar pedido', command = self.add_product).grid(row = 4, columnspan = 4, sticky = W + E)

        # Output Messages
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Table
        self.tree = ttk.Treeview(height = 10, columns = ('#1','#2','#3','#4','#5','#6', '7'))
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text='id', anchor = W)
        self.tree.heading('#1', text = 'Producto', anchor = CENTER)
        self.tree.heading('#2', text = 'Cantidad', anchor = CENTER)
        self.tree.heading('#3', text ='Cliente', anchor=CENTER)
        self.tree.heading('#4', text ='Fecha de pedido', anchor=CENTER)
        self.tree.heading('#5', text ='Fecha de entrega', anchor=CENTER)
        self.tree.heading('#6', text ='Vendedor', anchor=CENTER)
        self.tree.heading('#7', text ='Total', anchor=CENTER)


        # Buttons
        ttk.Button(text = 'DELETE', command = self.delete_product).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(text = 'EDIT', command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)

        # Filling the Rows
        self.get_products()


    # Function to Execute Database Querys
    def run_query(self, query, parameters = ()):
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
            print(row)
            self.tree.insert('', 0, text = row[0], values = (row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    # User Input Validation
    def validation(self):
        return len(self.product.get()) != 0 and len(self.total.get()) != 0

    def add_product(self):
        if self.validation():
            self.actual_date = datetime.now().strftime('%d-%m-%Y')
            query = 'INSERT INTO product VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.product.get(), self.amount.get(), self.client.get(), self.actual_date, self.date_of_delivery.get(), self.seller.get(), self.total.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Pedido {} tomado exitosamente'.format(self.product.get())
            self.product.delete(0, END)
            self.total.delete(0, END)
        else:
            self.message['text'] = 'Faltan datos'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE producto = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'Record {} deleted Successfully'.format(name)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Please, select Record'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_price = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'
        # Old Name
        Label(self.edit_wind, text = 'Old Name:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)
        # New Name
        Label(self.edit_wind, text = 'New Price:').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)

        # Old Price
        Label(self.edit_wind, text = 'Old Price:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 2, column = 2)
        # New Price
        Label(self.edit_wind, text = 'New Name:').grid(row = 3, column = 1)
        new_price= Entry(self.edit_wind)
        new_price.grid(row = 3, column = 2)

        Button(self.edit_wind, text = 'Update', command = lambda: self.edit_records(new_name.get(), name, new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W)
        self.edit_wind.mainloop()

    def edit_records(self, new_name, name, new_price, old_price):
        query = 'UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?'
        parameters = (new_name, new_price,name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated successfylly'.format(name)
        self.get_products()

if __name__ == '__main__':
    window = Tk()
    application = Tab1(window)
    window.mainloop()

