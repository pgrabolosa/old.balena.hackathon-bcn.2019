import paho.mqtt.client as mqtt
import json
from sense import messageAsync, sense

currentApp = None
knownApps = []

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("MQTT - Connected with result code "+str(rc))
    print("MQTT - Will subscribe to "+str(rc))
    client.subscribe("disp/#")
    client.subscribe("raw/joystick")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
   if msg.topic.startswith('disp/'):
      display(msg)
   elif msg.topic == 'raw/joystick':
      switchapp(str(msg.payload.decode("utf-8","ignore")))

def switchapp(direction):
   global currentApp
   oldApp = currentApp
   if direction in ['up', 'right']:
      currentApp = 0 if currentApp is None else ((currentApp+1)%len(knownApps))
   elif direction in ['down', 'left']:
      currentApp = 0 if currentApp is None else ((currentApp-1+len(knownApps))%len(knownApps))
   print("Switched apps from", oldApp, "to", currentApp)

def display(msg):
   senderName = msg.topic[len('disp/'):]
   print("Received display message from", senderName)
   
   if senderName not in knownApps:
      knownApps.append(senderName)
      print("Updated known apps to", knownApps)
   
   if currentApp is not None and senderName != knownApps[currentApp]:
      print("Ignoring call from", senderName)
      return #ignore call
   
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
      client.loop_forever()
