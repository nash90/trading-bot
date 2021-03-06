from sqlalchemy import Column, String, Boolean, Numeric, Integer, BigInteger, Date, Table, ForeignKey, DateTime, Sequence
from models.base import Base
from datetime import datetime
#from sqlalchemy.orm import relationship

class Order(Base):
  __tablename__ = 'orders'
  __table_args__ = {'extend_existing': True}
  id = Column('id', BigInteger, primary_key=True)
  order_id = Column('order_id', BigInteger)
  client_order_id = Column('client_order_id', String(50), default="")
  transact_time = Column('transact_time', BigInteger)
  created_date = Column(DateTime, default=datetime.now())
  server_side_status = Column('server_side_status', String(10), default="")
  symbol = Column('symbol', String(10), default="")
  type = Column('type', String(50), default="")
  side = Column('side', String(50), default="")
  average = Column('average', Numeric)
  price = Column('price', Numeric)
  stop_price = Column('stop_price', Numeric)
  stop_limit_price = Column('stop_limit_price', Numeric)
  executed_quantity = Column('executed_quantity', Numeric)
  orig_quantity = Column('orig_quantity', Numeric)
  buy_cummulative_quote_qty = Column('buy_cummulative_quote_qty', Numeric)
  sold_cummulative_quote_qty = Column('sold_cummulative_quote_qty', Numeric)
  total = Column('total', Numeric)
  profit_sale_txn_id = Column('profit_sale_txn_id', String(50), default="")
  profit_sale_stop_loss_price = Column('profit_sale_stop_loss_price', Numeric)
  market_sell_txn_id = Column('market_sell_txn_id', String(50), default="")
  marker_sell_price = Column('marker_sell_price', Numeric)
  bought_flag = Column('bought_flag', Boolean, default=False)
  sold_flag = Column('sold_flag', Boolean, default=False)
  profit_sale_process_flag = Column('profit_sale_process_flag', Boolean, default=False)
  all_prices = Column('all_prices', String(200), default="")
  fills = Column('fills', String(500), default="")
  logs = Column('logs', String(2000), default="")
  candle_pattern0 = Column('candle_pattern0', String(500), default="")
  candle_pattern1 = Column('candle_pattern1', String(500), default="")
  candle_pattern2 = Column('candle_pattern2', String(500), default="")
  candle_pattern3 = Column('candle_pattern3', String(500), default="")
  candle_pattern4 = Column('candle_pattern4', String(500), default="")
  candle0 = Column('candle0', BigInteger)
  candle1 = Column('candle1', BigInteger)
  candle2 = Column('candle2', BigInteger)
  candle3 = Column('candle3', BigInteger)
  candle4 = Column('candle4', BigInteger)

class DailyConfig(Base):
  __tablename__ = 'daily_config'
  __table_args__ = {'extend_existing': True}
  id = Column('id', BigInteger, primary_key=True)
  trade_date =  Column(Date)
  daily_profit_limit_flag = Column('daily_profit_limit_flag', Boolean, default=False)
  daily_profit_stop_limit_percent = Column('daily_profit_stop_limit_percent', Numeric)
  daily_loss_margin = Column('daily_loss_margin', Numeric)
  daily_profit_margin = Column('daily_profit_margin', Numeric)
  daily_profit_stop_margin = Column('daily_profit_stop_margin', Numeric)
  daily_profit_stopped_value = Column('daily_profit_stopped_value', Numeric)
  bot_status = Column('bot_status', String(50))
  bot_log = Column('bot_log', String(50))

class Candle(Base):
  __tablename__ = 'market_candle'
  __table_args__ = {'extend_existing': True}
  id = Column('id', BigInteger, primary_key=True)
  Open_time_str = Column('Open_time_str', Date)
  Open = Column('Open', Numeric)
  High = Column('High', Numeric)
  Low = Column('Low', Numeric)
  Close = Column('Close', Numeric)
  Volume = Column('Volume', Numeric)
  Close_Time_str = Column('Close_Time_str', Date)
  Quote_Asset_Volume = Column('Quote_Asset_Volume', Numeric)
  Number_Of_Trades = Column('Number_Of_Trades', Numeric)
  Taker_Buy_Base_Asset_Volume = Column('Taker_Buy_Base_Asset_Volume', Numeric)
  Taker_Buy_Quote_Asset_Volume = Column('Taker_Buy_Quote_Asset_Volume', Numeric)
  Ignore = Column('Ignore', Numeric)
  candle_pattern = Column('candle_pattern', String(500), default="")
  candle_score = Column('candle_score', Numeric)
  candle_cumsum = Column('candle_cumsum', Numeric)
  signal = Column('signal', Numeric)
  signal2 = Column('signal2', Numeric)


class Market_Arbi(Base):
  __tablename__ = 'market_arbi'
  __table_args__ = {'extend_existing': True}
  id = Column('id', BigInteger, primary_key=True)
  market_time = Column('market_time', DateTime)
  ab_symbol = Column('ab_symbol', String(50))
  bc_symbol = Column('bc_symbol', String(50))
  ca_symbol = Column('ca_symbol', String(50))
  ab_rate = Column('ab_rate', Numeric)
  bc_rate = Column('bc_rate', Numeric)
  ca_rate = Column('ca_rate', Numeric)
  start_a = Column('start_a', Numeric)
  to_b = Column('to_b', Numeric)
  to_c = Column('to_c', Numeric)
  to_a = Column('to_a', Numeric)
  cut_cost1 = Column('cut_cost1', Numeric)
  cut_cost2 = Column('cut_cost2', Numeric)
  cut_cost3 = Column('cut_cost3', Numeric)
  total_cost = Column('total_cost', Numeric)
  net_to_a = Column('net_to_a', Numeric)
  profit_rate = Column('profit_rate', Numeric)
  net_profit_rate = Column('net_profit_rate', Numeric)
  market_log = Column('market_log', String(500), default="")
  trade_id = Column('trade_id', BigInteger)


class Trade_Arbi(Base):
  __tablename__ = 'trade_arbi'
  __table_args__ = {'extend_existing': True}
  id = Column('id', BigInteger, primary_key=True)
  market_time = Column('market_time', DateTime)
  ab_symbol = Column('ab_symbol', String(50))
  bc_symbol = Column('bc_symbol', String(50))
  ca_symbol = Column('ca_symbol', String(50))
  ab_rate = Column('ab_rate', Numeric)
  bc_rate = Column('bc_rate', Numeric)
  ca_rate = Column('ca_rate', Numeric)
  real_rate_ab = Column('real_rate_ab', Numeric)
  real_rate_bc = Column('real_rate_bc', Numeric)
  real_rate_ca = Column('real_rate_ca', Numeric)    
  real_quantity_a = Column('real_quantity_a', Numeric)
  real_quantity_b = Column('real_quantity_b', Numeric)
  real_quantity_c = Column('real_quantity_c', Numeric)
  returned_quantity = Column('returned_quantity', Numeric)
  predicted_profit_rate = Column('predicted_profit_rate', Numeric)
  trade_log = Column('trade_log', String(500), default="")
