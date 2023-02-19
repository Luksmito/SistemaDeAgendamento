from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatIconButton

import sys

sys.path.append("../Components")
sys.path.append("api")

from Components.ScheduleItem import ScheduleItem
from Components.CustomModules import CustomGraphics
from api import api_get

class ListaAgendamentos(Screen):
    def __init__(self, **kwargs):
        super(ListaAgendamentos, self).__init__(**kwargs)
        #Metodo para se deletar
        
        print("init")
        #inicializando estilo do app
        
        schedules = 0

        #pegando os dados da api
        try:
            response = api_get()
            schedules = response
        except:
             schedules = [{"id": x, "name": f"Item{x}", "date": str(x)} for x in range(30)]
        
        #botao que vai para a tela de adicionar agendamento
        botao_adicionar = MDRectangleFlatIconButton(
                icon = "plus",
                text = "Adicionar agendamento",
                theme_text_color = "Custom",
                text_color = "white",
                line_color = "red",
                theme_icon_color = "Custom",
                icon_color = "orange", 
                padding = 10,
            )
        botao_adicionar.bind(on_press=self.tela_adicionar_agendamento)    

        #criando o Grid que vai receber cada item
        tela = MDGridLayout(cols=1, size_hint_y=None, spacing=5)
        tela.bind(minimum_height=tela.setter("height"))
    
        
        tela.add_widget(botao_adicionar)
        

        #adiciona cada item na tela
        scroll = ScrollView()
        for schedule in schedules:
            box = ScheduleItem(id_db=schedule["id"], nome=schedule["name"], data=schedule["date"],hora=schedule["hour"], button_text='Botão')
            tela.add_widget(box)
        
        scroll.add_widget(tela)
        self.add_widget(scroll)

    def tela_adicionar_agendamento(self, instance):
        self.manager.current = 'adicionar-agendamento'
    
