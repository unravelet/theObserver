#Publisher
import paho.mqtt.client as paho
import time, ssl

uid = "vc-raspi823o2"

client = paho.Client(uid) #must be unique
topic = "/visitorcounter/cam"

print("connecting to broker ...")
# Easy going security for easy handling for presentation/using in PresentationLab.
client.tls_set(cert_reqs = ssl.CERT_NONE)
client.tls_insecure_set(True)
client.connect("opendata.technikum-wien.at", 8883, 60)

payload = "hello students" #payload must be a string, byte-array, int or float e.g. payload = random.randint(0,9)
client.publish(topic, payload)
print("data published")
client.loop_stop()
client.disconnect()
print("END")