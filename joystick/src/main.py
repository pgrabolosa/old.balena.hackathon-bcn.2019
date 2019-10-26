from threading import Thread
from sense_hat import SenseHat
from mqttclient import MqttClient
import json

TOPIC='raw/joystick'
R = [255,0,0]
O = [255,127,0]
Y = [255,255,0]
G = [0,255,0]
B = [0,0,255]
N = [0,0,0]

sense = SenseHat()
try:
   print("MQTT - Trying to connect")
   mqtt = MqttClient('mosquitto')
except:
   print("MQTT - Failed to connect")
   mqtt = None

if __name__ == '__main__':
   if mqtt:
      mqtt.start()
   
   while True:
      event = sense.stick.wait_for_event()
      if mqtt is not None and event.action == "pressed":
         print("Event " + event.direction)
         mqtt.client.publish(TOPIC, event.direction)
         if event.direction == "middle":
            mqtt.client.publish("disp/button", json.dumps({"image":
[N, N, N, B, B, N, N, N,
N, N, B, B, B, B, N, N,
N, B, B, B, B, B, B, N,
O, O, B, B, B, B, Y, Y,
O, O, O, B, B, Y, Y, Y,
N, O, O, O, Y, Y, Y, N,
N, N, O, O, Y, Y, N, N,
N, N, N, O, Y, N, N, N]}))
