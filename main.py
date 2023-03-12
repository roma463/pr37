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
from playsound import playsound

Builder.load_file('test.kv')
Window.size = (360, 800)


questions = ["Вам нравится быть в центре внимания?","Выберите украшение", "В вашем гардеробе больше всего вешей этого цвета",
            "какое качество больше всего подходит вам","Самая привлекательная для вас сфера деятельности", "как вы приводите совю фиуру в порядок",
            "Любимое десткое развлечение","каоке из человечских качеств вам кажется наиболее важным", "какой цвет вы выбираете",
            "Если бы вы стали катастрофой, чем бы вы стали после смерти","Во просите помощи во вселенной?", "Какое ваше любимое время года?",
            "какая погода может привести вас в восторг","как бы вы провели выходной", "на какой планете вы хотели бы побывать?",
            "любимый фрукт","какую социальную сеть ты виберешь?", "Твоя любимая газировка?",
            "ваш любимый движок","кто вы по типу темперамента?"]
questionsImage = ["17199-705-0.jpg","1590499068_21.jpg", "1637746724_1-gamerwall-pro-p-oboi-v-stile-kosmos-oboi-na-rabochii-stol-1.jpg",
                "1669943287_1-pibig-info-p-kosmicheskie-oboi-oboi-1.jpg","goblin.jpeg","kosmonavt_luna_otdyh_1920x1200-650x406-1.jpg",
                "756034651068899.jpg","Без названия.jpeg", "Без названия (3).jpeg",
                "Без названия (2).jpeg","Без названия (1).jpeg", "solnechnaia-sistema-vselennaia-galaktika-planety-zviozdy-2.jpg",
                "planeta-kosmos-asteroidov-oskolki.jpg","nBkSUhL2hFcinc-1Ib6BrNOp2Z3z8Zj21iDEh_fH_nKUPXuaDyXTjHou4MVO6BCVoZKf9GqVe5Q_CPawk214LyWK9G1N5ho=JEDAGaQ9GuUcjvj2-JHDCw.jpg", "kosmonavt_luna_otdyh_1920x1200-650x406-1.jpg",
                "12.png","goblin.jpeg", "start.jpeg"
                "12.png","goblin.jpeg"]

variants_otvet = [["11","12","13","14"],#1
                ["21","22","23","24"],#2
                ["31","32","33","34"],#3
                ["41","42","43","44"],#4
                ["","","",""],#5
                ["","","",""],#6
                ["","","",""],#7
                ["","","",""],#8
                ["","","",""],#9
                ["","","",""],#10
                ["","","",""],#11
                ["","","",""],#12
                ["","","",""],#13
                ["","","",""],#14
                ["","","",""],#15
                ["","","",""],#16
                ["","","",""],#17
                ["","","",""],#18
                ["","","",""],#19
                ["","","",""],]#20

summ = 0

class PongPaddle(Widget):
    pass
class TestWidget(Widget):
    def on_press(self,string):     
        global summ
        if(len(questions) != 0):
            playsound("audio_file.mp3")
            i = random.randrange(0,len(questions),1)
            img.source = (questionsImage[i])
            self.ids.input.text = questions[i]
            questionsImage.pop(i)
            questions.pop(i)
            summ = summ + int(string)
            
            arrayOtvet = variants_otvet[i]
            variants_otvet.pop(i)
            self.ids.button1.text = arrayOtvet[0]
            self.ids.button2.text = arrayOtvet[1]
            self.ids.button3.text = arrayOtvet[2]
            self.ids.button4.text = arrayOtvet[3]


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