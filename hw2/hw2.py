# HW2


class nbayes:
    def __init__(self):
        self.train = []
        with open('data/spect-orig.train.csv') as f:
            t = f.readlines()
            print(len(t))
            for x in range(len(t)):
                a = t[x].replace('\n','').split(',')
                self.train.append(a)
        with open('data/spect-orig.test.csv') as f:
            self.stest = f.readlines()

    def c(self,t):
        return 0

    def learn(self):
        pass


def main():
    nb = nbayes()
    zeros = 0
    ones = 0
    c = 0
    for x in range(len(nb.train)):
        for k in range(1,23):
            print(nb.train[x][k])
            if int(nb.train[x][k]) == 0:
                zeros += 1
            elif int(nb.train[x][k]) == 1:
                ones += 1
        break
    i = 0
    for a in range(len(nb.train)):
        i+=1
        for b in range(a+1, len(nb.train)):
            if i == 2:
                break
            if nb.train[a] == nb.train[b]:
                c += 1
                print(b)
                print(nb.train[a] == nb.train[b])
        if i == 2:
            break;
    print(c)
    print(round(zeros/22,2))
    print(round(ones/22,2))
    print(nb.train[x])
#    print(nb.stest)


if __name__ == "__main__":
    main()

