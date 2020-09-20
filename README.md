
[![Build Status](https://travis-ci.com/MatteoPastore/qid_identifier_and_anonymizer.svg?branch=master)](https://travis-ci.com/MatteoPastore/qid_identifier_and_anonymizer)
# qid_identifier_and_anonymizer
This repository contains a (software) Anonymization Framework to perform singletons analysis and anonymization of OpenData’s datasets. OpenData must guarantee consistent information but at the same time must not harm the privacy of individuals. Analyzing open datasets containing information relating to licenses and published by the Italian government, the well-known quasi-identifier (date of birth, sex, municipality of residence) exhibits up to 2% of singleton, i.e. uniquely determined tuples, in already anonymized datasets. Our goal is to find the best tradeoff between consistent information (Fewer modified or deleted tuples) and maintaining privacy (Fewer number of singletons). The Framework select the best QID by the number of disclosed singletons and it provides an anonymization mechanism (based on generalization and suppression) to anonymize the well-known QID (year_of_birth, sex, sex) by minimizing the number of singletons while minimizing the number of affected rows. 
# Framework structure
It is a diagrammatic representation of the involved actors in the framework and their interactions. The blue boxes represent abstract classes, while the white boxes represent concrete classes.



The starting point of the anonymization is the Anonymizer which is the orchestrator of the whole anonymization and it is in charge of:
  1. verifying the correctness of the parameters set by the user,
  2. veryfing the type of the attribute to start the process,
  3. call the right script to anonymize according to the type of the attribute provided by the user,
  4. forward the right field to anonymize
  
Depending on the type of the attribute, the corresponding script decides how to anonymize the field. Three are the field-type supported by the framework.
  1. Year, that can be anonymized by Range ( YearRange ) or by Centroid ( YearCentroid ),
  2. Gender, that can be anonymized by All or Singletons,
  3. Municipality, that can be anonymized by All or Singletons.

Once anonymized, two are the following steps.
  1. MatchingCsv provide to match the modified lines and the deleted lines between the original dataset and the new one.
  2. PrivacyChecker provide to analyze the new dataset and discover how many singletons ( and wich percentage of them ) it has.
  
The framework can run in debug or no-debug mode, further more it can run in parallel mode.
In parallel mode it creates a thread for each anonymization technique.

# Repository structure 
![Structure](https://github.com/isislab-unisa/qid_identifier_and_anonymizer/blob/master/Structure.png?raw=true)
The core of the software is the main Framework:
  1. at launch it allows you to choose the mode of use;
  2. introduces a new dummy index to the dataset, to ensure that in subsequent operations, each record will correspond to itself and there can be no alterations. For example, when comparing the original dataset with the anonymized one, each tuple must match itself and there must be no disorder between them;
  3. will launch privacy_checker on the original dataset.

Then the anonymization cycle launched by the Framework begins, each anonymization cycle involves three phases:
  1. anonymization;
  2. comparison between original and anonymized dataset;
  3. privacy control of the new dataset.

The anonymization phase is managed by the Anonymizer.

It extends an abstract class, this because at any time the anonymization process can be replaced according to your needs.
It takes three arguments as input, the path of the file to be anonymized, on which field of the dataset to operate and which Type of data represents the field. The dataset field refers to which attribute to anonymize. The type instead refers to which data the field represents (gender, year, municipality). This implementation choice serves to make the process as abstract as possible, to make sure that whatever the name of the field, through the type argument, the anonymizer will know how to act.
If the attribute does not fall into these 3 categories, then the anonymizer will indicate to the user that the type is not yet supported.
After this comparison, the anonymizer calls the classes in charge of the corresponding anonymization. Therefore the role of the anonymizer is to sort out requests for anonymization.
In detail, there are 6 classes used for the anonymization of the dataset.
  1. genderAll: implements a global approach on the dataset by modifying the gender field with an empty box, which is equivalent to replacing the attribute with a generic one;
  2. genderSingleton: implements a local approach on the dataset by modifying the sex field with an empty box only in the lines representing singletons;
  3. provinceAll: implements a global approach on the dataset by modifying the municipality field with the generalization of the municipality to which it belongs. If it has already been anonymized, or if it is in the form of a region, the framework will move up the anonymization hierarchy by replacing the region with the nation and so on;
  4. provinceSingleton: implements a local approach on the dataset by modifying the municipality5 field with the generalization of the municipality but only in the lines that identify singletons;
  5. yearRange: replaces the year or date with a range of years. To do this, divide the years into groups of k elements, then take the minimum and maximum value of the groups to create the range;
  6. yearCentroid: replaces the year or date with the average range value.

For the targeted action of the anonymization technique on singletons, we use a slightly modified version of the PrivacyChecker, which identifies the singletons and reports them in a new csv file. The framework scrolls the latter and identifies the exact position of the corresponding row in the original dataset, modifying only the field we want to anonymize.
Once the anonymization process is complete, the quality control process begins, implemented by MatchingCsv. Quality is measured as the number of modified (suppressed + generalized) tuples. It is done by comparing the original dataset with the anonymized one, line by line. The certainty that the corresponding rows are being compared is given to us by the fact that we have previously entered a dummy ID that uniquely identifies a tuple. The process takes place by comparing the values contained in it field by field. At the end of the comparison, the number of modified and suppressed lines are printed in a log file.
The last step of the anonymization cycle is the one that involves privacy control, measured as the number of singletons detected within the dataset. The process takes place thanks to the PrivacyChecker. It is used for the election of the best QID, for the calculation of the number of singletons, percentage of singletons and calculation of distinct values.
The anonymization process takes place both by implementing it on one field at a time, and in pairs and finally on all 3 attributes together. When the anonymization process is concluded for each of the aforementioned combinations, we move on to the analysis of all the anonymizations carried out with their relative results (number of singletons, modified and deleted rows).
In charge of this is BestAnonymization which creates csv files containing a table where the various anonymization techniques are ordered both by the number of singletons, and by the number of modified rows, so that the user has at first impact idea of ​​which technique affected the quality of the dataset the least and which the loss of privacy.

#Modes of use
  1. debug: provides for the screen printing of each beginning and end of phase, so that the user can realize what the framework is doing and, in case of errors or slowdowns, know in which part of the program to intervene. The debug parameter is required and has a value of true or false;
  2.  Singleton municipality: since after numerous tests for various regions, I have identified that in most cases the anonymization of the municipality on singletons is the most efficient, the framework provides the option to launch the anonymization process only for this attribute, so such as to have a quick response avoiding all other techniques;   3. multithreading: in this mode of use, a thread is created for each anonymization process. The thread performs the functions of anonymization, quality control and privacy control in parallel to the other techniques. Through a join function, the processes in which multiple fields are anonymized wait for the previous step (anonymization of the single field) to finish. This mode greatly speeds up all processes.
  
#Dependencies

The framework is tested to work on Python 3.7.

The required dependencies are:
atomicwrites==1.4.0
attrs==19.3.0
certifi==2020.6.20
chardet==3.0.4
codecov==2.1.7
colorama==0.4.3
coverage==5.2
idna==2.10
importlib-metadata==1.7.0
more-itertools==8.4.0
numpy==1.18.1
packaging==20.4
pandas==1.0.1
pluggy==0.13.1
py==1.9.0
pyparsing==2.4.7
pytest==5.4.3
pytest-cov==2.10.0
python-dateutil==2.8.1
pytz==2019.3
requests==2.24.0
six==1.14.0
threaded==4.0.8
urllib3==1.25.9
virtualenv==16.7.5
wcwidth==0.2.5
zipp==3.1.0
APScheduler==2.1.2










