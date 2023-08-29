#%%
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt 
import random 
import csv
from pathlib import Path

def HistoricalData(tickr, value, Start, End, Freq="1d", logging=False):
  ## INPUTS: ticker, the value desired (open, close, volume etc), start and end date as well as the frequency desired, with a default of daily
  ## OUTPUTS: A list of the desired value over the time period with the given frequency
  stock = yf.Ticker(tickr + ".AX")
  stockInfo = stock.history(start=Start, end=End, interval=Freq)
  stockLst = stockInfo[value][:]
  if logging == True:
    print(stockLst)
  return stockLst

def dataAq(fileName, market, logging=False):
  ## INPUTS: filename, which global market at play, optional logging
  ## OUTPUTS: A list of tickers from the file

  csv_file = Path(__file__).parent / fileName
  tickerLst = []
  with csv_file.open() as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      tickerLst.append(row[0].removeprefix(market + ":"))
  if logging == True:
    print(tickerLst)
  return tickerLst

ASXTickerList = dataAq("ASX.csv", "ASX")

#%%
dataLst = []
for i in range(200):
  data = HistoricalData(ASXTickerList[i], "Close", "2020-01-01", "2022-01-01")
  dataLst.append(data)
  plt.plot(range(len(dataLst[i])), dataLst[i])
plt.show()
#%%

