import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock


class BouncingDVDApp(App):
    icon = "Tux.png"  # Set the path to your icon file here

    def build(self):
        self.layout = FloatLayout()
        self.dvd_logo = Image(source="Tux.png", size_hint=(None, None), size=(400, 200))
        self.layout.add_widget(self.dvd_logo)
        self.direction_x = 1
        self.direction_y = 1
        Clock.schedule_interval(self.update, 1 / 60)
        return self.layout

    def update(self, dt):
        self.dvd_logo.x += self.direction_x * 2
        self.dvd_logo.y += self.direction_y * 2

        if self.dvd_logo.right >= self.layout.width or self.dvd_logo.x <= 0:
            self.direction_x *= -1
        if self.dvd_logo.top >= self.layout.height or self.dvd_logo.y <= 0:
            self.direction_y *= -1


if __name__ == "__main__":
    BouncingDVDApp().run()
