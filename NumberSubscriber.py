import paho.mqtt.client as mqtt
import time

from MQQTClientCreator import MQQTClientCreator


class NumberSubscriber:
    Topic = "Number23847923"


    def on_connect(self, client, userdata, flags, reasonCode, properties=None):
        print("Connected With Result Code ", reasonCode)

    def message_callback(self, client, userdata, message):
        self.print_number(str(message.payload.decode("utf-8")))

    def print_number(self, number):
        print("received message: ", number)

    def print_subscribed_numbers(self, timeout):
        # def subscribe_numbers():
        client = MQQTClientCreator().create_connected_client("NumberPrinter")
        client.loop_start()
        client.subscribe(self.Topic)
        client.message_callback_add(self.Topic, self.message_callback)
        time.sleep(timeout)
        client.loop_stop()
        # client.loop_forever()

        # subscribe_numbers()
