from flask import Flask, request
from sense_hat import SenseHat
from mqttclient import MqttClient

app = Flask(__name__)
sense = SenseHat()
mqtt = MqttClient()


def message(text):
   sense.set_rotation(180)
   red = (255, 0, 0)
   sense.show_message(text, text_colour=red)


@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/banner', methods=['GET', 'POST'])
def banner():
   try:
      text = request.get_json().get('message')
   except:
      text = "Unicorn!"

   message(text)
   return text

if __name__ == '__main__':
   mqtt.start()
   app.run(host='0.0.0.0', port=5000)
