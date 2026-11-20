from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyTool(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.label = Label(text=" IFF EDITOR\nBY JC2K", font_size=22)
        layout.add_widget(self.label)
        btn = Button(text="START", background_color=(0, 0.6, 1, 1), size_hint_y=0.3)
        btn.bind(on_press=self.pindot)
        layout.add_widget(btn)
        return layout
    def pindot(self, instance):
        self.label.text = "GUMAGANA BRO!\nReady na to gawing IFF Editor!"

if __name__ == "__main__":
    MyTool().run()