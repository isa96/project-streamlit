import streamlit as st
import yfinance as yf
import pandas as pd

st.sidebar.write(
    '''
    # Simple Stock Price App
    Made with **streamlit** 
    '''
)

tickerSymbol = st.sidebar.selectbox('Select ticker: ', ('GOOG', 'AAPL', 'MSFT', 'FB'))
tickerData = yf.Ticker(tickerSymbol)

tickerPeriod = st.sidebar.selectbox('Period:', ('1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'))
tickerInterval = st.sidebar.selectbox('Interval:', ('1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'))

tickerDf = tickerData.history(period=tickerPeriod, interval=tickerInterval)

"## Closing Price"
st.line_chart(tickerDf['Close'], use_container_width=True)

"## Trading Volume"
st.bar_chart(tickerDf['Volume'], use_container_width=True)