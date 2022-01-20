#Subscriber
import paho.mqtt.client as paho
import time, ssl

uid = "vc-raspi823o2"

client = paho.Client(uid) #must be unique
topic = "/visitorcounter/cam"

#define callbacks
def on_connect(client, userdata, flags, rc):
    client.subscribe(topic, 0)
    
def on_message(client, userdata, message):
    # Process necessary logic.
    print("received message = ", str(message.payload.decode("utf-8")))

client.on_message = on_message
client.on_connect = on_connect

print("connecting to broker ...")
client.tls_set(cert_reqs = ssl.CERT_NONE)
client.tls_insecure_set(True)
client.connect("opendata.technikum-wien.at", 8883, 60)

#client.loop_forever()
client.loop_start()
# Endless loop wait to receive message(s).
print("connected - loop started")
time.sleep(10)
client.loop_stop()
client.disconnect()
print("END")