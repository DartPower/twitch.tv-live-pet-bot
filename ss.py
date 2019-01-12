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
import threading



class AuthScreen(GridLayout):
        def request(self, lab, runout, chan, aut):
                payload = "{\"action\":\"click\",\"amount\":3}"
                req_headers = {
                        'Content-Type': "application/json",
                        'authorization': "I think not.",
                }
                while True:
                        url = "https://pet.porcupine.tv/channel/{}/message".format(chan.text)
                        print(url)
                        data = requests.request("POST", url, data=payload, headers=req_headers).text
                        print(data)
                        lab.text =str("Points : "+ str(self.points))
                        try:
                                if data == "Unauthorized":
                                        runout.text = "Auth : Unauthorised"
                                        print(chan.text)
                                        code = requests.get(f"https://api.twitch.tv/v5/channels/{chan.text}/extensions", headers={"client-id": aut.text}).json()
                                        for i in code["tokens"]:
                                                if i["extension_id"] == "0biqu5sb4f8fq6pxxg09xix27d0uo2":
                                                        code = i["token"]
                                                        time.sleep(5)
                                                        break
                                        req_headers["authorization"] = f"Bearer {code}"
                                        print(req_headers)
                                elif data[12] == "0" or data[12] == "1":
                                        self.points = self.points + 30
                                        runout.text = "Auth : Authorised"
                        except IndexError:
                                runout.text = "Auth : Authorised"
                        except Exception:
                                pass
                        time.sleep(0.005)
                           

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
                self.auth.text = "E.g. sdakda232and... (you get the idea)"
                self.res = Label(text='Points :', font_size=35)
                self.add_widget(self.res)
                self.btn1 = Button(text='Quit')
                self.btn1.bind(on_press=self.quit)
                self.add_widget(self.btn1)
                self.thread = threading.Thread(target=partial(self.request, self.res, self.run, self.chan, self.auth), daemon=True)
                self.thread.start()

class An_App_About_My_UncleApp(App):
        def build(self):
                return AuthScreen()

An_App_About_My_UncleApp().run()

print("Thank you for using this app!")
