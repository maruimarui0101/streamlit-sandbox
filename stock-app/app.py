import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Simple stock price app

Shown are the stock **closing price** and **volume** of Google!

""")

# defn the ticker symbol
tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2020-01-01', end='2020-06-30')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
