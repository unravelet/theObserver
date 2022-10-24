from Logger import Logger
from MqttSender import MqttSender

logger = Logger("Main")
logger.info("Start theObserver...")

mqttSender = MqttSender.loadConfigFromYamlFile('config.yaml')

######

mqttSender.send("Test")