import yfinance as yf
import pandas as pd

class Yfinancee:
    def __init__(self, symbol, debut, fin):
        self.symbol = symbol
        self.debut = debut
        self.fin= fin
        
    def gdata(self):
        data = yf.download(self.symbol, start=self.debut, end=self.fin, group_by='ticker')
        data.reset_index(inplace=True)
        data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
        return data.to_dict('records')