import time
import unittest
from unittest.mock import Mock, ANY

from MQQTClientCreator import MQQTClientCreator


class MQQTClientCreatorTest(unittest.TestCase):

    def test_create_connected_client(self):
        cc = MQQTClientCreator()
        m = Mock()
        cc.on_connect = m
        client = cc.create_connected_client("NumberPrinter")
        try:
            client.loop_start()
            time.sleep(5)
            m.assert_called_with(ANY, ANY, ANY, 0)
        finally:
            client.loop_stop()


if __name__ == '__main__':
    unittest.main()
