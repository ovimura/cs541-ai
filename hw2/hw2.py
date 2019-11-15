# CS541: HW2 - Heart Anomalies
# Student: Ovidiu Mura
# Date: Nov 14, 2019

import math

class nbayes(object):
    '''
    This class is an implementation of the Naive Bayesian reasoning.
    '''
    def __init__(self, url_train, url_test):
        '''
        The constructor of this instance. Initializes the F, N arrays and
        loads the training/testing datasets.
        :param url_train: url of the training dataset file
        :param url_test: url of the testing dataset file
        '''
        self.F = []
        self.N = []
        self.train = []
        self.test = []
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

    def learn(self):
        '''
        It learns the data by counting the positive features in a 2-D array F,
        and counting the instance classification in array N, for a given feature and
        instance respectively.
        :return: a tuple with the 2-D array feature counts, and 1-D array instance counts
        '''
        self.N = [0,0]
        fs1 = [0 for _ in range(1,len(self.train[0][0:]))]
        fs2 = [0 for _ in range(1,len(self.train[0][0:]))]
        self.F = [fs1,fs2]
        for t in self.train:
            self.N[int(t[0])] += 1
            for j in range(1,len(t)):
                if int(t[j]) == 1:
                    self.F[int(t[0])][j-1] += 1
        return (self.N, self.F)

    def L(self, c):
        '''
        It applies Naive Bayesian reasoning for a new give instance.
        :param c: new instance to be classified
        :return: likelihood that the instance is Class-0 or Class-1
        '''
        L = [0,0]
        for i in [0,1]:
            L[i] = math.log(self.N[i] + 0.5) - math.log(self.N[0] + self.N[1] + 0.5)
            for j in range(1,len(c)):
                s = self.F[i][j-1]
                if int(c[j]) == 0:
                    s = self.N[i] - s
                L[i] = L[i] + math.log(s+0.5) - math.log(self.N[i] + 0.5)
        return L

    def classify(self, c):
        '''
        It classifies a new given instance.
        :param c: new instance
        :return: the predicted class
        '''
        L = self.L(c)
        if L[1] > L[0]:
            return 1
        return 0

def spect_orig():
    '''
    It learns and predict orig dataset.
    :return: None
    '''
    nb = nbayes('data/spect-orig.train.csv', 'data/spect-orig.test.csv')
    a, b = nb.learn()
    predicted_list = []
    actual_list = []
    one_pred_true = 0
    zeros_pred_true = 0
    for i in range(len(nb.test)):
        d = nb.classify(nb.test[i])
        actual_list.append(int(nb.test[i][0]))
        if d == 1:
            predicted_list.append(1)
        else:
            predicted_list.append(0)
    for x in range(len(predicted_list)):
        if predicted_list[x] == actual_list[x] and predicted_list[x] == 1:
            one_pred_true += 1
        if predicted_list[x] == actual_list[x] and predicted_list[x] == 0:
            zeros_pred_true += 1
    print("orig {}/{}({})  {}/{}({})  {}/{}({})".format(one_pred_true+zeros_pred_true, len(nb.test), round(float((one_pred_true+zeros_pred_true)/len(nb.test)),2), zeros_pred_true,
                                                        len([x for x in actual_list if int(x) == 0]), round(float(zeros_pred_true/len([x for x in actual_list if int(x) == 0])),2),
                                                        one_pred_true, len([x for x in actual_list if int(x) == 1]), round(float(one_pred_true/len([x for x in actual_list if int(x) == 1])),2)))

def spect_itg():
    '''
    It learns and predicts itg dataset.
    :return: None
    '''
    nb = nbayes('data/spect-itg.train.csv', 'data/spect-itg.test.csv')
    a, b = nb.learn()
    predicted_list = []
    actual_list = []
    one_pred_true = 0
    zeros_pred_true = 0
    for i in range(len(nb.test)):
        d = nb.classify(nb.test[i])
        actual_list.append(int(nb.test[i][0]))
        if d == 1:
            predicted_list.append(1)
        else:
            predicted_list.append(0)
    for x in range(len(predicted_list)):
        if predicted_list[x] == actual_list[x] and predicted_list[x] == 1:
            one_pred_true += 1
        if predicted_list[x] == actual_list[x] and predicted_list[x] == 0:
            zeros_pred_true += 1
    print("itg {}/{}({})  {}/{}({})  {}/{}({})".format(one_pred_true+zeros_pred_true, len(nb.test), round(float((one_pred_true+zeros_pred_true)/len(nb.test)),2), zeros_pred_true,
                                                        len([x for x in actual_list if int(x) == 0]), round(float(zeros_pred_true/len([x for x in actual_list if int(x) == 0])),2),
                                                        one_pred_true, len([x for x in actual_list if int(x) == 1]), round(float(one_pred_true/len([x for x in actual_list if int(x) == 1])),2)))

