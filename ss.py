import requests
import time
import sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from functools import partial

payload = "{\"action\":\"click\",\"amount\":3}"
headers = {
    'host': "pet.porcupine.tv",
    'user-agent': "python script | https://github.com/Hitsounds/twitch.tv-live-pet-bot | marvelrenju1@gmail.com",
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
        def request(self, lab, runout, dt):
                headers["authorization"] = self.auth.text
                url = "https://pet.porcupine.tv/channel/{}/message".format(self.chan.text)
                res = requests.request("POST", url, data=payload, headers=headers)
                data = res.text
                self.t = str("Points : "+ str(self.points))
                lab.text = self.t
                try:
                        if data[12] == "0" or data[12] == "1" :
                                self.points = self.points + 30
                                runout.text = "Auth : Authorised"
                        elif data == "Unauthorized":
                                runout.text = "Auth : Unauthorised"
                except IndexError:
                        runout.text = "Auth : Authorised"
                           

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
                self.run = Label(text='Auth : Unauthorised')
                self.add_widget(self.run)    
                self.auth = TextInput(multiline=True)
                self.add_widget(self.auth)
                self.auth.text = "E.g. Bearer sdasds231as..."
                self.res = Label(text='Points :', font_size=35)
                self.add_widget(self.res)
                self.btn1 = Button(text='Quit')
                self.btn1.bind(on_press=self.quit)
                self.add_widget(self.btn1)
                Clock.schedule_interval(partial(self.request, self.res, self.run), 1.0 / 200.0)


class A_App_About_My_UncleApp(App):
        def build(self):
                return AuthScreen()

A_App_About_My_UncleApp().run()

print("Thank you for using this app!")
