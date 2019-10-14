
n = 0
hosts = []
guests = []

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

def process_rows(data):
    global n
    global r1
    global r2
    global guests
    r1 = []
    for k in range(n):
        row = data[k].split(' ')
        row[-1] = row[-1].replace('\n', '')
        r1.append(row)
#        for j in range(1, n/2+1):
#            r2[k].append((guests[j-1],data[k].replace('\n', ' ').split(' ')[n/2+j-1]))


class Person:
    def __init__(self):
        self.no = 0
        self.seat = 0

    def r(p):
        global hosts
        if p.no in hosts:
            return 0
        else:
            return 1

def main():
    global hosts
    global guests
    global n
    global r1
    global r2
    d = read("data/hw1-inst1.txt")
    print_content(d)
    get_n(d)
    get_hosts(d)
    print hosts
    get_guests(d)
    print guests
    process_rows(d)
    for a in range(len(r1)):
        print r1[a]


#    print r2
    read("data/hw1-inst2.txt")
    read("data/hw1-inst3.txt")


if __name__ == "__main__":
    main()
