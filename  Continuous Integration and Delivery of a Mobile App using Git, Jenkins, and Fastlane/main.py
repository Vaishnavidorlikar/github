# Development - Simple Mobile App using Python (Kivy Framework)
# main.py (Mobile App Code)
import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello World!')

if __name__ == '__main__':
    MyApp().run()