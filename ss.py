import http.client
import time
import sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from functools import partial

conn = http.client.HTTPSConnection("pet.porcupine.tv")

payload = "{\"action\":\"click\",\"amount\":3}"
headers = {
    'cookie': "__cfduid=d01093ad4bc404f7b4bfe29bce44827561532619609",
    'host': "pet.porcupine.tv",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-language': "en-US,en;q=0.5",
    'accept-encoding': "gzip, deflate, br",
    'referer': "https://0biqu5sb4f8fq6pxxg09xix27d0uo2.ext-twitch.tv/0biqu5sb4f8fq6pxxg09xix27d0uo2/2.2.0/84b076c36d1653b32972c7eef8c73e2c/viewer.html?anchor=component&language=en&mode=viewer&state=released&platform=web",
    'content-type': "application/json",
    'authorization': "I think not.",
    'content-length': "29",
    'origin': "https://0biqu5sb4f8fq6pxxg09xix27d0uo2.ext-twitch.tv",
    'dnt': "1",
    'connection': "keep-alive"
    }


class AuthScreen(GridLayout):
        def request(self, lab, dt):
                headers["authorization"] = self.auth.text
                conn.request("POST", "/channel/{}/message".format(self.chan.text), payload, headers)
                res = conn.getresponse()
                data = res.read()
                self.t = str("Points : "+ str(self.points))
                lab.text = self.t
                try:
                        print(self.points)
                        if data.decode("utf-8")[12] == "0" or data.decode("utf-8")[12] == "1" :
                                self.points = self.points + 30       
                except:
                        pass        

        def quit(self, btn):
                App.get_running_app().stop()                

        
        def __init__(self, **kwargs):
                super(AuthScreen, self).__init__(**kwargs)
                self.points = 0
                self.cols = 2
                self.add_widget(Label(text='Channel ID'))
                self.chan = TextInput(multiline=False)
                self.add_widget(self.chan)
                self.chan.text = "148072511"
                self.add_widget(Label(text='Auth'))
                self.auth = TextInput(multiline=False)
                self.add_widget(self.auth)
                self.auth.text = "Enter"
                self.res = Label(text='Points :', font_size=35)
                self.add_widget(self.res)
                self.btn1 = Button(text='Quit')
                self.btn1.bind(on_press=self.quit)
                self.add_widget(self.btn1)
                Clock.schedule_interval(partial(self.request, self.res), 1 / 200.)
        

class A_App_About_My_UncleApp(App):
        def build(self):
                return AuthScreen()

A_App_About_My_UncleApp().run()
        
print("Thank you for using this shit app!")