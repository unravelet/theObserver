import ssl
import uuid
import yaml
import paho.mqtt.client as paho


class Mqtt:
    lastSend = ""

    def __init__(self, broker, port, topic):
        self.id = topic + "-" + str(uuid.uuid4())
        self.broker = broker
        self.port = port
        self.topic = topic

        self.client = paho.Client(client_id=self.id, userdata=None, protocol=paho.MQTTv5)
        self.client.tls_set(cert_reqs=ssl.CERT_NONE)
        self.client.tls_insecure_set(True)

        print(f"Connect to {self.broker}...")
        self.client.connect(self.broker, self.port, 60)
        print("Connected!")

    def send(self, text):
        if self.lastSend != text:
            self.lastSend = text
            self.client.publish(self.topic, text, qos=1)
            self.client.loop()

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect() 


if __name__ == "__main__":
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        client = Mqtt(config["mqtt_broker"], config["mqtt_port"], config["mqtt_topic"])
        client.send("test string")
