from  Yahoo_recup import Yfinancee
from  strreamlit import Streamlitappli
from mongo_push import Mongobdd
import yfinance as yf
import streamlit as st
from pprint import pprint



init = Yfinancee('AAPL', '2020-12-01','2021-12-01')
data = init.gdata()
pprint(data)
mongo = Mongobdd('Yfinance', 'AAPL')
insert = mongo.insert_data(data)
affiche = Streamlitappli('Yfinance', 'AAPL')
afiche = affiche.affich_data()

