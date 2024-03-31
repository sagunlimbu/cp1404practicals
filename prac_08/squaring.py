# squaring.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class SquareNumberApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        top_layout = BoxLayout(orientation='horizontal')
        input_number = TextInput(hint_text="Enter a number", multiline=False)
        square_button = Button(text="Square")
        square_button.bind(on_press=self.handle_square)
        top_layout.add_widget(input_number)
        top_layout.add_widget(square_button)

        instruction_label = Label(text="Enter a number and press 'Square'", color=(1, 0, 1, 1))

        output_label = Label()
        top_layout.add_widget(output_label)

        layout.add_widget(top_layout)
        layout.add_widget(instruction_label)

        return layout

    def handle_square(self, instance):
        try:
            number = float(self.root.ids.input_number.text)
            result = number ** 2
            self.root.ids.output_label.text = f"Square of {number} is {result}"
        except ValueError:
            self.root.ids.output_label.text = "Invalid input. Please enter a valid number."


if __name__ == '__main__':
    SquareNumberApp().run()
