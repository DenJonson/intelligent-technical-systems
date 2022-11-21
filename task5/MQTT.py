import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
  print("Connected with result code {O}".format(str(rc)))
  client.subscribe("digitest/test1")
  
def on_message(client, userdata, msg):
  print("Massage received-> " + msg.topic + " " + str(msg.payload))
  
client = mqtt.Client("digi_mqtt_test")
client.on_connect = on_connect
client.on_message = on_message

client.connect('127.0.0.1', 17300)
client.loop_forever()