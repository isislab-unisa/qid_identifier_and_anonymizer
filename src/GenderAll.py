import pandas as pd
import csv as csv
import numpy as np
import sys
import os
arguments = len(sys.argv) - 1
if arguments < 1:
	print ("you must provide the file url")
else:
	file_path = sys.argv[1]
	file_name = os.path.basename(file_path).split(".")[0]
data=pd.read_csv(file_path, delimiter=",", dtype={"anno_nascita":float,"comune_residenza": object, "sesso":object})


data["sesso"]=" "

data.to_csv(file_name+"GenderAll.csv", index=False)