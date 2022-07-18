from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder

Builder.load_file('signin/signin.kv')

check = False

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        password = self.ids.pwd_field
        info = self.ids.info
        

        uname = user.text
        pws = password.text

        if uname == '' or pws == '':
            info.text = '[color=#FF0000]usuario y/o contraseña son requeridos[/color]'
        else:
            if uname == 'admin' and pws == 'admin':
                info.text = '[color=#00FF00]Incio de sesion correcto[/color]'
                self.parent.parent.current = 'screen_op'
                check = True
            else:
                info.text = '[color=#FF0000]Usuario o contraseña son incorrectos[/color]'

class SigninApp(App):
    def build(self):
        return SigninWindow()


if __name__=="__main__":
    sa = SigninApp()
    sa.run()