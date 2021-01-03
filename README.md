# trading-bot
The repository consist of binanace trading bots. There are two types of bot
1. Kline trading bot
2. 3 way arbitrage bot 

## Installation requirement
* Python 3+
* Pipenv
* Postgres (Not required if using sqlite)
## Kline trading bot: Bot that trades based on Kline pattern with option to train and use ML for trade decision
### how to run
#### Task
The task for the sample configuration is as follows
* Use sqlite database for simplicity and not to run extra db server
* Kline pattern selected to put market buy order are Bullish_Harami, Bullish_Engulfing, Piercing_Line_bullish, Hanging_Man_bullish
* profit_rate = 0.45% (Start considering Sell order when current market price exceeds 0.45% up of the buy price )
* stop_loss = 0.35% (Put a Sell order when current market price exceeds 0.35 down of the buy price in order to avoid further loss)
* stop_profit_rate = 0.15% ( Put a sell order at 0.15 percent down of profit rate ) A strategy to dynamically update the profit limit price on bullish engulfing. Set to 0 to sell at fixed profit rate
* principle_amount = 100 (Use 100 dollar at one trade)
* {"asset":"BTC", "exchange":"BTCUSDT", "min_limit":"0.005"} (Check BTC kline candle for trading (15 min order book used))

#### Steps
1. Make sure python and pipenv is installed
2. For above sample task, set configs/config.py as follows

```
import os

db_url = os.environ['PSQL_DB_HOST'] + ':5432/' + os.environ['PSQL_BINBOT_DB_NAME']

config = {
    "reset_db":False,
    "start_bot":True,
    "mock_trade":False,    
    "db":{
        "db_type":"sqlite",
        "file":"data.db",
        "db_url": db_url,
        "db_username": os.environ['PSQL_BINBOT_DB_USER'],
        "db_password": os.environ['PSQL_BINBOT_DB_PWD'],    
    },
    "api_key":os.environ["BI_KEY"],
    "api_secret":os.environ["BI_SEC"],
    "crypto_list":[
        {"asset":"BTC", "exchange":"BTCUSDT", "min_limit":"0.005"}
    ],
    "stop_loss":0.0035,
    "profit_rate":0.0045,
    "stop_profit_rate":0.0015,
    "stop_script":0,
    "principle_amount":100,
    "day_start_amount":10000,
    "root_asset": "USDT",
    "bot_freqency":6,
    "profit_sleep": 150,
    "loss_sleep": 300,
    "error_sleep":11,
    "bot_permit": {
        "check_permit":True,
        "daily_loss_margin": -0.02,
        "daily_profit_margin": 0.01,
        "daily_profit_stop_margin": 0.25,
        "validate_candlestick":True,
        "invalid_candlestick_sleep":20,
        "reject_candles": {
            "doji": True,
            "evening_star": True,
            "morning_star": True,
            "shooting_Star_bearish": True,
            "shooting_Star_bullish": True,
            "hammer": True,
            "inverted_hammer": True,
            "bearish_harami": True,
            "Bullish_Harami": False,
            "Bearish_Engulfing": True,
            "Bullish_Engulfing": False,
            "bullish_reversal": True,
            "bearish_reversal": True,
            "Piercing_Line_bullish": False,
            "Hanging_Man_bearish": True,
            "Hanging_Man_bullish": False,
            "Unidentified": True,
            "Last_2_Negetives":True
        }
    },
}
```
3. From project root run ```pipenv run python script.py ```


## 3 way arbitrage bot: 3 way trading rate based arbitrage bot
### how to run
```pipenv run python arbi_script.py```
TODO: Step and config Details
