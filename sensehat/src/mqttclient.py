import paho.mqtt.client as mqtt
from sense import messageAsync

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("MQTT - Connected with result code "+str(rc))
    print("MQTT - Will subscribe to "+str(rc))
    client.subscribe("disp/#")
    client.subscribe("raw/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
   if msg.topic.startswith('disp/'):
      should_display(msg)
   elif msg.topic.startswith('raw/'):
      should_process(msg)

def should_display(disp_msg):
   messageAsync("Should Display")
   
def should_process(raw_msg):
   messageAsync("Should Process")

class MqttClient:
   def __init__(self, servername):
      self.client = mqtt.Client()
      self.client.on_connect = on_connect
      self.client.on_message = on_message

      self.client.connect(servername, 1883, 60)
   
   def start(self):
      print("MQTT - Starting mqtt loop")
      self.client.loop_start()