# About
This project is a online client-server model data-mining application

## How to Use
### For running on local desktop:

1. install python3 first

2. install all dependencies in `requirement.txt`

3. type in `python manage.py runserver`

4. You should be able to use this software in `localhost:8080` now


### For running on server:

1. cofigure nginx `uwsgi --http :8000 --chdir /root/dataMining/ -w djangoData.wsgi`

2. configure path and allowed host

-STATIC_URL = '/static/'
+STATIC_URL = '/polls/static/'
+STATIC_ROOT = '/root/dataMining/polls/static/'

# Road Map
## Version
- [X] 0.1 CSV preview and nav bars, writing templates for home page and all sub-pages
- [X] 0.2 Classification tempalte and base logic set up
- [X] 0.3 Finished Classification 
- [X] 0.4 Finished documention tempaltes and documents for Classification
- [X] 0.5 Clustering tempalte and base logic set up 
- [X] 0.6 Finished Clustering 
- [X] 0.7 Finished documention for clustering
- [X] 0.8 Deploy this software to server
- [X] 0.9 Finished Aporiori based association rules, finished upload and downloading functionalities
- [X] 1.0 Adding detailed documentation and all functionalities for parameters adjustment

## Functionalities
### General
- [X] Show all data uploaded
- [X] File upload and download
- [X] Using Ajax to dynamically change HTML element.
- [X] Using Django tempaltes for all types of demand
- [X] Configure Django URL config different functionalities
- [X] Using OOP for Django views
- [ ] More data fomat support: xls
- [ ] More data fomat support: text file

### Data preprocess
- [X] Missing data handling
- [ ] More advanced Missing data handling(fix missing data automatically)
- [X] char to digit tranformation

### Clustering
- [X] Clustering: KMeans
- [X] Clustering:Mini Batch KMeans 
- [X] Clustering:Affinity Propagation
- [X] Clustering:Mean Shift
- [X] Clustering:Spectral Clustering
- [X] Clustering:Agglomerative Clustering
- [X] Clustering:DBSCAN
- [X] Clustering:Birch
- [X] Documentation for Clustering
- [X] Parameters Adjustment for Clustering

### Classification
- [X] Classification:Logistic Regression
- [X] Classification:KNeighbors Classifier
- [X] Classification:SVC
- [X] Classification:GradientBoosting Classifier
- [X] Classification:DecisionTree Classifier
- [X] Classification:Random Forest Classifier
- [X] Classification:MLP Classifier
- [X] Classification:Gaussian Naive Bayes
- [X] Documentation for classification
- [X] Parameters Adjustment for Classification

### Association rules
- [X] Apriori algorithm
- [ ] Parameters for Apriori algorithm
- [ ] Full documentation for Apriori algorithm
- [ ] More association rules algorithm
