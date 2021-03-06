import joblib

def createNumericCandleDict(order, c0, c1, c2, c3, c4):
    new_dict = {}
    new_dict["c0_Open"] = c0.Open
    new_dict["c0_High"] = c0.High
    new_dict["c0_Low"] = c0.Low
    new_dict["c0_Close"] = c0.Close
    new_dict["c0_Volume"] = c0.Volume
    new_dict["c0_Quote_Asset_Volume"] = c0.Quote_Asset_Volume
    new_dict["c0_Number_Of_Trades"] = c0.Number_Of_Trades
    new_dict["c0_Taker_Buy_Base_Asset_Volume"] = c0.Taker_Buy_Base_Asset_Volume
    new_dict["c0_Taker_Buy_Quote_Asset_Volume"] = c0.Taker_Buy_Quote_Asset_Volume

    new_dict["c1_Open"] = c1.Open
    new_dict["c1_High"] = c1.High
    new_dict["c1_Low"] = c1.Low
    new_dict["c1_Close"] = c1.Close
    new_dict["c1_Volume"] = c1.Volume
    new_dict["c1_Quote_Asset_Volume"] = c1.Quote_Asset_Volume
    new_dict["c1_Number_Of_Trades"] = c1.Number_Of_Trades
    new_dict["c1_Taker_Buy_Base_Asset_Volume"] = c1.Taker_Buy_Base_Asset_Volume
    new_dict["c1_Taker_Buy_Quote_Asset_Volume"] = c1.Taker_Buy_Quote_Asset_Volume

    new_dict["c2_Open"] = c2.Open
    new_dict["c2_High"] = c2.High
    new_dict["c2_Low"] = c2.Low
    new_dict["c2_Close"] = c2.Close
    new_dict["c2_Volume"] = c2.Volume
    new_dict["c2_Quote_Asset_Volume"] = c2.Quote_Asset_Volume
    new_dict["c2_Number_Of_Trades"] = c2.Number_Of_Trades
    new_dict["c2_Taker_Buy_Base_Asset_Volume"] = c2.Taker_Buy_Base_Asset_Volume
    new_dict["c2_Taker_Buy_Quote_Asset_Volume"] = c2.Taker_Buy_Quote_Asset_Volume 

    new_dict["c3_Open"] = c3.Open
    new_dict["c3_High"] = c3.High
    new_dict["c3_Low"] = c3.Low
    new_dict["c3_Close"] = c3.Close
    new_dict["c3_Volume"] = c3.Volume
    new_dict["c3_Quote_Asset_Volume"] = c3.Quote_Asset_Volume
    new_dict["c3_Number_Of_Trades"] = c3.Number_Of_Trades
    new_dict["c3_Taker_Buy_Base_Asset_Volume"] = c3.Taker_Buy_Base_Asset_Volume
    new_dict["c3_Taker_Buy_Quote_Asset_Volume"] = c3.Taker_Buy_Quote_Asset_Volume   

    new_dict["c4_Open"] = c4.Open
    new_dict["c4_High"] = c4.High
    new_dict["c4_Low"] = c4.Low
    new_dict["c4_Close"] = c4.Close
    new_dict["c4_Volume"] = c4.Volume
    new_dict["c4_Quote_Asset_Volume"] = c4.Quote_Asset_Volume
    new_dict["c4_Number_Of_Trades"] = c4.Number_Of_Trades
    new_dict["c4_Taker_Buy_Base_Asset_Volume"] = c4.Taker_Buy_Base_Asset_Volume
    new_dict["c4_Taker_Buy_Quote_Asset_Volume"] = c4.Taker_Buy_Quote_Asset_Volume 

    """
    if order != None:
      marker_sell_price = order.marker_sell_price
      price = order.price
      profit = (marker_sell_price - price)/price
      new_dict["profit"] = profit
      profit_flag = 1 if profit > 0 else 0
      new_dict["profit_flag"] = profit_flag
    """
    if order != None:
      net_sold = float(order.sold_cummulative_quote_qty) * 0.9995
      net_buy = float(order.buy_cummulative_quote_qty) * 1.0005
      profit = (net_sold - net_buy)/ net_buy
      new_dict["profit"] = profit
      profit_flag = 1 if profit > 0 else 0
      new_dict["profit_flag"] = profit_flag

    return new_dict


