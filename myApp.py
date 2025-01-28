from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from bounceApp import BouncingDVDApp  # Import the BouncingDVDApp class

# Load the .kv file
Builder.load_file("login_form.kv")


class LoginForm(FloatLayout):
    def __init__(self, **kwargs):
        super(LoginForm, self).__init__(**kwargs)

    def validate_login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        if username == "admin" and password == "password":
            self.clear_widgets()
            self.add_widget(
                Label(
                    text="Login Successful!",
                    size_hint=(0.6, 0.1),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
            )
            self.run_bounce_app()
        else:
            self.clear_widgets()
            self.add_widget(
                Label(
                    text="Login Failed!",
                    size_hint=(0.6, 0.1),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
            )
            try_again_button = Button(
                text="Try Again",
                size_hint=(0.4, 0.1),
                pos_hint={"center_x": 0.5, "center_y": 0.4},
            )
            try_again_button.bind(on_press=self.reset_login_form)
            self.add_widget(try_again_button)

    def reset_login_form(self, instance):
        self.clear_widgets()
        self.add_widget(LoginForm())

    def run_bounce_app(self):
        App.get_running_app().stop()  # Stop the current app
        BouncingDVDApp().run()  # Run the BouncingDVDApp


class MyApp(App):
    def build(self):
        return LoginForm()


if __name__ == "__main__":
    MyApp().run()
