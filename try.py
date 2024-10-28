import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import tkinter as tk
import datetime





maıın=tk.Tk()

maıın.title("dene")

maıın.geometry("500x500")



hisseler = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN', 'NFLX', 'NVDA', 'PYPL', 'BABA']
""" değişken tanımlama """
sec_hısse=tk.StringVar()
sec_hısse.set(hisseler[0])



def grfk():
   global bucket 
   global yy

   
   """ bütcenin yüzdesini almak  almak  """
 
   bucket=float( mnysv.get())
   mn=sec_hısse.get()
   

   strt=datetime.datetime.now()
   sn=datetime.datetime(strt.year , 1,1)

   sok=yf.download(mn, start=sn , end=strt)

   yılbs=sok['Close'].iloc[0]
   gncl=sok['Close'].iloc[-1]

   """ hisse senedinin yılbaşından bu yana  yüzde getirisi  """
   yy=((gncl-yılbs)/yılbs)*100

   """ bütcenin yüzdesini almak  """
   bte=(bucket *(1 + (yy /100)))


   


   lbl=tk.Label(maıın, text=f"{mn}: {yy} , \n  {bucket} birim para , yükselerek  {bte} olur   "  , font=('Helvetica', 12))
   lbl.pack()



mnysv=tk.Entry(maıın)
mnysv.pack()

oe=tk.OptionMenu(maıın, sec_hısse ,*hisseler )
oe.pack()


hspl=tk.Button(maıın, text='hesapla', command=grfk)
hspl.pack()



""" ikinci sayfa   """

def twopages():
  

  scn=tk.Toplevel(maıın)
  scn.title("risk seviyeleri ")
  scn.geometry("500x500")

  hissele = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN', 'NFLX', 'NVDA', 'PYPL', 'BABA']
  dataa = yf.download(hissele, start='2023-01-01', end='2023-12-31')['Adj Close']

  daily_retun=dataa.pct_change().dropna()  
  """ Günlük ortalama getiriyi ve günlük getirilerin standart sapmasını hesaplayın """  
  mean_daily_return=daily_retun.mean()
  std_dev_daily_return=daily_retun.std()  
  """ Yıllık getiri ve oynaklık """  
  annualized_return=mean_daily_return* 252 # 252 trading days in a year
  annualized_std_dev=  std_dev_daily_return* np.sqrt(252)  
  """ risk """  
  risk_free_rate= 0.02  
  sharpe_ratio=(annualized_return - risk_free_rate )/ annualized_std_dev
  print(f"{sharpe_ratio}")
  rısk_wıea=tk.Label(scn, text=f"risk : {sharpe_ratio}")
  rısk_wıea.pack()



geç=tk.Button(maıın,text='rısk sevıyeleri', command=twopages )
geç.pack()


maıın.mainloop()


