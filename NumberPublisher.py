import paho.mqtt.client as mqtt
import random

from MQQTClientCreator import MQQTClientCreator

Broker = "mqtt.eclipseprojects.io"
BrokerPort = 1883
Topic = "Number23847923"


def generate_number():
    return random.randint(1, 100)


def publish_number(num):
    client = MQQTClientCreator().create_connected_client("NumberGenerator")
    client.connect(Broker, BrokerPort)

    client.publish(Topic, num)
    print(f"Published {str(num)} to topic '{Topic}'")


def publish_rand_number():
    num = generate_number()
    publish_number(num)