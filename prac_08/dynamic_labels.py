from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        main_layout = BoxLayout(orientation='vertical', id='main')

        names = ["John", "Jane", "Alice", "Bob", "Eve"]

        for name in names:
            label = Label(text=name)
            main_layout.add_widget(label)

        layout.add_widget(main_layout)
        return layout


if __name__ == '__main__':
    DynamicLabelsApp().run()
