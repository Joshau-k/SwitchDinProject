
import time
import unittest

from unittest.mock import Mock, ANY
from NumberSubscriber import NumberSubscriber

from NumberPublisher import publish_number


class NumberGeneratorTest(unittest.TestCase):

    def test_subscribe(self):
        sub = NumberSubscriber()
        m = Mock()

        publish_number(37)

        sub.message_callback = m
        sub.print_subscribed_numbers(15)

        t = 0
        while m.called is False and t <= 15:
            time.sleep(1)
            t += 1

        m.assert_called_with(ANY, ANY, ANY)
        self.assertEqual('37', m.call_args.args[2].payload.decode("utf-8"))


if __name__ == '__main__':
    unittest.main()
