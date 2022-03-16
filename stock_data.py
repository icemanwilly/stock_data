import time
import finnhub
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.widgets import Button

finnhub_client = finnhub.Client(api_key="c7stlf2ad3i9jn7rlr9g")

def ColorCheck(p):
  if p[0] > p[-1]:
    color = "red"
  else:
    color = "green"
  return color

def oneDay(val):
  prices = finnhub_client.stock_candles("AAPL", "5", int(time.time()) - 86400, int(time.time()))["c"][-125:]
  x = np.linspace(0, len(prices) / 12, len(prices))
  color = ColorCheck(prices)
  plt.sca(ax)
  plt.cla()
  ax.plot(x, prices, color=color)
  plt.show()

def fiveDay(val):
  prices = finnhub_client.stock_candles("AAPL", "30", int(time.time()) - 604800, int(time.time()))["c"]
  x = np.linspace(0, 5, len(prices))
  color = ColorCheck(prices)
  plt.sca(ax)
  plt.cla()
  ax.plot(x, prices, color=color)
  plt.show()
  
def oneMonth(val):
  prices = finnhub_client.stock_candles("AAPL", "D", int(time.time()) - 2630000, int(time.time()))["c"]  
  x = np.linspace(0, 30, len(prices))
  color = ColorCheck(prices)
  plt.sca(ax)
  plt.cla()
  ax.plot(x, prices, color=color)
  plt.show()

def sixMonth(val):
  prices = finnhub_client.stock_candles("AAPL", "D", int(time.time()) - 15780000, int(time.time()))["c"]
  x = np.linspace(0, len(prices) / 30, len(prices))
  color = ColorCheck(prices)
  plt.sca(ax)
  plt.cla()
  ax.plot(x, prices, color=color)
  plt.show()

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


import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
import math

def updateGraph():
    """Example function triggered by Tkinter GUI to change matplotlib graphs."""
    global currentGraph
    # Clear all graphs drawn in figure
    plt.clf()
    prices = finnhub_client.stock_candles("AAPL", "5", int(time.time()) - 86400, int(time.time()))["c"][-125:]
    x = np.linspace(0, len(prices) / 12, len(prices))
    color = ColorCheck(prices)
    plt.plot(x,prices, color=color)
    fig.canvas.draw()

# This defines the Python GUI backend to use for matplotlib
matplotlib.use('TkAgg')

# Initialize an instance of Tk
root = tk.Tk()

# Initialize matplotlib figure for graphing purposes
fig = plt.figure(1)

# Special type of "canvas" to allow for matplotlib graphing
canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()


# Example data (note: default calculations for angles are in radians)
updateGraph()


# Add the plot to the tkinter widget
plot_widget.grid(row=1, column=0, columnspan=5)

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

variable = tk.StringVar(root)
variable.set(OPTIONS[0]) # default value

w = tk.OptionMenu(root, variable, *OPTIONS)
w.grid(row=0, column=0, sticky="NESW")

button = tk.Button(root, text="OK")
button.grid(row=0, column=1, sticky="NESW")


root.mainloop()
"""
axes = plt.axes([0.1, 0.9, 0.05, 0.05])
bnext = Button(axes, '1D',color="yellow")
bnext.on_clicked(oneDay)

axes = plt.axes([0.25, 0.9, 0.05, 0.05])
bnext2 = Button(axes, '5D',color="yellow")
bnext2.on_clicked(fiveDay)

axes = plt.axes([0.4, 0.9, 0.05, 0.05])
bnext3 = Button(axes, '1M',color="yellow")
bnext3.on_clicked(oneMonth)

axes = plt.axes([0.55, 0.9, 0.05, 0.05])
bnext4 = Button(axes, '6M',color="yellow")
bnext4.on_clicked(sixMonth)

axes = plt.axes([0.7, 0.9, 0.05, 0.05])
bnext5 = Button(axes, '1Y',color="yellow")
bnext5.on_clicked(oneYear)

axes = plt.axes([0.85, 0.9, 0.05, 0.05])
bnext6 = Button(axes, '5Y',color="yellow")
bnext6.on_clicked(fiveYear)"""
