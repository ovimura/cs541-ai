# CS541: HW2
# Student: Ovidiu Mura
# Date: Nov 14, 2019

import math

class knn(object):
    '''
    This class implements the k-Nearest-Neighbor learner.
    '''
    def __init__(self, url_train='data/spect-orig.train.csv', url_test='data/spect-orig.test.csv', k=5):
        '''
        The constructor of the knn instance.
        :param url_train:
        :param url_test:
        :param k:
        '''
        self.train = []
        self.test = []
        self.k = k
        with open(url_train) as f:
            t = f.readlines()
            for x in range(len(t)):
                a = t[x].replace('\n','').split(',')
                self.train.append(a)
        with open(url_test) as f:
            t = f.readlines()
            for x in range(len(t)):
                a = t[x].replace('\n','').split(',')
                self.test.append(a)

    def euclidean_distance(self, v1,v2):
        '''
        It calculates the Euclidean Distance for two given vectors.
        :param v1:
        :param v2:
        :return:
        '''
        d = 0.0
        u1 = []
        u2 = []
        for j in range(1,len(v1)):
            u1.append(v1[j])
            u2.append(v2[j])
        for x in range(len(v2)-1):
            d +=pow((float(u1[x])-float(u2[x])),2)
        return math.sqrt(d)

    def get_k_nearest_neighbors(self, train, t):
        ds = []
        ns = []
        for x in range(len(train)):
            d = self.euclidean_distance(train[x], t)
            ds.append((train[x], d))
        ds.sort(key=lambda tup: tup[1])
        for x in range(self.k):
            ns.append(ds[x][0])
        return ns

    def predict(self, train, t):
        ns = self.get_k_nearest_neighbors(train, t)
        output_values = [row[0] for row in ns]
        return max(set(output_values), key=output_values.count)

    def run(self):
        predicted = []
        actuals = []
        for i in range(len(self.test)):
            predicted.append(self.predict(self.train,self.test[i]))
            actuals.append(self.test[i][0])
        ones = 0
        zeros = 0
        for x in range(len(predicted)):
            if int(predicted[x]) == int(actuals[x]) and int(predicted[x]) == 1:
                ones += 1
            if int(predicted[x]) == int(actuals[x]) and int(predicted[x]) == 0:
                zeros += 1
        print("orig {}/{}({})  {}/{}({})  {}/{}({})".format(ones+zeros, len(self.test), round(float((ones+zeros)/len(self.test)),2), zeros,
                                                        len([x for x in actuals if int(x) == 0]), round(float(zeros/len([x for x in actuals if int(x) == 0])),2),
                                                        ones, len([x for x in actuals if int(x) == 1]), round(float(ones/len([x for x in actuals if int(x) == 1])),2)))

knn().run()
