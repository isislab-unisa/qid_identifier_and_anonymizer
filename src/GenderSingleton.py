import pandas as pd
import csv as csv
import numpy as np
import os
import sys

class GenderSingletonClass():

  def anonymizeGenderSingleton(file_path, field):
    file_name = os.path.basename(file_path).split(".")[0]
    columns=os.path.splitext("sesso,anno_nascita,comune_residenza.csv")[0].split(",")

    colnames=[]
    for name in columns:
     colnames.append(name)
    colnames.append("n")

    output=pd.read_csv("sesso,anno_nascita,comune_residenza.csv",  delimiter=",", dtype={"anno_nascita":object,"comune_residenza": object, "sesso":object})


    data_df=pd.read_csv(file_path, delimiter=",", dtype={"anno_nascita":object,"comune_residenza": object, "sesso":object})

    i=0

    for index, row in output.iterrows():
      anno = row["anno_nascita"]
      comune = row["comune_residenza"]
      sesso = row["sesso"]
     
      
      #print(data_df.loc[(data_df.anno_nascita==anno) & (data_df.comune_residenza==comune) & (data_df.sesso==sesso)])
      data_df.loc[(data_df.anno_nascita==anno) & (data_df.comune_residenza==comune) & (data_df.sesso==sesso), [field]] = " "


  
  
      i=i+1

    data_df.to_csv(file_name+"GenderSingleton.csv", index=False)
