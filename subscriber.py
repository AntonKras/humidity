import paho.mqtt.client as mqtt
import time
from influxdb import InfluxDBClient
from queue import Queue

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))

    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    q.put(data)


q = Queue()
time.sleep(25)
client_2 = mqtt.Client("Anton_2")
client_2.on_message = on_message
client_2.connect("127.0.0.1", 1883, 60)  # подключение к брокеру
client_2.loop_start()
print('Подключен')
client_2.subscribe('sensors/humidity')
while True:
    time.sleep(4)
    client_2.on_message = on_message
    while not q.empty():

        message = q.get()
        if message is None:
            continue
        value = float(message)
        if value < 30:
            client_2.publish("humidifier", 'ON')
        elif value > 60:
            client_2.publish("humidifier", 'OFF')
        print("received from queue", message)
    time.sleep(4)  # wait