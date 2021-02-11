import argparse
import random

from config import Topic
from MQQTClientCreator import MQQTClientCreator


def generate_number():
    return random.randint(1, 100)


def publish_number(num):
    client = MQQTClientCreator().create_connected_client("NumberGenerator")
    client.publish(Topic, num)
    print(f"Published {str(num)} to topic '{Topic}'")


def publish_rand_number():
    num = generate_number()
    publish_number(num)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_arg', nargs='?', type=int, help='number to publish (random 1-100 chosen if not supplied)', default=None)
    args = parser.parse_args()
    if args.first_arg is None:
        publish_rand_number()
    else:
        publish_number(args.first_arg)


if __name__ == '__main__':
    main()
