import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# "Solo tres acciones de empresas argentinas en Nueva York ganaron en 2020"
Aplicación web realizada con la librería Streamlit. Los datos fueron obtenidos a través de la librería Yfinance.
https://www.cronista.com/finanzas-mercados/Bolsas-de-Europa-cerraron-en-rojo-por-mas-restricciones-y-WallStreetopera-plano-20201231-0011.html
Precio de cierre y volumen durante el 2020, info de la compañía.  
#  Mercado libre:
""")

#definimos el símbolo bursátil
tickerSymbol = 'MELI'
#obtenemos data con la librería yfinance
tickerData = yf.Ticker(tickerSymbol)
#obtenemos los precios históricos de esta compañía en un período dado
tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2021-1-1')


st.write("""
## Precio de cierre
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volumen
""")
st.line_chart(tickerDf.Volume)
#info de la compañía
tickerData.info


st.write("""
#  Globant:
""")


tickerSymbol = 'GLOB'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2021-1-1')


st.write("""
## Precio de cierre
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volumen
""")
st.line_chart(tickerDf.Volume)

tickerData.info


st.write("""
#  Ternium (Grupo Techint):
""")

tickerSymbol = 'TX'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2021-1-1')


st.write("""
## Precio de cierre
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volumen
""")
st.line_chart(tickerDf.Volume)

tickerData.info



