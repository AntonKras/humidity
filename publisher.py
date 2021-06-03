import paho.mqtt.client as mqtt  # import the client1
import time
from random import uniform
from queue import Queue


def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))

    print("message received ", str(message.payload.decode("utf-8")), flush=True)
    print("message topic=", message.topic, flush=True)
    q.put(data)

q = Queue()
client = mqtt.Client("Anton")  # создание клиента
print("Подключение к брокеру")
client.connect("127.0.0.1", 1883, 60)  # подключение к брокеру
client.loop_start()  # start the loop
print("Отправка сообщений в топик", "sensors")
while True:
    humidity_value = uniform(10.0, 70.0)    # создание рандомных значений влажности
    client.publish("sensors/humidity", humidity_value)    # отправка значений влажности в топик

    client.subscribe("humidifier")
    client.on_message = on_message
    time.sleep(4)