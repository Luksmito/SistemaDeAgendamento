from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class DropDownButton(Button):
    def __init__(self, options, **kwargs):
        super().__init__(**kwargs)
        self.options = options
        self.drop_down = DropDown()
        for option in self.options:
            btn = Button(text=option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.drop_down.select(btn.text))
            self.drop_down.add_widget(btn)
        self.bind(on_release=self.drop_down.open)
        self.drop_down.bind(on_select=lambda instance, x: setattr(self, 'text', x))

class DropDownExample(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        options = ['8:00', '9:00', '10:00', '11:00', '12:00']
        dropdown_button = DropDownButton(options, text=options[0])
        layout.add_widget(dropdown_button)
        return layout

if __name__ == '__main__':
    DropDownExample().run()
