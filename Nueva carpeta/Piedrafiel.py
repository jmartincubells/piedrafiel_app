from tkinter import *
from datetime import datetime
from tkinter import ttk
import tkinter as tk
import sqlite3

toStirng

class Tab_Control:
    db_name = 'database.db'

    def __init__(self, root):
        self.root = root
        self.root.title("Piedrafiel")
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


        Label(frame, text='Cliente: ').grid(row=1, column=0)
        self.client = Entry(frame)
        self.client.focus()  # The cursor will appear hear
        self.client.grid(row=1, column=1)

        Label(frame, text='Producto: ').grid(row=2, column=0)
        self.product = Entry(frame)
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
        self.message.grid(row=5, column=0, columnspan=2, sticky=W + E)

        # Table
        def width(colunm, text, width):
            num_column = "#" + str(colunm)
            self.tree.column(num_column, width=width)
            self.tree.heading(num_column, text=text, anchor=W)
            return

        self.tree = ttk.Treeview(self.TabControl1, height=10, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        self.tree.grid(row=3, column=0, columnspan=4)
        width(0, 'Codigo', 60)
        width(1, 'Cliente', 100)
        width(2, 'Producto', 100)
        width(3, 'Cantidad', 100)
        width(4, 'Fecha de pedido', 100)
        width(5, 'Fecha de entrega', 100)
        width(6, 'Vendedor', 100)
        width(7, 'Total', 100)

        self.scrollbar(self.TabControl1, 3, 4, self.tree)
        # Buttons
        ttk.Button(self.TabControl1, text='Marcar como entregado', command=self.mark_as_done).grid(row=4, column=0, sticky=W + E)
        ttk.Button(self.TabControl1, text='Actualizar', command=lambda: self.message_tab1('Pagina refrescada') and self.get_products).grid(row=4, column=1, sticky=W + E)
        ttk.Button(self.TabControl1, text='Editar', command=lambda: self.edit_product('product')).grid(row=4, column=2, sticky=W + E)
        ttk.Button(self.TabControl1, text='Eliminar', command=lambda: self.delete_pop_out('product')).grid(row=4, column=3, sticky=W + E)
        # Filling the Rows
        self.get_products()

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////TAB 2/////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////



        def width_tab2(colunm, text, width):
            num_column = "#" + str(colunm)
            self.tree_tab2.column(num_column, width=width)
            self.tree_tab2.heading(num_column, text=text, anchor=W)
            return

        self.tree_tab2 = ttk.Treeview(self.TabControl2, height=16, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        self.tree_tab2.grid(row=0, column=0, columnspan=4)
        width_tab2(0, 'Codigo', 60)
        width_tab2(1, 'Cliente', 100)
        width_tab2(2, 'Producto', 100)
        width_tab2(3, 'Cantidad', 100)
        width_tab2(4, 'Fecha de pedido', 100)
        width_tab2(5, 'Fecha de entrega', 100)
        width_tab2(6, 'Vendedor', 100)
        width_tab2(7, 'Total', 100)

        self.scrollbar(self.TabControl2, 0, 4, self.tree_tab2)

        self.get_products_tab2()

        tk.Button(self.TabControl2, text='Marcar como en progreso', command=self.mark_as_in_progress).grid(row=1, column=0,
                                                                                            sticky=W + E)
        tk.Button(self.TabControl2, text='Actualizar', command=self.get_products_tab2).grid(row=1, column=1, sticky=W + E)
        tk.Button(self.TabControl2, text='Editar', command=lambda: self.edit_product('history_of_')).grid(row=1, column=2, sticky=W + E)
        tk.Button(self.TabControl2, text='Eliminar', command=lambda: self.delete_pop_out("history_of_")).grid(row=1, column=3, sticky=W + E)

        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////TAB 3/////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # /////////////////////////////////////////////////////////////////////////////////////////////////////////////

        Label(self.TabControl3, text = 'Version 1.0.0').grid(row=0, column=1)

    def message_tab1(self, text):
        message = Label(self.TabControl1, text=text, fg='red')
        message.grid(row=5, column=0, columnspan=2, sticky=W + E)

    def message_tab2(self, text):
        message = Label(self.TabControl2, text=text, fg='red')
        message.grid(row=2, column=0, columnspan=2, sticky=W + E)

    def scrollbar(self, tab_number, row, column, object):
        scrollbar = ttk.Scrollbar(tab_number, orient='vertical', command= object.yview)
        scrollbar.grid(row=row, column=column, sticky='ns')
        #  communicate back to the scrollbar
        object['yscrollcommand'] = scrollbar.set

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
            actual_date = datetime.now().strftime('%d-%m-%Y')
            query = 'INSERT INTO product VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)'
            parameters = (self.client.get(), self.product.get(), self.amount.get(), actual_date,
                          self.date_of_delivery.get(),
                          self.seller.get(), self.total.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Pedido tomado exitosamente'
            self.product.delete(0, END)
            self.amount.delete(0, END)
            self.client.delete(0, END)
            self.date_of_delivery.delete(0, END)
            self.seller.delete(0, END)
            self.total.delete(0, END)
        else:
            self.message['text'] = 'Faltan datos'
        self.get_products()

    def delete_pop_out(self, tab):
        self.message['text'] = ''
        if tab == 'product':
            try:
                product = self.tree.item(self.tree.selection())['text']
            except IndexError as e:
                self.message['text'] = 'Please, select Record'
                return
        else:
            try:
                product = self.tree_tab2.item(self.tree_tab2.selection())['text']
            except IndexError as e:
                self.message['text'] = 'Please, select Record'
                return

        self.delete_wind = Toplevel()
        self.delete_wind.title = 'Elimiar pedido'

        Label(self.delete_wind, text = "¿Estas seguro que deseas borrar el pedido?").grid(row = 0, column = 0, pady = 10, columnspan = 2)
        tk.Button(self.delete_wind, text='Aceptar', command=lambda: self.delete_tab(tab, product)).grid(row=1, column=1, sticky=W + E)
        tk.Button(self.delete_wind, text='Cancelar', command=self.delete_wind.destroy).grid(row=1, column=0, sticky=W + E)

    def delete_tab(self, tab, producto):
        query = 'DELETE FROM {} WHERE id = ?'.format(tab)
        self.run_query(query, (producto, ))
        message = 'Pedido "{}" fue eliminado'.format(producto)
        if tab == 'product':
            self.message_tab1(message)
        else:
            self.message_tab2(message)

        self.delete_wind.destroy()
        self.get_products()
        self.get_products_tab2()

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
        message = '"{}" Marcado como en entregado'.format(name)
        self.message_tab1(message)
        self.get_products()
        self.get_products_tab2()

    def mark_as_in_progress(self):
        self.message['text'] = ''
        try:
            self.tree_tab2.item(self.tree_tab2.selection())['text']
        except IndexError as e:
            self.message['text'] = 'Porfavor seleccione un pedido'
            return
        self.message['text'] = ''
        name = self.tree_tab2.item(self.tree_tab2.selection())['text']
        query = 'INSERT INTO product SELECT * FROM history_of_ WHERE id = ?'
        cut_query = 'DELETE FROM history_of_ WHERE id = ?'
        self.run_query(query, (name,))
        self.run_query(cut_query, (name,))
        message = '"{}" Marcado como en proceso'.format(name)
        self.message_tab2(message)
        self.get_products()
        self.get_products_tab2()

    def edit_product(self, tab):
        self.message['text'] = ''
        if tab == 'product':
            try:
                number = self.tree.item(self.tree.selection())['text']
                tree_tab = self.tree.item(self.tree.selection())["values"]
            except IndexError as e:
                self.message['text'] = 'Please, select Record'
                return
        else:
            try:
                number = self.tree_tab2.item(self.tree_tab2.selection())['text']
                tree_tab = self.tree_tab2.item(self.tree_tab2.selection())["values"]
            except IndexError as e:
                self.message['text'] = 'Please, select Record'
                return

        client = tree_tab[0]  # Valor que va a tomar de la DB
        product = tree_tab[1]  # Valor que va a tomar de la DB
        amount = tree_tab[2]  # Valor que va a tomar de la DB
        date_register = tree_tab[3]
        date_of_delivery = tree_tab[4]  # Valor que va a tomar de la DB
        seller = tree_tab[5]  # Valor que va a tomar de la DB
        total = tree_tab[6]

        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'

        # Old Name
        Label(self.edit_wind, text='Nombre de cliente registrado').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=client), state='readonly').grid(row=0,
                                                                                                         column=2)
        # New Name
        Label(self.edit_wind, text='Cliente: ').grid(row=1, column=1)
        client_edit = Entry(self.edit_wind)
        client_edit.grid(row=1, column=2)

        # Old Price
        Label(self.edit_wind, text='Producto registrado: ').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=product), state='readonly').grid(row=2,
                                                                                                              column=2)
        # New Price
        Label(self.edit_wind, text='Producto: ').grid(row=3, column=1)
        product_edit = Entry(self.edit_wind)
        product_edit.grid(row=3, column=2)

        Label(self.edit_wind, text='Cantidad registrada: ').grid(row=4, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=amount), state='readonly').grid(row=4,
                                                                                                           column=2)
        # New Name
        Label(self.edit_wind, text='Cantidad: ').grid(row=5, column=1)
        amount_edit = Entry(self.edit_wind)
        amount_edit.grid(row=5, column=2)

        Label(self.edit_wind, text='Fecha del pedido registrada: ').grid(row=6, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=date_register), state='readonly').grid(
            row=8,
            column=2)
        # New Name
        Label(self.edit_wind, text='Fecha del pedido: ').grid(row=7, column=1)
        date_register_edit = Entry(self.edit_wind)
        date_register_edit.grid(row=7, column=2)

        Label(self.edit_wind, text='Dia de entrega registrado: ').grid(row=8, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=date_of_delivery), state='readonly').grid(row=8,
                                                                                                           column=2)
        # New Name
        Label(self.edit_wind, text='Dia de entrega: ').grid(row=9, column=1)
        date_of_delivery_edit = Entry(self.edit_wind)
        date_of_delivery_edit.grid(row=9, column=2)

        # Old Price
        Label(self.edit_wind, text='Vendedor registrado: ').grid(row=10, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=seller), state='readonly').grid(row=10,
                                                                                                            column=2)
        # New Price
        Label(self.edit_wind, text='Vendedor: ').grid(row=11, column=1)
        seller_edit = Entry(self.edit_wind)
        seller_edit.grid(row=11, column=2)

        Label(self.edit_wind, text='Total registrado: ').grid(row=12, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=total), state='readonly').grid(row=12,
                                                                                                           column=2)
        # New Price
        Label(self.edit_wind, text='Total: ').grid(row=13, column=1)
        total_edit = Entry(self.edit_wind)
        total_edit.grid(row=13, column=2)

        Label(self.edit_wind, text='LOS ESPACIOS EN BLANCO SE QUEDARAN GUARDADOS EN BLANCO').grid(row=14, column=1, columnspan= 2, pady = 10)

        Button(self.edit_wind, text='Editar',
               command=lambda: self.edit_records(tab, number, client_edit.get(), client, product_edit.get(), product, amount_edit.get(), amount, date_register_edit.get(), date_register, date_of_delivery_edit.get(), date_of_delivery, seller_edit.get(), seller, total_edit.get(), total)
               ).grid(row=14, column=2, sticky=W + E, columnspan = 2)
        self.edit_wind.mainloop()

    def edit_records(self, tab, number, client_edit, client, product_edit, product, amount_edit, amount, date_register_edit, date_register, date_of_delivery_edit, date_of_delivery, seller_edit, seller, total_edit, total):
        if tab == 'product':
            query = 'UPDATE product SET id = ?, Cliente = ?, Producto = ? , Cantidad = ?, Fecha_de_Pedido  = ?, Fecha_de_entrega = ?, Vendedor = ?, Total = ? WHERE id = ? AND Cliente = ? AND Producto = ? AND Cantidad = ? AND Fecha_de_Pedido  = ? AND Fecha_de_entrega = ? AND Vendedor = ? AND Total = ?'
        else:
            query = 'UPDATE history_of_ SET id = ?, Cliente = ?, Producto = ? , Cantidad = ?, Fecha_de_Pedido  = ?, Fecha_de_entrega = ?, Vendedor = ?, Total = ? WHERE id = ? AND Cliente = ? AND Producto = ? AND Cantidad = ? AND Fecha_de_Pedido  = ? ANDFecha_de_entrega = ? AND Vendedor = ? AND Total = ?'

        parameters = (number, client_edit, product_edit, amount_edit, date_register_edit, date_of_delivery_edit, seller_edit, total_edit, number, client, product, amount, date_register, date_of_delivery, seller, total)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Record {} updated successfylly'.format(client)
        self.get_products()
        self.get_products_tab2()

if __name__ == '__main__':
    root = Tk()
    application = Tab_Control(root)
    root.mainloop()
