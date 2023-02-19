from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDDatePicker

import sys

sys.path.append("api")

from api import api_post

Builder.load_file('./Screens/adicionar_agendamento.kv')

class AdicionarAgendamento(Screen):
    def __init__(self, **kwargs):
        super(AdicionarAgendamento, self).__init__(**kwargs)
        opcoes_horario = ["7:00","8:00","9:00","10:00","11:00","13:00","14:00","15:00"]
        menu_items = [
            {
                "text": f"{opcao}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=opcao: self.select_horario(x),
            } for opcao in opcoes_horario
        ]

        self.menu = MDDropdownMenu(
            caller=self.ids.horarios,
            items=menu_items,
            width_mult=4,
            position='bottom',
        )
        
        self.ids.nome.bind(
            on_focus=self.set_error_message,
        )
        self.data_agendamento = None
        #self.label_errors = MDLabel()


    def select_horario(self, horario):
        self.ids.horarios.text = horario
        self.menu.dismiss()
    
        
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    
    
    def on_save(self, instance, value, date_range):
        data = value.isoformat().split('-')
        self.data_agendamento = value
        data = data[2] + "/" + data[1] + "/" + data[0]
       
        self.ids.data_escolhida.text = data

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        instance.dismiss()

    def retornar_tela_inicial(self):
        self.manager.current = 'lista-agendamentos'
    
    def mostrar_erros(self, resposta):
        mapa = {
            "date": "Data",
            "name": "Nome",
            "telephone": "Telefone",
            "hour": "Horario",
            "email": "Email"
        }
        for chave in resposta.items():
            if chave[0] != "status":
                self.ids.erro.text += f"{mapa[chave[0]]}: " + chave[1][0] + "\n"
        
    def set_error_message(self, instance_textfield):
        self.ids.nome.error = True
    
    def enviar_formulario(self):
        self.ids.erro.text = ""
        novo_agendamento = {
            "name": self.ids.nome.text,
            "email": self.ids.email.text,
            "telephone": self.ids.telefone.text,
            "date": self.data_agendamento,
            "healthInsurance": "",
            "hour": self.ids.horarios.text
        }
        try:    
            response = api_post(novo_agendamento)
            
            if response["status"] != 200:
                self.mostrar_erros(response)


        except ValueError as e:
            #print(response["content"])
            print(f"ERRO {e}")
        