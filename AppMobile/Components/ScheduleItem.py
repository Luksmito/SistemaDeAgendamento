from kivy.uix.popup import Popup
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.label import Label
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard

import sys

sys.path.append('../api')


from api import api_delete

class ScheduleItem(MDCard, Widget):
    def __init__(self,id_db = None, nome='a', data='a', button_text='a', hora="a", **kwargs):
        super().__init__(**kwargs)
        self.id_db = id_db
        #metodo para ser deletado
        self.register_event_type('on_deletado')

        #estilizacao
        self.style = "elevated"
        self.line_color=(0.2, 0.2, 0.2, 0.8)
        self.padding="4dp"
        self.shadow_softness=2
        self.shadow_offset=(0, 1)

        #tamanho
        self.valign = 'center'
        self.size_hint = (1, None)
        self.height = 100
        
        # Adiciona os Labels
        box_label = MDBoxLayout(orientation="horizontal")
        data = data.split("-")
        data = f"{data[2]}/{data[1]}/{data[0]}"
        label1 = Label(text=nome, size_hint=(0.45, 1))
        label2 = Label(text=data + "\n" + hora, size_hint=(0.45, 1))
        box_label.add_widget(label1)
        box_label.add_widget(label2)
        
        self.add_widget(box_label)

        # Adiciona o Botão
        button = MDFloatingActionButton(
                    icon="delete", 
                    size_hint=(0.1, 1), 

                )

        button.bind(on_release=self.show_confirmation_dialog)
        
        self.add_widget(button)

    def show_confirmation_dialog(self, button):
        dialog = MDDialog(
            title="Excluir Agendamento",
            text="Tem certeza que deseja excluir esse agendamento?",
            size_hint=(0.8, 1),
            buttons=[
                MDFlatButton(
                    text="Sim",
                    on_release=lambda x: self.delete_schedule(dialog)
                ),
                MDFlatButton(
                    text="Não",
                    on_release=lambda x: dialog.dismiss()
                ),
            ]
        )

        dialog.open()

    def delete_schedule(self, dialog):
        
        response = api_delete(self.id_db)    
        if response.status_code == 204:
            #dispara o evento de delete
            self.dispatch('on_deletado')
            dialog.dismiss()
        else:
            #cria um dialogo avisando que ocorreu um erro
            dialog.dismiss()
            dialog2 = MDDialog(
                title="Erro na exclusão",
                text=f"Erro ao tentar excluir agendamento, tente novamente mais tarde",
                size_hint=(0.8, 1),
            )
            dialog2.open()
        
    def on_deletado(self):
        self.parent.remove_widget(self)
