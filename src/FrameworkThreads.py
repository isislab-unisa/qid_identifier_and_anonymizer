import pandas as pd
import random
import numpy as np
import os
import subprocess
import sys
from Anonymizer import AnonymizerClass as Anonymizer
from MatchingCsv import MatchingClass as MatchingCsv
from privacy_checker import PrivacyChecker as PrivacyChecker
from SetIndex import SetIndexClass as SetIndex
from DropNewId import DropNewIdClass as DropNewId
from BestAnonymization import BestFinder as BestFinder
import threading
import time



class AnonymizerThread (threading.Thread):
   def __init__(self, name, path, field, type):
      threading.Thread.__init__(self)
      self.name= name
      self.path = path
      self.field = field
      self.type = type
   def run(self):
      print ("Starting " + self.name)
      anonymizeThread(self.path, self.field, self.type)
      print ("Exiting " + self.name)

def anonymizeThread(path, field, type):
	Anonymizer.anonymize(path, field, type)	
	if type=="Year":
		MatchingCsv.matching("C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndex.csv", path[:-4]+"Range.csv")
		MatchingCsv.matching("C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndex.csv", path[:-4]+"Centroid.csv")	
		DropNewId.dropNewId(path[:-4]+"Range.csv")
		PrivacyChecker.privacychecker(path[:-4]+"RangeNoNewId.csv")
		DropNewId.dropNewId(path[:-4]+"Centroid.csv")
		PrivacyChecker.privacychecker(path[:-4]+"CentroidNoNewId.csv")
	if type=="Gender":
		MatchingCsv.matching("C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndex.csv", path[:-4]+"GenderAll.csv")
		MatchingCsv.matching("C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndex.csv", path[:-4]+"GenderSingleton.csv")	
		DropNewId.dropNewId(path[:-4]+"GenderAll.csv")
		PrivacyChecker.privacychecker(path[:-4]+"GenderAllNoNewId.csv")
		DropNewId.dropNewId(path[:-4]+"GenderSingleton.csv")
		PrivacyChecker.privacychecker(path[:-4]+"GenderSingletonNoNewId.csv")
	if type=="Municipality":
		MatchingCsv.matching("C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndex.csv", path[:-4]+"ProvinceAll.csv")
		MatchingCsv.matching("C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndex.csv", path[:-4]+"ProvinceSingleton.csv")	
		DropNewId.dropNewId(path[:-4]+"ProvinceAll.csv")
		PrivacyChecker.privacychecker(path[:-4]+"ProvinceAllNoNewId.csv")
		DropNewId.dropNewId(path[:-4]+"ProvinceSingleton.csv")
		PrivacyChecker.privacychecker(path[:-4]+"ProvinceSingletonNoNewId.csv")




if os.path.isfile("sesso,anno_nascita,comune_residenza.csv"):
	os.remove("sesso,anno_nascita,comune_residenza.csv")
if os.path.isfile("sesso,anno_nascita.csv"):
	os.remove("sesso,anno_nascita.csv")
if os.path.isfile("sesso,comune_residenza.csv"):
	os.remove("sesso,comune_residenza.csv")
if os.path.isfile("sesso.csv"):
	os.remove("sesso.csv")
if os.path.isfile("anno_nascita,comune_residenza.csv"):
	os.remove("anno_nascita,comune_residenza.csv")
if os.path.isfile("anno_nascita.csv"):
	os.remove("anno_nascita.csv")
if os.path.isfile("anno_nascita,sesso.csv"):
	os.remove("anno_nascita,sesso.csv")
if os.path.isfile("comune_residenza.csv"):
	os.remove("comune_residenza.csv")
if os.path.isfile("comune_residenza,sesso.csv"):
	os.remove("comune_residenza,sesso.csv")
if os.path.isfile("comune_residenza,anno_nascita.csv"):
	os.remove("comune_residenza,anno_nascita.csv")

os.system("python Singleton.py dataset.csv")
if os.path.isfile("anno_nascita,comune_residenza,sesso.csv"):
	os.rename(r'C:\\Users\\matte\\Desktop\\Framework2\\anno_nascita,comune_residenza,sesso.csv',r'C:\\Users\\matte\\Desktop\\Framework2\\sesso,anno_nascita,comune_residenza.csv')
if os.path.isfile("comune_residenza,anno_nascita,sesso.csv"):
	os.rename(r'C:\\Users\\matte\\Desktop\\Framework2\\comune_residenza,anno_nascita,sesso.csv',r'C:\\Users\\matte\\Desktop\\Framework2\\sesso,anno_nascita,comune_residenza.csv')
if os.path.isfile("anno_nascita,sesso,comune_residenza.csv"):
	os.rename(r'C:\\Users\\matte\\Desktop\\Framework2\\anno_nascita,sesso,comune_residenza.csv',r'C:\\Users\\matte\\Desktop\\Framework2\\sesso,anno_nascita,comune_residenza.csv')
if os.path.isfile("comune_residenza,sesso,anno_nascita.csv"):
	os.rename(r'C:\\Users\\matte\\Desktop\\Framework2\\comune_residenza,sesso,anno_nascita.csv',r'C:\\Users\\matte\\Desktop\\Framework2\\sesso,anno_nascita,comune_residenza.csv')
if os.path.isfile("sesso,comune_residenza,anno_nascita.csv"):
	os.rename(r'C:\\Users\\matte\\Desktop\\Framework2\\sesso,comune_residenza,anno_nascita.csv',r'C:\\Users\\matte\\Desktop\\Framework2\\sesso,anno_nascita,comune_residenza.csv')								#GenereSingleton


#SetIndex e PrivacyChecker
print("Running SetIndex and PrivacyChecker")
SetIndex.setIndex("C:\\Users\\matte\\Desktop\\Framework2\\dataset.csv")	
PrivacyChecker.privacychecker("C:\\Users\\matte\\Desktop\\Framework2\\dataset.csv")

#YearRange + YearCentroid
thread1=AnonymizerThread("YearRange + YearCentroid","C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndex.csv", "anno_nascita", "Year")
thread1.start()


#GenderAll and GenderSingleton

thread2=AnonymizerThread("Gender All + Gender Singleton","C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndex.csv", "sesso", "Gender")
thread2.start()


#ProvinceAll and ProvinceSingleton	

thread3=AnonymizerThread("Province All + Province Singleton","C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndex.csv", "comune_residenza", "Municipality")
thread3.start()


thread1.join()
thread2.join()
thread3.join()
#YearRange + Province

thread4=AnonymizerThread("Year Range + Province","C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndexRange.csv", "comune_residenza", "Municipality")
thread4.start()


#YearCentroid + Province

thread5=AnonymizerThread("Year Centroid + Province","C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndexCentroid.csv", "comune_residenza", "Municipality")
thread5.start()

#GenderAll + Province

threadGenderAllProvince=AnonymizerThread("Gender All + Province","C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndexGenderAll.csv", "comune_residenza", "Municipality")
threadGenderAllProvince.start()


#GenderAll + Year
thread7=AnonymizerThread("Gender All + Year","C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndexGenderAll.csv", "anno_nascita", "Year")
thread7.start()


threadGenderAllProvince.join()
#GenderAll + Province + Year

thread8=AnonymizerThread("Gender All + Province + Year ","C:\\Users\\matte\\Desktop\\Framework2\\dataset_newIndexGenderAllProvinceAll.csv", "anno_nascita", "Year")
thread8.start()

#Ranking
BestFinder.finder("C:\\Users\\matte\\Desktop\\Framework2\\resultsQuality", "C:\\Users\\matte\\Desktop\\Framework2\\results")
