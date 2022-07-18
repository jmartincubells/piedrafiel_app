from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# from admindashboard.admindashboard import AdminWindow
from till_operator.till_operator import OperatorWindow
from signin.signin import SigninWindow


class MainWindow(BoxLayout):
    signin_widget = SigninWindow()
    operator_widget = OperatorWindow()
    # admin_widget = AdminWindow()

    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.screen_si.add_widget(self.signin_widget)
        # self.ids.screen_admin.add_widget(self.admin_widget)
        self.ids.screen_op.add_widget(self.operator_widget)


class MainApp(App):
    def build(self):
        return MainWindow()


if __name__=="__main__":
    sa = MainApp()
    sa.run()