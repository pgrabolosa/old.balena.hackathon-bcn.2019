from threading import Thread
from sense_hat import SenseHat
sense = SenseHat()

def message(text):
   sense.set_rotation(180)
   red = (255, 0, 0)
   sense.show_message(text, text_colour=red)

currentMessageAsync=None
def messageAsync(text):
   currentMessageAsync = Thread(target=lambda *args: message(text), args=())
   currentMessageAsync.start()