def spect_resplit():
    '''
    It learns and predicts resplit dataset.
    :return: None
    '''
    nb = nbayes('data/spect-resplit.train.csv', 'data/spect-resplit.test.csv')
    a, b = nb.learn()
    predicted_list = []
    actual_list = []
    one_pred_true = 0
    zeros_pred_true = 0
    for i in range(len(nb.test)):
        d = nb.classify(nb.test[i])
        actual_list.append(int(nb.test[i][0]))
        if d == 1:
            predicted_list.append(1)
        else:
            predicted_list.append(0)
    for x in range(len(predicted_list)):
        if predicted_list[x] == actual_list[x] and predicted_list[x] == 1:
            one_pred_true += 1
        if predicted_list[x] == actual_list[x] and predicted_list[x] == 0:
            zeros_pred_true += 1
    print("resplit {}/{}({})  {}/{}({})  {}/{}({})".format(one_pred_true+zeros_pred_true, len(nb.test), round(float((one_pred_true+zeros_pred_true)/len(nb.test)),2), zeros_pred_true,
                                                        len([x for x in actual_list if int(x) == 0]), round(float(zeros_pred_true/len([x for x in actual_list if int(x) == 0])),2),
                                                        one_pred_true, len([x for x in actual_list if int(x) == 1]), round(float(one_pred_true/len([x for x in actual_list if int(x) == 1])),2)))

def spect_resplit_itg():
    '''
    It learns and predicts resplit-itg dataset.
    :return: None
    '''
    nb = nbayes('data/spect-resplit-itg.train.csv', 'data/spect-resplit-itg.test.csv')
    a, b = nb.learn()
    predicted_list = []
    actual_list = []
    one_pred_true = 0
    zeros_pred_true = 0
    for i in range(len(nb.test)):
        d = nb.classify(nb.test[i])
        actual_list.append(int(nb.test[i][0]))
        if d == 1:
            predicted_list.append(1)
        else:
            predicted_list.append(0)
    for x in range(len(predicted_list)):
        if predicted_list[x] == actual_list[x] and predicted_list[x] == 1:
            one_pred_true += 1
        if predicted_list[x] == actual_list[x] and predicted_list[x] == 0:
            zeros_pred_true += 1
    print("resplit-itg {}/{}({})  {}/{}({})  {}/{}({})".format(one_pred_true+zeros_pred_true, len(nb.test), round(float((one_pred_true+zeros_pred_true)/len(nb.test)),2), zeros_pred_true,
                                                        len([x for x in actual_list if int(x) == 0]), round(float(zeros_pred_true/len([x for x in actual_list if int(x) == 0])),2),
                                                        one_pred_true, len([x for x in actual_list if int(x) == 1]), round(float(one_pred_true/len([x for x in actual_list if int(x) == 1])),2)))

def spect():
    '''
    It learns and predicts SPECT dataset.
    :return: None
    '''
    nb = nbayes('data/SPECT.train', 'data/SPECT.test')
    a, b = nb.learn()
    predicted_list = []
    actual_list = []
    one_pred_true = 0
    zeros_pred_true = 0
    for i in range(len(nb.test)):
        d = nb.classify(nb.test[i])
        actual_list.append(int(nb.test[i][0]))
        if d == 1:
            predicted_list.append(1)
        else:
            predicted_list.append(0)
    for x in range(len(predicted_list)):
        if predicted_list[x] == actual_list[x] and predicted_list[x] == 1:
            one_pred_true += 1
        if predicted_list[x] == actual_list[x] and predicted_list[x] == 0:
            zeros_pred_true += 1
    print("spect {}/{}({})  {}/{}({})  {}/{}({})".format(one_pred_true+zeros_pred_true, len(nb.test), round(float((one_pred_true+zeros_pred_true)/len(nb.test)),2), zeros_pred_true,
                                                        len([x for x in actual_list if int(x) == 0]), round(float(zeros_pred_true/len([x for x in actual_list if int(x) == 0])),2),
                                                        one_pred_true, len([x for x in actual_list if int(x) == 1]), round(float(one_pred_true/len([x for x in actual_list if int(x) == 1])),2)))


def main():
    '''
    The program's main method executes the learn/predict datasets functions.
    :return: None
    '''
    spect_orig()
    spect_itg()
    spect_resplit()
    spect_resplit_itg()
    spect()

if __name__ == "__main__":
    main()
