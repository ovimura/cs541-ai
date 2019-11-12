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


    def c(self,t):
        '''
        It returns the classifier class based on the probability
        :param t:
        :return:
        '''
        ones = [x for x in t[1:] if int(x) == 1]
        zeros = [x for x in t[1:] if int(x) == 0]
        h0 = round(float(len(zeros)/(len(t)-1)),2)
        h1 = round(float(len(ones)/(len(t)-1)),2)
        return 1 if h1 > h0 else 0


    def f(self, idx, t):
        '''
        It returns the feature at given index from instance t
        :param idx: index of the feature
        :param t: instance from which to return the feature
        :return: the feature at the given index from given instance
        '''
        return t[int(1+idx)]


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
    print(nb.c(nb.train[0]))
    print(nb.stest[0])
    print(nb.f(2,nb.stest[0]))
    nb.learn()


if __name__ == "__main__":
    main()
