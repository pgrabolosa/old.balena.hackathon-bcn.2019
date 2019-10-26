from threading import Thread
from sense_hat import SenseHat
from mqttclient import MqttClient

TOPIC='raw/joystick'

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
      event = sense.wait_for_event()
      if action == "pressed":
         mqtt.client.publish(TOPIC, event.direction)