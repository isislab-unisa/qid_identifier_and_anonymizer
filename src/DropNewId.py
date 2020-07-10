import pandas as pd
import random
import numpy as np
import sys
import os
class DropNewIdClass():
	def dropNewId(file_path):
		file_name = os.path.basename(file_path).split(".")[0]
		df = pd.read_csv(file_path)


		df.drop("newId", axis=1, inplace=True)

		df.to_csv(file_name+"NoNewId.csv", index=False)