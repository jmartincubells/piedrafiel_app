from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_file('till_operator/operator.kv')


class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    Window.size = (1366, 768)
    def add_order(self):
        products_container = self.ids.products
        client = self.ids.client_inp.text
        tel = self.ids.phonenumber_inp.text
        email = self.ids.email_inp.text
        date_delivery = self.ids.date_of_delivery_inp.text
        seller = self.ids.seller_inp.text
        # client = self.ids.client_inp.text
        # client = self.ids.client_inp.text

        self.details = BoxLayout(size_hint_y=None, height=30)
        products_container.add_widget(self.details)

        id_l = Label(text='0', size_hint_x=.05, color=(.06, .45, .45, 1))
        client_l = Label(text=client, size_hint_x=.2, color=(.06, .45, .45, 1))
        tel_l = Label(text=tel, size_hint_x=.1, color=(.06, .45, .45, 1))
        actual_date_l = Label(text='??/??/????', size_hint_x=.2, color=(.06, .45, .45, 1))
        date_delivery_l= Label(text=date_delivery, size_hint_x=.15, color=(.06, .45, .45, 1))
        seller_l= Label(text=seller, size_hint_x=.2, color=(.06, .45, .45, 1))
        total_l = Label(text='?????', size_hint_x=.07, color=(.06, .45, .45, 1))
        edit = Button(text='>', size_hint_x=.03, color=(.06, .45, .45, 1))
        edit.bind(on_release=self.edit_orders)

        self.details.add_widget(id_l)
        self.details.add_widget(client_l)
        self.details.add_widget(tel_l)
        self.details.add_widget(actual_date_l)
        self.details.add_widget(date_delivery_l)
        self.details.add_widget(seller_l)
        self.details.add_widget(total_l)
        self.details.add_widget(edit)


    def edit_orders(self, widget):
        pass


    def add_more(self):
        prod_addmore = self.ids.product_inputs

        self.product = BoxLayout(size_hint_x=1, height=30, spacing=5)
        

        prod = TextInput(size_hint_x=.2)
        qty = TextInput(size_hint_x=.1)
        price = TextInput(size_hint_x=.1)
        delete = Button(text='-', size_hint_x=.05)

        self.product.add_widget(prod)
        self.product.add_widget(qty)
        self.product.add_widget(price)
        self.product.add_widget(delete)

        prod_addmore.add_widget(self.product)
        delete.bind(on_release=self.deleting)

    def deleting(self, instance):
        instance.parent.ids.lid.text= self.get_id(instance)


class OperatorApp(App):
    def build(self):
        return OperatorWindow()


if __name__ == "__main__":
    oa = OperatorApp()
    oa.run()
