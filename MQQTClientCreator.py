import paho.mqtt.client as mqtt
import time

Broker = "mqtt.eclipseprojects.io"
BrokerPort = 1883


class MQQTClientCreator:
    def on_connect(self, client, userdata, flags, reasoncode, properties=None):
        print("Connected With Result Code ", reasoncode)

    def create_connected_client(self, clientid):
        new_client = mqtt.Client(clientid)
        new_client.on_connect = self.on_connect  # on_connect
        new_client.connect(Broker, BrokerPort)
        return new_client
