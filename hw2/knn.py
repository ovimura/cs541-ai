# https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/

import numpy as np
import math
import csv
import operator
from sklearn.metrics import confusion_matrix, classification_report
#open training data set
file1 = open('data/spect-orig.train.csv','r')
data1 = csv.reader(file1)
train_data = np.array(list(data1)).astype(np.int)
#open test data set
file2 = open('data/spect-orig.test.csv','r')
data2 = csv.reader(file2)
test_data = np.array(list(data2)).astype(np.int)

def euclideanDistance(instance1,instance2,length):
    distance =0
    new1 = []
    new2 = []
    for j in range(1,len(instance1)):
        new1.append(instance1[j])
        new2.append(instance2[j])
    for x in range(length):
        distance +=pow((new1[x]-new2[x]),2)
    return math.sqrt(distance)

def getKNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(trainingSet[x], testInstance, length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=lambda tup: tup[1])
    #print(distances)
    #print(distances[0][1])
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def predictClass(train, t, num_neighbors):
    #print(t)
    neighbors = getKNeighbors(train, t, num_neighbors)
    #print(neighbors)
    output_values = [row[0] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

new_list = []
pred_list = []
actual_list = []

k = 5
print(len(test_data))

for i in range(test_data.shape[0]):
    pred_list.append(predictClass(train_data,test_data[i],k))
    actual_list.append(test_data[i][0])


print(test_data[0][0])
print(pred_list)
print(actual_list)

ones = 0
zeros = 0
for x in range(len(pred_list)):
    if pred_list[x] == actual_list[x] and pred_list[x] == 1:
        ones += 1
    if pred_list[x] == actual_list[x] and pred_list[x] == 0:
        zeros += 1





print(ones)
print(zeros)
print("orig {}/{}({})".format(ones+zeros, len(test_data), round(float((ones+zeros)/len(test_data)),2)))


# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0

print(accuracy_metric(actual_list,pred_list))
