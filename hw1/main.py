
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

def process_row(data, k):
    global n
    global r1
    global r2
    global guests
    for i in range(1, n/2+1):
        r1.append((i,data[k].split(' ')[i-1]))
    for j in range(1, n/2+1):
        r2.append((guests[j-1],data[k].replace('\n', ' ').split(' ')[n/2+j-1]))


def main():
    global hosts
    global guests
    global n
    global r1
    global r2
    d = read("data/hw1-inst2.txt")
    print_content(d)
    get_n(d)
    get_hosts(d)
    print hosts
    get_guests(d)
    print guests
    process_row(d, 1)
    print r1
    print r2
    read("data/hw1-inst2.txt")
    read("data/hw1-inst3.txt")


if __name__ == "__main__":
    main()
