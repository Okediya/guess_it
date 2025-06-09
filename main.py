from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import random

class NumberGuessingGame(BoxLayout):
    def __init__(self, **kwargs):
        super(NumberGuessingGame, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10


        self.number = random.randint(1, 100)
        self.balance = 0

        self.instruction_label = Label(text="Guess a number between 1 and 100:")
        self.balance_label = Label(text=f"Balance: ${self.balance}")
        self.guess_input = TextInput(multiline=False, input_filter='int')
        self.submit_button = Button(text="Submit Guess")
        self.feedback_label = Label(text="")

        self.add_widget(self.instruction_label)
        self.add_widget(self.balance_label)
        self.add_widget(self.feedback_label)
        self.add_widget(self.guess_input)
        self.add_widget(self.submit_button)
        

        self.submit_button.bind(on_press=self.check_guess)

    def check_guess(self, instance):
        try:
            guess = int(self.guess_input.text)
            if guess < self.number:
                self.feedback_label.text = "Too low!"
                self.balance -= 1
            elif guess > self.number:
                self.feedback_label.text = "Too high!"
                self.balance -= 1
            else:
                self.feedback_label.text = "You got it!"
                self.balance += 1
                self.submit_button.disabled = True
                Clock.schedule_once(self.reset_game, 2)

            self.balance_label.text = f"Balance: ${self.balance}"
        except ValueError:
            self.feedback_label.text = "Please enter a valid number!"
    
    def reset_game(self, dt):
        self.number = random.randint(1, 100)
        self.guess_input.text = ""
        self.feedback_label.text = ""
        self.submit_button.disabled = False

class NumberGuessingApp(App):
    def build(self):
        return NumberGuessingGame()
    
if __name__ == "__main__":
    NumberGuessingApp().run()