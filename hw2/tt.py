# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:25:50 2019
CS541 Intro to AI Class
Naive Bayse implementation on Heart Anomaly data set.
Pseudo Code was provide in the assignment.
@author: Kamakshi
"""
import csv
import numpy as np
from math import log
from sklearn.metrics import confusion_matrix
#open training data set
file1 = open('data/spect-orig.train.csv','r')
data1 = csv.reader(file1)
train_data = np.array(list(data1))
#open test data set
file2 = open('data/spect-orig.test.csv','r')
data2 = csv.reader(file2)
test_data = np.array(list(data2))
""" 
F[i,j] is a two-dimensional array of counts, where the left dimension is an instance classication (0 or 1) 
and the right dimension is a feature number. The contents of each array entry is a count of the number of times 
that the given feature appears positive in the given class. 
The array N[i] is indexed by instance classication and gives the count of training instances with that classication.
Each training instance t has a class t:c and an array of features t.f .
"""
def learner(train_data):
    F = np.zeros((2,train_data.shape[1]))
    N = np.zeros((2,1))
    for i in range(train_data.shape[0]):
       target_class = int(train_data[i,0])
       if target_class ==0:
           N[0] +=1
       else:
           N[1]+=1
       for j in range(1,train_data.shape[1]):
           if train_data[i,j]=='1':
               F[target_class,j] += 1
    return F,N
"""
Like the training instances, a classication instance has an array of features c.f .
"""
def classifier(F,N,k):
    L = np.zeros((2,1))
    for i in range(2):
        L[i] = log(N[i]+0.5)-log(N[0]+N[1]+0.5)
        for j in range(1,test_data.shape[1]):
            s = F[i,j]
            if test_data[k,j]== '0':
                s = N[i] -s
            L[i]= L[i]+log(s+0.5) - log(N[i]+0.5)
    return(L)
def classify():
      predicted_list =[]
      for i in range(test_data.shape[0]):
          L = classifier(F,N, i)
          if L[1]>L[0]:
              predicted_list.append(1)
          else:
              predicted_list.append(0)
      return(predicted_list)
## Main Program
(F,N) = learner(train_data)
pred_list = classify()
actual_list = []
for i in range(test_data.shape[0]):
        target_class = test_data[i,0].astype('int') #labels from csv
        actual_list.append(target_class)
accur = (np.array(pred_list) == np.array(actual_list)).sum()/float(len(actual_list))*100
print("Accuracy=",accur)
print(confusion_matrix(actual_list,pred_list))
