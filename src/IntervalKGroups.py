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
data=pd.read_csv(file_path , delimiter=",", dtype={"anno_nascita":float,"comune_residenza": object, "sesso":object})
columns_names=["newId","anno_nascita", "comune_residenza", "sesso"]
columnIndex=data["newId"]
newData=pd.DataFrame(columns= columns_names,index=columnIndex)
newData=data.sort_values("anno_nascita")

newData.dropna(inplace=True)
columnDate=newData["anno_nascita"].to_numpy()
newColumnDate = list(set(columnDate))

n=4
arrayNewCentroids=[]
newColumnDate = [newColumnDate[i * n:(i + 1) * n] for i in range((len(newColumnDate) + n - 1) // n )]  
 

for array in newColumnDate:
	middle = float(len(array))/2
	if middle % 2 != 0:
			arrayNewCentroids.append(array[int(middle - .5)])
	else:
			arrayNewCentroids.append((array[int(middle)]))

NewColumn=columnDate.tolist()
NewColumn = [ int(x) for x in NewColumn ]


i=0
d=0
while i < len(columnDate):

	while d < len(newColumnDate):
		if NewColumn[i] in range (int(newColumnDate[d][0] ) ,int(newColumnDate[d][-1]+1)):
			NewColumn[i]=newColumnDate[d][0],"/",newColumnDate[d][-1]
			
			break
		d=d+1
	i=i+1
	d=0

newData["anno_nascita"]=NewColumn

newData.to_csv(file_name+"Range.csv", index=False)






		

