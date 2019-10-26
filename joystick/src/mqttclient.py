import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("MQTT - Connected with result code "+str(rc))
    print("MQTT - Will subscribe to "+str(rc))
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

class MqttClient:
   def __init__(self, servername):
      self.client = mqtt.Client()
      self.client.on_connect = on_connect
      self.client.on_message = on_message

      self.client.connect(servername, 1883, 60)
   
   def start(self):
      print("MQTT - Starting mqtt loop")
      self.client.loop_start()