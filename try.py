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



def hspa():
    p=float(ana_money.get())
    r=float(rate.get())/ 100
    t=float(yas.get())
    n=12
    pmt=float(mount_money.get())

    bf=p*(1 + r / n )**(n * t) #ana para üzerinden hesaplama
    bf += pmt * (((1 + r / n) ** (n * t)-1) / (r / n) ) 
    wiev.config(text=f" {bf:,.2f}")
    

    

    
ğ=tk.Label(maıın, text="vade oranı 12 aydır " )
ğ.pack()

    

""" ana para """   
d=tk.Label(maıın, text="başlangıç parası" )
d.pack()
ana_money=tk.Entry(maıın)
ana_money.pack()    


"""aylık  yatırlacak para """
a=tk.Label(maıın, text="aylık-yatırılacak-para" )
a.pack()
mount_money=tk.Entry(maıın)
mount_money.pack()


""" faiz oranı """
b=tk.Label(maıın, text="faiz-oranı" )
b.pack()
rate=tk.Entry(maıın)
rate.pack()





""" yıl sayısı  """
c=tk.Label(maıın, text="kaç-yıl-yatırlacak" )
c.pack()
yas=tk.Entry(maıın)
yas.pack()




wiev=tk.Label(maıın )
wiev.pack()

hspl=tk.Button(maıın, text='hesapla', command=hspa)
hspl.pack()



maıın.mainloop()

