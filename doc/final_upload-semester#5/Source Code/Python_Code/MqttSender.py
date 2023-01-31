import ssl
import uuid
import yaml
import paho.mqtt.client as paho
from Logger import Logger

class MqttSender:
    lastSend: str = ""
    logger = Logger("MqttSender")

    def __init__(self, broker, port, topic):
        self.id = topic + "-" + str(uuid.uuid4())
        self.broker = broker
        self.port = port
        self.topic = topic

        self.client = paho.Client(client_id=self.id, userdata=None, protocol=paho.MQTTv5)
        self.client.tls_set(cert_reqs=ssl.CERT_NONE)
        self.client.tls_insecure_set(True)

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect

        self.connect()

    @classmethod
    def loadConfigFromYamlFile(cls, file: str):
        with open('config.yaml') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            return cls(config["mqtt_broker"], config["mqtt_port"], config["mqtt_topic"])

    def connect(self):
        self.logger.info(f"connect to {self.broker}:{self.port}")
        self.client.connect(self.broker, self.port, 60)

    def on_connect(self, client, userdata, flags, rc, a):
        self.logger.info(f"connected to {self.broker}:{self.port}")

    def on_disconnect(self, client, userdata, flags, rc, a):
        self.logger.info(f"disconnected from {self.broker}:{self.port}")
        self.connect()

    def send(self, text: str):
        if self.lastSend != text:
            self.lastSend = text
            self.logger.debug(f"sending message in topic {self.topic}: {text}")
            self.client.publish(self.topic, text, qos=1)
            self.client.loop()

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        self.logger.info(f"disconnected from {self.broker}:{self.port}")


    def subscribe(self):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        self.client.subscribe("theObserver", qos=1)
        self.client.on_message = on_message

if __name__ == "__main__":
    client = MqttSender.loadConfigFromYamlFile('config.yaml')
    client.send("Hello World!")