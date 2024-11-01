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
   """ kaç yıl hesaplanacağı """
   tım=int(sr.get())
   """Faiz hesaplama sıklığı  """
   fahe=int(fhs.get())
   a=bucket * (1 + (yy / (fahe * 100))) ** (fahe * tım )
   bakye=bucket
   bakyem=[]
   """ bileşik faiz aylık """

   
   for ay  in range(1 , tım * 12 + 1):
     bakye += bakye * tım
     bakyem.append(bakye)

   lbl.config(text=f"{mn} Yüzde Getiri: {yy:.2f}% \nBaşlangıç Miktarı: {bucket} \n{tım} Yıl Sonrası Bakiye: {bakyem[-1]:.2f}")



    

   
   """ bileşik faiz grafığı  """

   plt.plot(range(1, tım + 1 ), bakyem )
   plt.grid(True)
   plt.show()

""" hisse seç """
oe=tk.OptionMenu(maıın, sec_hısse ,*hisseler )
oe.pack()

""" başlangıcda yatırlacak para """
mnysv=tk.Entry(maıın)
mnysv.pack()

""" süre yıl olarak yazılmalı """
sr=tk.Entry(maıın )
sr.pack()



""" faiz hesaplama sıklığpı   Kullanıcı burada faiz hesaplamanın yıllık kaç defa yapılacağını belirtir (örneğin yıllık için 1, aylık için 12 gibi)."""
fhs=tk.Entry(maıın)
fhs.pack()


hspl=tk.Button(maıın, text='hesapla', command=grfk)
hspl.pack()



maıın.mainloop()


