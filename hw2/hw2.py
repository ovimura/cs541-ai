# HW2

import math

class nbayes:
    def __init__(self, url_train, url_test):
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

    def c(self,i):
        '''
        It returns the classifier class based on the probability
        :param i:
        :return:
        '''
        return len([x for x in self.train if int(x[0]) == i])

    def pr_h(self, i):
        '''
        It calculates the probability of the given hypothesis.
        :param i:
        :return:
        '''
        return float(self.c(i)/len(self.train))

    def pr_f_h(self, j, k, i):
        '''
        It calculates the probability of the given feature index which equals given k for given hypothesis i.
        :param j:
        :param k:
        :param i:
        :return:
        '''
        return float((self.c(i) + self.f(j,k))/self.c(i))

    def f(self,j,k):
        '''
        It counts the number of instances where the feature at index j is equal to the given k
        :param j:
        :param k:
        :return:
        '''
        fj = 0
        for x in self.train:
            if int(x[j]) == k:
                fj += 1
        return fj

    def learn(self):
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
        L = self.L(c)
        if L[1] > L[0]:
            return 1
        return 0

def main():
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
    print("orig {}/{}({})".format(one_pred_true+zeros_pred_true, len(nb.test), round(float((one_pred_true+zeros_pred_true)/len(nb.test)),2)))

if __name__ == "__main__":
    main()
