import logging
import time
import unittest

import NumberSubscriber
from NumberPublisher import generate_number, publish_number, Broker, Topic
import paho.mqtt.client as mqtt


class NumberGeneratorTest(unittest.TestCase):

    def test_randomNumber(self):
        num = generate_number()
        self.assertLessEqual(num, 100, "number is <= 100")
        self.assertGreaterEqual(num, 1, "number is >= 1")

    def test_manyRandomNumber(self):
        largest = 0
        smallest = 100
        for i in range(1, 10000):
            num = generate_number()
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num
        self.assertLessEqual(largest, 100, "largest generated num is <= 100")
        self.assertGreaterEqual(smallest, 1, "smallest generated num is >= 1")


    # def number_received(self, userdata, message):
    #     # return message.payload
    #     self.assertEqual(12, message.payload)
    #     # print("received message: ", str(message.payload.decode("utf-8")))


    # def test_publishNumber(self):
    #     client = mqtt.Client("NumberPrinter")
    #     client.connect(Broker)
    #     client.subscribe(Topic)
    #
    #     client.on_message = self.number_received
    #     publish_number(5)
    #     time.sleep(5)


if __name__ == '__main__':
    unittest.main()
