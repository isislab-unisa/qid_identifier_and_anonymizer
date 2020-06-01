# qid_identifier_and_anonymizer
It contains a framework to select the best QID by the number of disclosed singletons and it provides an anonymization mechanism (based on generalization and suppression) to anonymize the well-known QID (year_of_birth, sex, sex) by minimizing the number of singletons while minimizing the number of affected rows.

Src folder contains the source code. More in details:
Framework.py is the master file, it contains all the calls to the other scripts. It provide the opportunity to launch only privacy_checker on the dataset.
First call of this file is privacy checker on the dataset, it gives us various statistics, as number of singletons, percentage of singletons, best QID.
Next, calls SetIndex that create a new id for all of the dataset's records, is helpful for the matching of the original csv with the anonymized one.
Every iteration of anonymization, is made of 4 steps. The first one calls the script in charge of anonymizing the dataset with a certain technique. Once this step is completed
the framework provide to match the datasets, the original one with the anonymized one. Further more it delete the newId to let privacy_checker work properly.
The scripts of anonymization are the following:
-AnnoRange provide to anonymize the dataset creating a range of years instead a certain date.
-AnnoCentroide does the same, but instead of creating a range it takes the medium value of it.
-GenereAll anonymize the entire dataset deleting the genre from all the records.
-GenereSingleton anonymize only the singletons we found, deleting the genre from them.
-ProvinceAll anonymize the entire dataset putting the region instead of the city.
-ProvinceSingleton does the same, but only on the singletons.
Next the framework provide to use the anonymization techniques with all the possible combinations between them.
