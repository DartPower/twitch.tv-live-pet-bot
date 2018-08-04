import http.client
import time
import sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


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

print("ss")

class AuthScreen(GridLayout):

        def __init__(self, **kwargs):
                super(AuthScreen, self).__init__(**kwargs)
                self.cols = 2
                self.add_widget(Label(text='Channel ID'))
                self.chan = TextInput(multiline=False)
                self.add_widget(self.chan)
                self.chan.text = "148072511"
                self.add_widget(Label(text='Auth'))
                self.auth = TextInput(multiline=False)
                self.add_widget(self.auth)
                self.auth.text = "Enter"



#class resultsscreen(BoxLayout):
#        def __init__(self, **kwargs):
 #               super(resultsscreen, self).__init__(**kwargs)
  #              self.add_widget(Label(text='Points: ', points))        
                


l = AuthScreen()                



class A_App_About_My_UncleApp(App):
        def build(self):
                return l

A_App_About_My_UncleApp().run()
        


headers["authorization"] = l.auth.text
i = 0.005
points = 0                
while True:
        time.sleep(i)
        conn.request("POST", "/channel/{}/message".format(l.chan.text), payload, headers)
        res = conn.getresponse()
        data = res.read()
        try:
                print(points)
                if data.decode("utf-8")[12] == "0" or data.decode("utf-8")[12] == "1" :
                        points = points + 30
                
        except:
                pass

           

        
        
