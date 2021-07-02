#from os import path
#import requests
#import time
#import mysql.connector
#from pathlib import Path
#from datetime import datetime
#Tax-data=

#mydb=mysql.connector.connect(
 #   host="localhost",
  #  user="taxoffice",
   # password="7vGnSPoxPK4PbhLx",
   # database="TaxOffice"

#)

#mycursor=mydb.cutsor()
#script_locatio= path(__file__).absolute().parent
#import mysql.connector

##mydb=mysql.connector.connect(
#host="localhost",
#user="taxoffice",
#password="7vGnSPoxPK4PbhLx",
#database="TaxOffice"
#)

#print(mydb)
#----------

#///%matplotlib inline
#import matplotlib.pyplot as plt
#import pandas as pd
#import numpy as np
#dt='C:\\Users\\LG\\Desktop\SUMMER1\\Real_Property_Tax_-_2020.csv'
#data=pd.read_csv(dt)
#print(data)
#plot_data=data[data['RESIDENCE']=='PRINCIPAL RESIDENCE']
#plot_data=plot_data.groupby('ZIP CODE')
#plot_data.plot(kind='hist',bins=100)
#plt.title("Top 10 Tax")
#plt.ylabel("TEST")