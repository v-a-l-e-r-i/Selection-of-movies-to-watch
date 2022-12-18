from main import get_info
import json
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

Window.maximize()
Window.clearcolor = (154/255, 184/255, 186/255, 1)


class CreateWidget(BoxLayout):
    name_btn = StringProperty()
    grade_btn = StringProperty()
    img_pos = StringProperty()


class ErrorButton(BoxLayout):
    pass


class Start(Screen):
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)

    def some_funct(self, name, grade, img):
        CreateWidget.name_btn = f"{name}"
        CreateWidget.grade_btn = f"{grade}"
        CreateWidget.img_pos = f"{img}"
        self.creatives = CreateWidget()
        self.ids.container.add_widget(self.creatives)

    def create_widget(self, u, g, f, m, i, inf):
        self.ids.container.clear_widgets()
        n = 0
        try:
            self.ids.container.cols = 3
            get_info(u, g, f, m, i, inf)
            sl = {}
            with open("file.json", 'r', encoding='utf-8') as file:
                sl = json.load(file)
                file.close()

            for key, value in sorted(sl.items(), key=lambda para: (para[1], para[0]), reverse=True):
                if float(value[0]) >= 5.5:
                    self.some_funct(key, value[0], value[1])
                else:
                    break
        except Exception as e:
            self.ids.container.cols = 1
            self.ids.container.add_widget(ErrorButton())


class MyApp(App):
    def build(self):
        return Start()


if __name__ == '__main__':
    MyApp().run()

