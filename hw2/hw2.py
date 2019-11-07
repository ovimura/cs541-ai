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
                print(self.train)
                exit(3)
        with open('data/spect-orig.test.csv') as f:
            self.stest = f.readlines()

    def c(self,t):
        return 0

    def learn(self):
        pass


def main():
    nb = nbayes()
    print(nb.train)
    print(nb.stest)


if __name__ == "__main__":
    main()

