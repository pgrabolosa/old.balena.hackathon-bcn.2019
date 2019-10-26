import paho.mqtt.client as mqtt
import json
from sense import messageAsync, sense

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("MQTT - Connected with result code "+str(rc))
    print("MQTT - Will subscribe to "+str(rc))
    client.subscribe("disp/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
   try:
      msgDecoded=str(msg.payload.decode("utf-8","ignore"))
      msgRoot = json.loads(msgDecoded)
      if type(msgRoot) is not dict:
         raise AttributeError("Not JSON")
   except:
      print("Bad format for topic disp/#")
      return # ignore it
   
   if 'color' in msgRoot:
      sense.clear(msgRoot['color'])
   elif 'image' in msgRoot:
      sense.set_pixels(msgRoot['image'])
   elif 'text' in msgRoot:
      messageAsync(msgRoot['text'])
   else:
      print("Unexpected format for topic disp/#")

def should_display(disp_msg):
   messageAsync("Should Display")
   
def should_process(raw_msg):
   messageAsync("Should Process")


if __name__ == '__main__':
      client = mqtt.Client()
      client.on_connect = on_connect
      client.on_message = on_message

      client.connect('mosquitto', 1883, 60)
      self.client.loop_forever()
