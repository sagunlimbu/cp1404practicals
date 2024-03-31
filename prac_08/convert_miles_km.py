from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class ConvertMilesKmApp(App):
    output_text = StringProperty("0.0")

    def build(self):
        return BoxLayout()


if __name__ == '__main__':
    ConvertMilesKmApp().run()
