from threading import Thread
from flask import Flask, request
from mqttclient import MqttClient
from sense import messageAsync

app = Flask(__name__)
try:
   print("MQTT - Trying to connect")
   mqtt = MqttClient('mosquitto')
except:
   print("MQTT - Failed to connect")
   mqtt = None

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
