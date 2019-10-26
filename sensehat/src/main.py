from threading import Thread
from flask import Flask, request
from sense_hat import SenseHat
from mqttclient import MqttClient

app = Flask(__name__)
sense = SenseHat()
try:
   mqtt = MqttClient('mqtt')
except:
   mqtt = None

def message(text):
   sense.set_rotation(180)
   red = (255, 0, 0)
   sense.show_message(text, text_colour=red)

currentMessageAsync=None
def messageAsync(text):
   currentMessageAsync = Thread(target=lambda self, *args: message(text), args=())
   currentMessageAsync.run()
   

@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/banner', methods=['GET', 'POST'])
def banner():
   try:
      text = request.get_json().get('message')
   except:
      text = "Unicorn!"

   messageAsync(text)
   return text

if __name__ == '__main__':
   if mqtt:
      mqtt.start()
   app.run(host='0.0.0.0', port=5000)
