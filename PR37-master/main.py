from kivy.config import Config
Config.set("graphics", "resizable", 0)
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import random
from kivy.uix.image import Image
from kivy.graphics import Color, Line, Rectangle
import re

Builder.load_file('test.kv')
Window.size = (360, 800)

questions = ["вопhujik","вопрос 2", "вопрос 3"]
questionsImage = ["12.png","goblin.jpeg", "start.jpeg"]

summ = 0

class PongPaddle(Widget):
    pass
class TestWidget(Widget):
    def on_press(self,string):     
        global summ
        if(len(questions) != 0):
            i = random.randrange(0,len(questions),1)
            img.source = (questionsImage[i])
            self.ids.input.text = questions[i]
            questionsImage.remove(questionsImage[i])
            questions.remove(questions[i])
            summ = summ + int(string)
            print(summ)
        else:
            if(summ > 0 or summ < 3):
                self.ids.input.text = "1"
            elif(summ >= 15 or summ < 30):
                self.ids.input.text = "2"
            elif(summ >= 30 or summ < 45):
                self.ids.input.text = "3"
            elif(summ >= 45 or summ < 60):
                self.ids.input.text = "4"

class TestApp(App):
    def build(self):
        global img 
        a = TestWidget()
        img = Image(source = r"goblin.jpeg", pos=(80, 600), size= (200, 200))
        a.add_widget(img)
        return a

if __name__ == "__main__":
    TestApp().run()