from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader


Config.set('graphics', 'resizable', 0)
res, q = 0, 0
sound = SoundLoader.load('Medianoche.mp3')

def radio(con):
    global sound
    print (sound)
    if con == True:
        if sound:
            sound.play()         
    elif con == False:
        if sound:
            sound.stop()
        

class BoxApp(App):

    def build(self):
        root_widget = BoxLayout()#orientation='horizontal')
        #   button_radio = AnchorLayout(anchor_x = 'left', anchor_y = 'top', size_hint = [None, None], size = [300,200])
        bt_for_radio = AnchorLayout(anchor_x = 'left', anchor_y = 'top', size_hint = [.5, .5])
        
        bt_radio = Button(text = 'Радио', on_press = self.btn_radio)
        bt_for_radio.add_widget(bt_radio)

        bt_for_call = AnchorLayout(anchor_x = 'right', anchor_y = 'top', size_hint = [.5, .5])
        bt_call = Button(text = 'Звонки', on_press = self.btn_call) #anchor_x = 'right', anchor_y = 'top', size_hint = [0.2, 0.2]
        bt_for_call.add_widget (bt_call)

        root_widget.add_widget (bt_for_call)
        root_widget.add_widget (bt_for_radio)

        return root_widget


    def btn_radio(self, instance):
        global res, q
        res += 1
        q += 1  

        if res == 1 and q == 1:
            print (2)
            res, q = -1, -1
            con = True
            radio(con)
        else:
            print(1111)
            res, q = 0, 0
            con = False
            radio(con)

    def btn_call(self, instance):
        pass
        #должны получить список кому можно позвонить и так же надо распозновать речь и воспроизводжить 

def get_words():
    pass 


BoxApp().run()