def createCategoricCandleList(item):
    new_dict = {}
    new_dict["candle_pattern0"] = item.candle_pattern0
    new_dict["candle_pattern1"] = item.candle_pattern1
    new_dict["candle_pattern2"] = item.candle_pattern2
    new_dict["candle_pattern3"] = item.candle_pattern3
    new_dict["candle_pattern4"] = item.candle_pattern4

    """
    marker_sell_price = item.marker_sell_price
    price = item.price
    profit = (marker_sell_price - price)/price
    new_dict["profit"] = profit
    profit_flag = 1 if profit > 0 else 0
    new_dict["profit_flag"] = profit_flag
    """

    net_sold = float(item.sold_cummulative_quote_qty) * 0.9995
    net_buy = float(item.buy_cummulative_quote_qty) * 1.0005
    profit = (net_sold - net_buy)/ net_buy
    new_dict["profit"] = profit
    profit_flag = 1 if profit > 0 else 0
    new_dict["profit_flag"] = profit_flag

    return new_dict

def saveObject(obj, obj_file):
  with open(obj_file, 'wb') as f:
    joblib.dump(obj, f, compress=9)


def loadObject(obj_file):
  with open(obj_file, 'rb') as f:
    obj = joblib.load(f)

  return obj

def createNumericCandleDictFromDict(c0, c1, c2, c3, c4):
    new_dict = {}
    new_dict["c0_Open"] = c0.get("Open")
    new_dict["c0_High"] = c0.get("High")
    new_dict["c0_Low"] = c0.get("Low")
    new_dict["c0_Close"] = c0.get("Close")
    new_dict["c0_Volume"] = c0.get("Volume")
    new_dict["c0_Quote_Asset_Volume"] = c0.get("Quote_Asset_Volume")
    new_dict["c0_Number_Of_Trades"] = c0.get("Number_Of_Trades")
    new_dict["c0_Taker_Buy_Base_Asset_Volume"] = c0.get("Taker_Buy_Base_Asset_Volume")
    new_dict["c0_Taker_Buy_Quote_Asset_Volume"] = c0.get("Taker_Buy_Quote_Asset_Volume")

    new_dict["c1_Open"] = c1.get("Open")
    new_dict["c1_High"] = c1.get("High")
    new_dict["c1_Low"] = c1.get("Low")
    new_dict["c1_Close"] = c1.get("Close")
    new_dict["c1_Volume"] = c1.get("Volume")
    new_dict["c1_Quote_Asset_Volume"] = c1.get("Quote_Asset_Volume")
    new_dict["c1_Number_Of_Trades"] = c1.get("Number_Of_Trades")
    new_dict["c1_Taker_Buy_Base_Asset_Volume"] = c1.get("Taker_Buy_Base_Asset_Volume")
    new_dict["c1_Taker_Buy_Quote_Asset_Volume"] = c1.get("Taker_Buy_Quote_Asset_Volume")

    new_dict["c2_Open"] = c2.get("Open")
    new_dict["c2_High"] = c2.get("High")
    new_dict["c2_Low"] = c2.get("Low")
    new_dict["c2_Close"] = c2.get("Close")
    new_dict["c2_Volume"] = c2.get("Volume")
    new_dict["c2_Quote_Asset_Volume"] = c2.get("Quote_Asset_Volume")
    new_dict["c2_Number_Of_Trades"] = c2.get("Number_Of_Trades")
    new_dict["c2_Taker_Buy_Base_Asset_Volume"] = c2.get("Taker_Buy_Base_Asset_Volume")
    new_dict["c2_Taker_Buy_Quote_Asset_Volume"] = c2.get("Taker_Buy_Quote_Asset_Volume") 

    new_dict["c3_Open"] = c3.get("Open")
    new_dict["c3_High"] = c3.get("High")
    new_dict["c3_Low"] = c3.get("Low")
    new_dict["c3_Close"] = c3.get("Close")
    new_dict["c3_Volume"] = c3.get("Volume")
    new_dict["c3_Quote_Asset_Volume"] = c3.get("Quote_Asset_Volume")
    new_dict["c3_Number_Of_Trades"] = c3.get("Number_Of_Trades")
    new_dict["c3_Taker_Buy_Base_Asset_Volume"] = c3.get("Taker_Buy_Base_Asset_Volume")
    new_dict["c3_Taker_Buy_Quote_Asset_Volume"] = c3.get("Taker_Buy_Quote_Asset_Volume")   

    new_dict["c4_Open"] = c4.get("Open")
    new_dict["c4_High"] = c4.get("High")
    new_dict["c4_Low"] = c4.get("Low")
    new_dict["c4_Close"] = c4.get("Close")
    new_dict["c4_Volume"] = c4.get("Volume")
    new_dict["c4_Quote_Asset_Volume"] = c4.get("Quote_Asset_Volume")
    new_dict["c4_Number_Of_Trades"] = c4.get("Number_Of_Trades")
    new_dict["c4_Taker_Buy_Base_Asset_Volume"] = c4.get("Taker_Buy_Base_Asset_Volume")
    new_dict["c4_Taker_Buy_Quote_Asset_Volume"] = c4.get("Taker_Buy_Quote_Asset_Volume") 

    return new_dict