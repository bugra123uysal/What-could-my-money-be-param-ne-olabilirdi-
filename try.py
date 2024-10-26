import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import tkinter as tk
import datetime
hisseler = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN', 'NFLX', 'NVDA', 'PYPL', 'BABA']


maıın=tk.Tk()

maıın.title("dene")

maıın.geometry("500x500")

mnysv=tk.Entry(maıın, textvariable='birikim miktarını giriniz')
mnysv.pack()

oe=tk.OptionMenu(maıın, *hisseler )
oe.pack()


hspl=tk.Button(maıın, text='hesapla')
hspl.pack()



maıın.mainloop()


