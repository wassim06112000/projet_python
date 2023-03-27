import yfinance as yf
import pandas as pd
from pymongo import MongoClient
from pprint import pprint
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pymongo import MongoClient



class Streamlitappli:
    def __init__(self, db_name, collection_name):
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = MongoClient()
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]
        
    def affich_data(self):
        data = pd.DataFrame(list(self.collection.find()))
        
        
        
        
        #graphique
        fig = go.Figure(data=go.Scatter(x=data['Date'], y=data['Close']))
        st.plotly_chart(fig)
        fig = go.Figure(data=go.Candlestick(x=data['Date'],
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close']))
        st.plotly_chart(fig)
        #tableau
        st.write(data)
        




