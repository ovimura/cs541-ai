
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
    def __init__(self, n):
        self.n = n
        self.row1 = [Person(x,0) for x in range(1, n/2+1)]
        self.row2 = [Person(x,0) for x in range(n/2+1, n+1)]
        self.score = 0

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

    def get_score(self):
        for i in range(n/2-1):
            if self.r(self.row1[i]) == 0 and self.r(self.row1[i+1]) == 1:
                self.score += 1
            if self.r(self.row2[i]) == 0 and self.r(self.row2[i+1]) == 1:
                self.score += 1
            if self.r(self.row1[i]) == 0 and self.r(self.row2[i]) == 1:
                self.score += 2
            if self.r(self.row1[i]) == 1 and self.r(self.row2[i]) == 0:
                self.score += 2
        if self.r(self.row1[i+1]) == 0 and self.r(self.row2[i+1]) == 1:
            self.score += 2
        if self.r(self.row1[i+1]) == 1 and self.r(self.row2[i+1]) == 0:
            self.score += 2
        return self.score


    def search(self):
        global hosts
        global guests
        open_list = []
        closed_list = []
        open_list.append(self.row1[0])
        hs = []
        gs = []
        mx = 0
        j = 0
        seat_no = 1
        pos = 0
        while len(open_list)>0:
            c = open_list[0]
            c.seat = seat_no
            open_list.pop(0)
            if self.r(c) == 0 and len(open_list) == 0:
                for x in self.row2:
                    gs.append(x)
                for i in range(len(gs)):
                    print "i: " + str(i)
                    m = self.h(c,gs[i])
                    if m > mx:
                        mx = m
                        j = i
                tmp = gs[j]
                tmp.seat = seat_no+len(self.row1)
                self.row2.pop(j-len(self.row1))
                self.row2.insert(pos,tmp)
                gs.pop(j)
                pos += 1
                open_list.append(tmp)
            if self.r(c) == 1 and len(open_list) == 0:
                for x in self.row1:
                    if x.no != 1:
                        hs.append(x)
                mx = 0
                j = 0
                for i in range(len(hs)):
                    print "ii: " + str(i)
                    m = self.h(c,hs[i])
                    if m > mx:
                        mx = m
                        j = i
                tmp = hs[j]
                tmp.seat = seat_no + 5
                self.row2.insert(pos,tmp)
                pos += 1
                open_list.append(tmp)
            closed_list.append(c)
            closed_list.append(tmp)
            seat_no += 1

        for y in self.row2:
            print "y:: " + str(y.no)


        return self.score


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

    t = Table(n)
    p = Person(2,4)
    print p.no
    print "hosts:" + str(t.r(Person(2,1)))
    print t.h(Person(1,1), Person(10,2))
    print "get_score: " + str(t.get_score())
    print "a* search: " + str(t.search())
#    print r2
#    read("data/hw1-inst2.txt")
#    read("data/hw1-inst3.txt")


if __name__ == "__main__":
    main()
