from threading import Thread
from sense_hat import SenseHat
from mqttclient import MqttClient
from time import sleep
import json

RAW_TOPIC='raw/temperature'
DISP_TOPIC='disp/temperature'

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
      sleep(15)
      if mqtt is not None:
         mqtt.client.publish(RAW_TOPIC, json.dumps({
            "humidity": sense.get_humidity(),
            "temperature": sense.get_temperature(),
            "pressure": sense.get_pressure()
         }))
         mqtt.client.publish(DISP_TOPIC, json.dumps({
            "text": "T%d" % (int(sense.get_temperature()))
         }))
