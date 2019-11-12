# HW2

class nbayes:
    def __init__(self, url_train, url_test):
        self.F = []
        self.N = []
        self.train = []
        self.stest = []
        with open(url_train) as f:
            t = f.readlines()
            for x in range(len(t)):
                a = t[x].replace('\n','').split(',')
                self.train.append(a)
        with open(url_test) as f:
            t = f.readlines()
            for x in range(len(t)):
                a = t[x].replace('\n','').split(',')
                self.stest.append(a)


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
        fs = [0 for _ in range(len(self.train[0][1:]))]
        self.F = [fs,fs]
        print((self.N))
        print(self.F)
        print(len(self.F[0]))
        print(len(self.F[1]))


def main():
    nb = nbayes('data/spect-orig.train.csv', 'data/spect-orig.test.csv')
    print(nb.pr_h(0))
    print(nb.pr_h(1))
    print(nb.pr_f_h(1,0,1))
    print(nb.pr_f_h(1,1,1))


if __name__ == "__main__":
    main()
