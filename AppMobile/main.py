from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import os
os.environ['KIVYMD_LANG'] = 'pt'
import sys
sys.path.append("./Screens")

from Screens.ListaAgendamentos import ListaAgendamentos
from Screens.AdicionarAgendamento import AdicionarAgendamento

class MyScreenManager(MDScreenManager):
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.material_style = "M3"
        sm = MyScreenManager()
        sm.add_widget(ListaAgendamentos(name="lista-agendamentos"))
        sm.add_widget(AdicionarAgendamento(name="adicionar-agendamento"))
        return sm



if __name__ == '__main__':
    MyApp().run()