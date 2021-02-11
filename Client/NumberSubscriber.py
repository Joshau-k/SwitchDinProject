import argparse
import time

from config import Topic
from MQQTClientCreator import MQQTClientCreator


class NumberSubscriber:

    def on_subscribe(self, client, userdata, mid, granted_qos):
        pass

    def message_callback(self, client, userdata, message):
        self.print_number(str(message.payload.decode("utf-8")))

    def print_number(self, number):
        print("received message: ", number)

    def print_subscribed_numbers(self, timeout):
        client = MQQTClientCreator().create_connected_client("NumberPrinter")
        client.loop_start()
        client.on_subscribe = self.on_subscribe
        client.subscribe(Topic)
        client.message_callback_add(Topic, self.message_callback)
        time.sleep(timeout)
        client.loop_stop()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_arg', nargs='?', type=int, help='time (seconds) to listen for', default=10)
    args = parser.parse_args()
    NumberSubscriber().print_subscribed_numbers(args.first_arg)


if __name__ == '__main__':
    main()
