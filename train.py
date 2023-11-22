# pip install streamlit fbprophet yfinance plotly
import streamlit as st
import datetime as date

import yfinance as yf
import prophet as Prophet
import prophet.plot as plot_plotly
import plotly as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365
