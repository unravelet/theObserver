from log import logger
from mqtt import Mqtt

client = Mqtt.loadConfigFromYamlFile('config.yaml')

if __name__ == "__main__":
    client.send("Test")