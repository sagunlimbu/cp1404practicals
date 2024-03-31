from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutDemo(BoxLayout):
    def handle_greet(self):
        print("Greet")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        print("Clear")
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""

class BoxLayoutDemoApp(App):
    def build(self):
        return BoxLayoutDemo()

if __name__ == "__main__":
    BoxLayoutDemoApp().run()
