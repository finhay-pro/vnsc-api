import ssl
import paho.mqtt.client as mqtt
from stock_pb2 import StockPriceMessage
from google.protobuf import json_format

# Define the MQTT settings

class StockClient():


    def __init__(self, broker, port, username, password):
        self.broker = broker
        self.port = port
        self.username = username
        self.password = password

        # Define the callback function when connecting to the broker
        def on_connect(client, userdata, connect_flags, reason_code, properties):
            if reason_code == 0:
                print("Connected successfully")
            else:
                print(f"Connection failed with code {reason_code}")

        # Define the callback function when a message is received
        def on_message(client, userdata, msg):
            stock = StockPriceMessage()
            stock.ParseFromString(msg.payload)
            self.on_message(stock)

        # Create an MQTT client instance
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, transport='websockets')
        client.tls_set(cert_reqs=ssl.CERT_NONE)

        # Set the username and password
        client.username_pw_set(username, password)

        # Assign the callback functions
        client.on_connect = on_connect
        client.on_message = on_message

        self.client = client

    def subscribe(self, symbol):
        """
        Subscribe to a stock symbol, `symbol` can be:
        - `*`: all stocks
        - `list`: a list of stock symbols
        - `str`: a single stock symbol
        """
        if symbol == '*':
            self.client.subscribe(f'/stock-price/+')
        else:
            if type(symbol) is list:
                for s in symbol:
                    self.client.subscribe(f'/stock-price/{s}')
            else:
                self.client.subscribe(f'/stock-price/{symbol}')

    def unsubscribe(self, symbol):
        """
        Unsubscribe to a stock symbol, `symbol` can be:
        - `*`: all stocks
        - `list`: a list of stock symbols
        - `str`: a single stock symbol
        """
        if symbol == '*':
            self.client.unsubscribe(f'/stock-price/+')
        else:
            if type(symbol) is list:
                for s in symbol:
                    self.client.unsubscribe(f'/stock-price/{s}')
            else:
                self.client.unsubscribe(f'/stock-price/{symbol}')

    def connect(self):
        # Connect to the broker
        self.client.connect(self.broker, self.port)


    def loop_forever(self):
        self.client.loop_forever()


    def on_message(self, stock: StockPriceMessage):
        json_str = json_format.MessageToJson(stock)
        print(f"Received message: {json_str} for symbol {stock.symbol}")