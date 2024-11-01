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

   """ bileşik faiz """
   a=bucket * (1 + (yy / (fahe * 100))) ** (fahe * tım )
   
 




   lbl=tk.Label(maıın, text=f"{mn}: {yy} , \n bütce: {bucket}  \n  {bte} olur  \n bileşik faiz: {a}  "    , font=('Helvetica', 12))
   lbl.pack()

""" hisse seç """
oe=tk.OptionMenu(maıın, sec_hısse ,*hisseler )
oe.pack()

""" yatırlacak para """


mnysv=tk.Entry(maıın)
mnysv.pack()

""" süre """
sr=tk.Entry(maıın )
sr.pack()



""" faiz hesaplama sıklığpı  """
fhs=tk.Entry(maıın)
fhs.pack()





hspl=tk.Button(maıın, text='hesapla', command=grfk)
hspl.pack()



maıın.mainloop()


