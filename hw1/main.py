
n = 0
hosts = []
guests = []

preference_matrix = []

r1 = []
r2 = []

def get_n(data):
    global n
    n = int(data[0][:-1])
    print(n)
    if (n % 2) != 0:
        raise Exception("error: text file has not even number n of people on the first line!")

def get_hosts(data):
    global hosts
    hosts.extend( [x for x in range(1,n/2+1)])

def get_guests(data):
    global guests
    guests = [x for x in range((n/2)+1, n+1)]

def read(p):
    with open(p, "r") as f:
        data = f.readlines()
    i = 0
    return data

def print_content(a):
    i = 0
    while i<len(a):
        print "%s" % a[i][:-1]
        i += 1

def process_preference_matrix(data):
    global n
    global preference_matrix
    global guests
    r1 = []
    for k in range(1,n+1):
        row = data[k].split(' ')
        row[-1] = row[-1].replace('\n', '')
        preference_matrix.append(row)


class Person:
    def __init__(self, no, seat):
        self.no = no
        self.seat = seat


class Table:
    def __init__(self):
        self.row1 = []
        self.row2 = []

    def r(self, p):
        global hosts
        if p.no in hosts:
            return 0
        else:
            return 1

    def h(self, p1, p2):
        global preference_matrix
        if p1.no == 0 or p2.no == 0:
            raise Exception("error: incorrect person number")
        return preference_matrix[p1.no-1][p2.no-1]


def main():
    global hosts
    global guests
    global n
    global preference_matrix
    d = read("data/hw1-inst1.txt")
    print_content(d)
    get_n(d)
    get_hosts(d)
    print hosts
    get_guests(d)
    print guests
    process_preference_matrix(d)
    for a in range(len(preference_matrix)):
        print preference_matrix[a]

    t = Table()
    p = Person(2,4)
    print p.no
    print t.r(Person(1,1))
    print t.h(Person(1,1), Person(1,2))
#    print r2
#    read("data/hw1-inst2.txt")
#    read("data/hw1-inst3.txt")


if __name__ == "__main__":
    main()
