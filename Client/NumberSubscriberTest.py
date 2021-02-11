import time
import unittest
from unittest.mock import Mock, ANY
from NumberSubscriber import NumberSubscriber
from NumberPublisher import publish_number


class NumberGeneratorTest(unittest.TestCase):

    def on_subscribe_test(self, client, userdata, mid, granted_qos):
        time.sleep(1)
        publish_number(37)

    def test_subscribe(self):
        sub = NumberSubscriber()
        m = Mock()

        sub.on_subscribe = self.on_subscribe_test
        sub.message_callback = m
        sub.print_subscribed_numbers(5)

        m.assert_called_with(ANY, ANY, ANY)
        self.assertEqual('37', m.call_args.args[2].payload.decode("utf-8"))


if __name__ == '__main__':
    unittest.main()
