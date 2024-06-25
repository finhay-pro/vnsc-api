from price import StockClient
import os
import time
import threading


class MyClient(StockClient):

    def on_message(self, stock):
        # If you don't override this method, there is a default implementation
        # that will print json format of the stock message
        print(stock.symbol, stock.price)


if __name__ == "__main__":
    broker = 'emqx.vinasecurities.com'
    port = 8084
    username = os.environ['MQTT_USERNAME']
    password = os.environ['MQTT_PASSWORD']
    client = MyClient(broker, port, username, password)
    client.connect()
    client.subscribe(['VND', 'VRE'])
    client.loop_forever()

