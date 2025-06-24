import websocket, json

class PriceFeed:
    def __init__(self, symbols):
        self.symbols = symbols
        self.prices = {}

    def _on_message(self, ws, msg):
        data = json.loads(msg)
        if 'tick' in data:
            self.prices[data['tick']['symbol']] = data['tick']['quote']

    def start(self):
        url = "wss://ws.derivws.com/websockets/v3?app_id=1089"
        ws = websocket.WebSocketApp(url, on_message=self._on_message)
        ws.run_forever()

    def get_prices(self):
        return self.prices.copy()
