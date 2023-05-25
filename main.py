import os
import time
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException

load_dotenv()
api_key = os.getenv('api_key')
secret_key = os.getenv('secret_key')

def main():
    client = Client(api_key=api_key, api_secret=secret_key)
    while True:
        try:
            price_now = client.futures_coin_symbol_ticker(pair='ETHUSD')[0].get('price')
            start_time = int((time.time()-3600)*1000)
            stop_time = int((time.time()-3480)*1000)
            price_hour_ago = client.futures_coin_index_price_klines(
                pair='ETHUSD', interval='1m',
                startTime=str(start_time), endTime=str(stop_time)
            )[0][1]
            procent = (abs(float(price_hour_ago) - float(price_now)))/float(price_hour_ago)
        except BinanceAPIException as error:
            print(error)
        else:
            if procent > 0.01:
                print('Подъем! Пора торговать!')
                time.sleep(60)
            time.sleep(1)

if __name__ == '__main__':
    main()