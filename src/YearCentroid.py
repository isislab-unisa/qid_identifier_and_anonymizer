import pandas as pd
import csv as csv
import numpy as np
import os
import sys

class YearCentroidClass():
	def anonymizeYearCentroid(file_path, field):

		file_name = os.path.basename(file_path).split(".")[0]
		data=pd.read_csv(file_path, delimiter=",")
		cols=[]
		for col in data.columns:
			cols.append(col)
		
		columnIndex=data.iloc[:,0]
		newData=pd.DataFrame(columns=cols,index=columnIndex)
		newData=data.sort_values(field)
		newData.dropna(inplace=True)
		columnDate=newData[field].to_numpy()
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
		arrayNewCentroids= [ int(x) for x in arrayNewCentroids]
		i=0
		d=0
		while i < len(columnDate):

			while d < len(arrayNewCentroids):
				if NewColumn[i] in range (int(newColumnDate[d][0] ) ,int(newColumnDate[d][-1]+1)):
					NewColumn[i]=arrayNewCentroids[d]
					
					break
				d=d+1
			i=i+1
		newData[field]=NewColumn
		newData.to_csv(file_name+"Centroid.csv", index=False)






				


