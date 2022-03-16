import time
import finnhub
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.widgets import Button
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
import math

finnhub_client = finnhub.Client(api_key="c7stlf2ad3i9jn7rlr9g")

def ColorCheck(p):
  if p[0] > p[-1]:
    color = "red"
  else:
    color = "green"
  return color


def oneYear(val):
  prices = finnhub_client.stock_candles("AAPL", "D", int(time.time()) - 31536000, int(time.time()))["c"]
  x = np.linspace(0, len(prices) / 30, len(prices))
  color = ColorCheck(prices)
  plt.sca(ax)
  plt.cla()
  ax.plot(x, prices, color=color)
  plt.show()

def fiveYear(val):
  prices = finnhub_client.stock_candles("AAPL", "W", int(time.time()) - 157680000, int(time.time()))["c"]
  x = np.linspace(0, len(prices) / 30, len(prices))
  color = ColorCheck(prices)
  plt.sca(ax)
  plt.cla()
  ax.plot(x, prices, color=color)
  plt.show()

def updateGraph(val, dur):
    """Example function triggered by Tkinter GUI to change matplotlib graphs."""
    global currentGraph
    plt.clf()
    if dur == "1 Day":
      prices = finnhub_client.stock_candles(val, "5", int(time.time()) - 86400, int(time.time()))["c"][-125:]
      x = np.linspace(0, len(prices) / 12, len(prices))
    elif dur == "5 Days":
      prices = finnhub_client.stock_candles(val, "30", int(time.time()) - 604800, int(time.time()))["c"]
      x = np.linspace(0, 5, len(prices))
    elif dur == "1 Month":
      prices = finnhub_client.stock_candles(val, "D", int(time.time()) - 2630000, int(time.time()))["c"]
      x = np.linspace(0, 30, len(prices))
    elif dur == "6 Months":
      prices = finnhub_client.stock_candles(val, "D", int(time.time()) - 15780000, int(time.time()))["c"]
      x = np.linspace(0, len(prices) / 30, len(prices))
    elif dur == "1 Year":
      prices = finnhub_client.stock_candles(val, "D", int(time.time()) - 31536000, int(time.time()))["c"]
      x = np.linspace(0, len(prices) / 30, len(prices))
  color = ColorCheck(prices)
      
    color = ColorCheck(prices)
    plt.plot(x,prices, color=color)
    fig.canvas.draw()

def change(item):
  global dur, ticker
  ticker = item
  updateGraph(item, dur)

matplotlib.use('TkAgg')

root = tk.Tk()

fig = plt.figure(1)

canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()

dur = "1 Day"
ticker = "AAPL"
updateGraph(ticker, dur)

plot_widget.grid(row=1, column=0, columnspan=5)

OPTIONS = [
"AAPL",
"TSLA",
"NVDA",
"SPY",
"NFLX",
"AMZN",
"GOOGL"
] 

variable = tk.StringVar(root)
variable.set(OPTIONS[0]) 

w = tk.OptionMenu(root, variable, *OPTIONS, command=change)
w.grid(row=0, column=0, sticky="NESW")

def changeDuration(answer):
  global dur, ticker
  dur = answer
  updateGraph(ticker, answer)

OPTIONS = [
"1 Day",
"5 Days",
"1 Month",
"6 Months",
"1 Year",
"5 Years",
] 

duration= tk.StringVar(root)
duration.set(OPTIONS[0])

w2 = tk.OptionMenu(root, duration, *OPTIONS, command=changeDuration)
w2.grid(row=0, column=1, sticky="NESW")

root.mainloop()
