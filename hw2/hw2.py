# HW2


class NBayes:
    def __init__(self):
        with open('data/spect-orig.train.csv') as f:
            self.strain = f.readlines()
        with open('data/spect-orig.test.csv') as f:
            self.stest = f.readlines()

    def c(self,t):
        return 0

    def learn(self):
        pass


def main():
    nb = NBayes()
    print(nb.strain)
    print(nb.stest)


if __name__ == "__main__":
    main()

