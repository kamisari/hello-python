# vim: fileencoding=utf-8

from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text="hello world")

def main():
    print(App.uid)
    TestApp().run()

if __name__ == '__main__':
    main()
