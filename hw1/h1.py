
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
    hosts.extend( [x for x in range(1,int(n/2)+1)])

def get_guests(data):
    global guests
    guests = [x for x in range(int(n/2)+1, n+1)]

def read(p):
    with open(p, "r") as f:
        data = f.readlines()
    i = 0
    return data

def print_content(a):
    i = 0
    while i<len(a):
        print ("%s" % a[i][:-1])
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
        self.c = 0

class Table:
    def __init__(self, n):
        self.n = n
        self.row1 = [Person(x,0) for x in range(1, int(n/2)+1)]
        self.row2 = [Person(x,0) for x in range(int(n/2)+1, n+1)]
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
        hs = []
        gs = []
        mx = -1000
        hpos = 0
        gpos = 0
        seat_no = 1
        r = 0
        for x in self.row1:
            hs.append(x)
        for y in self.row2:
            gs.append(y)
        open_list.append(hs[0])
        hs.pop(0)
        while len(open_list)>0:
            c = open_list[0]
            open_list.pop(0)
            print (c.no)
            if self.r(c) == 0 and len(open_list) == 0:
                for i in range(len(gs)):
                    m = self.h(c,gs[i])
                    if int(m) > int(mx):
                        mx = m
                        j = i
                tmp = gs[j]
                tmp.seat = seat_no+len(self.row1)
                for k,itm in enumerate(self.row2):
                    if itm.no == tmp.no:
                        self.row2.pop(k)
                if r == 0:
                    self.row2.insert(gpos,tmp)
                else:
                    self.row1.insert(gpos,tmp)
                gs.pop(j)
                open_list.append(tmp)
                hpos += 1
                mx = -1000
                if len(hs) ==0 and len(gs) ==0:
                    break
                print ("gs size: " + str(len(gs)) + str(len(hs)))
            elif self.r(c) == 1 and len(open_list) == 0:
                print ("guest" + str(c.no))
#                if c.no == 6:
#                    break
                for i in range(len(hs)):
                    m = self.h(c,hs[i])
                    print ("m: " + str(m) + " mx: " + str(mx))
                    print (int(m)>int(mx))
                    print (m)
                    print (mx)
                    if int(m) > int(mx):
                        mx = m
                        j = i
                        print ("MX: " + str(mx))
                tmp = hs[j]
                print (j)
                print (hs[j].no)
                print ([x.no for x in hs])
                tmp.seat = seat_no + len(self.row1)
                for k, itm in enumerate(self.row2):
                    if itm.no == tmp.no:
                        self.row2.pop(k)
                for k, itm in enumerate(self.row1):
                    if itm.no == tmp.no:
                        self.row1.pop(k)
                gpos += 1
                if r == 0:
                    r += 1
                    self.row2.insert(hpos, tmp)
                else:
                    self.row1.insert(hpos, tmp)
                    r -= 1
                hs.pop(j)
                mx = -1000
                if len(hs)==0 and len(gs)==0:
                    break
                print ("hs size: " + str(len(hs)) + str(len(hs)))
                open_list.append(tmp)
            closed_list.append(c)
            seat_no += 1
        print ([x.no for x in hs])
        print ([x.no for x in gs])
        return self.score


def main():
    global hosts
    global guests
    global n
    global preference_matrix
    d = read("data/hw1-inst3.txt")
    print_content(d)
    get_n(d)
    get_hosts(d)
    print (hosts)
    get_guests(d)
    print (guests)
    process_preference_matrix(d)
    for a in range(len(preference_matrix)):
        print (preference_matrix[a])

    t = Table(n)
    t.search()
    print ([n.no for n in t.row1])
    print ([m.no for m in t.row2])

#    print r2
#    read("data/hw1-inst2.txt")
#    read("data/hw1-inst3.txt")


if __name__ == "__main__":
    main()
