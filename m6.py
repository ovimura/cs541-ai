from collections import deque
import sys

preference_matrix = []

n = 10

def process_preference_matrix(data):
    global preference_matrix
    for k in range(1,n+1):
        row = data[k].split(' ')
        row[-1] = row[-1].replace('\n', '')
        preference_matrix.append(row)

with open("hw1/data/hw1-inst1.txt", "r") as f:
    d = f.readlines()

process_preference_matrix(d)

for ss in range(len(preference_matrix)):
    print(preference_matrix[ss])


class Graph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def update_adjacency_list(self, v):
        ''' 
            Remove all related seats and people numbers from the space states
        '''
        keys = [x for x in self.adjacency_list.keys() if x != v and x[1:] != v[1:] and x[:1] != v[:1]]
        keys.insert(0,v)
        excl = [x for x in self.adjacency_list.keys() if x not in keys]
        for k in excl:
            del self.adjacency_list[k]
        for k in excl:
            for key in self.adjacency_list.keys():
                if k in [x[0] for x in self.adjacency_list[key]]:
                    for idx, kk in enumerate(self.adjacency_list[key]):
                        if k == kk[0]:
                            self.adjacency_list[key].remove(kk)


    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {}
        for x in range(1,11):
            H['A'+str(x)] = 1
            H['B'+str(x)] = 1
            H['C'+str(x)] = 1
            H['D'+str(x)] = 1
            H['E'+str(x)] = 1
            H['F'+str(x)] = 1
            H['G'+str(x)] = 1
            H['H'+str(x)] = 1
            H['I'+str(x)] = 1
            H['J'+str(x)] = 1
        return H[n]

#    def h(self, v, n):
#        return n,v


    def astar(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}
        g[start_node] = 0
        # parents contains an adjacency map of all nodes
        parents = {}
        sub_sol = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            print('-')
            n = None
            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) > g[n] + self.h(n):
                    n = v;
            if n == None:
                print('Path does not exist!')
                return None, None
            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []
                s = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path, self.adjacency_list
            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                    self.update_adjacency_list(m)
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            # print(parents)
            open_list.remove(n)
            closed_list.add(n)
        print('Path does not exist!')
        return None, None

adjacency_list = {}

for y in range(1,11):
    adj_list1 = []
    adj_list2 = []
    adj_list3 = []
    adj_list4 = []
    adj_list5 = []
    adj_list6 = []
    adj_list7 = []
    adj_list8 = []
    adj_list9 = []
    adj_list10 = []

    for x in range(1,6):
        if y < 6:
            adj_list1.append(('F'+str(x),0))
            adj_list1.append(('B'+str(x),0))
        else:
            adj_list1.append(('F'+str(x),2))
            adj_list1.append(('B'+str(x),1))
    for z in range(6,11):
        if y > 5:
            adj_list1.append(('F'+str(z),0))
            adj_list1.append(('B'+str(z),0))
        else:
            adj_list1.append(('F'+str(z),2))
            adj_list1.append(('B'+str(z),1))
    adjacency_list['A'+str(y)] = adj_list1

    for x in range(1,6):
        if y < 6:
            adj_list2.append(('A'+str(x),0))
            adj_list2.append(('C'+str(x),0))
            adj_list2.append(('G'+str(x),0))
        else:
            adj_list2.append(('A'+str(x),1))
            adj_list2.append(('C'+str(x),1))
            adj_list2.append(('G'+str(x),2))
    for z in range(6,11):
        if y > 5:
            adj_list2.append(('A'+str(z),0))
            adj_list2.append(('C'+str(z),0))
            adj_list2.append(('G'+str(z),0))
        else:
            adj_list2.append(('A'+str(z),1))
            adj_list2.append(('C'+str(z),1))
            adj_list2.append(('G'+str(z),2))
    adjacency_list['B'+str(y)] = adj_list2

    for x in range(1,6):
        if y < 6:
            adj_list3.append(('B'+str(x),0))
            adj_list3.append(('H'+str(x),0))
            adj_list3.append(('D'+str(x),0))
        else:
            adj_list3.append(('B'+str(x),1))
            adj_list3.append(('D'+str(x),1))
            adj_list3.append(('H'+str(x),2))
    for z in range(6,11):
        if y > 5:
            adj_list3.append(('B'+str(z),0))
            adj_list3.append(('H'+str(z),0))
            adj_list3.append(('D'+str(z),0))
        else:
            adj_list3.append(('B'+str(z),1))
            adj_list3.append(('H'+str(z),2))
            adj_list3.append(('D'+str(z),1))
    adjacency_list['C'+str(y)] = adj_list3

    for x in range(1,6):
        if y < 6:
            adj_list4.append(('C'+str(x),0))
            adj_list4.append(('E'+str(x),0))
            adj_list4.append(('I'+str(x),0))
        else:
            adj_list4.append(('C'+str(x),1))
            adj_list4.append(('E'+str(x),1))
            adj_list4.append(('I'+str(x),2))
    for z in range(6,11):
        if y > 5:
            adj_list4.append(('C'+str(z),0))
            adj_list4.append(('E'+str(z),0))
            adj_list4.append(('I'+str(z),0))
        else:
            adj_list4.append(('C'+str(z),1))
            adj_list4.append(('E'+str(z),1))
            adj_list4.append(('I'+str(z),2))
    adjacency_list['D'+str(y)] = adj_list4

    for x in range(1,6):
        if y < 6:
            adj_list5.append(('D'+str(x),0))
            adj_list5.append(('J'+str(x),0))
        else:
            adj_list5.append(('D'+str(x),1))
            adj_list5.append(('J'+str(x),2))
    for z in range(6,11):
        if y > 5:
            adj_list5.append(('D'+str(z),0))
            adj_list5.append(('J'+str(z),0))
        else:
            adj_list5.append(('D'+str(z),1))
            adj_list5.append(('J'+str(z),2))
    adjacency_list['E'+str(y)] = adj_list5

    for x in range(1,6):
        if y < 6:
            adj_list6.append(('A'+str(x),0))
            adj_list6.append(('G'+str(x),0))
        else:
            adj_list6.append(('A'+str(x),2))
            adj_list6.append(('G'+str(x),1))
    for z in range(6,11):
        if y > 5:
            adj_list6.append(('A'+str(z),0))
            adj_list6.append(('G'+str(z),0))
        else:
            adj_list6.append(('A'+str(z),2))
            adj_list6.append(('G'+str(z),1))
    adjacency_list['F'+str(y)] = adj_list6

    for x in range(1,6):
        if y < 6:
            adj_list7.append(('B'+str(x),0))
            adj_list7.append(('F'+str(x),0))
            adj_list7.append(('H'+str(x),0))
        else:
            adj_list7.append(('B'+str(x),2))
            adj_list7.append(('F'+str(x),1))
            adj_list7.append(('H'+str(x),1))
    for z in range(6,11):
        if y > 5:
            adj_list7.append(('B'+str(z),0))
            adj_list7.append(('F'+str(z),0))
            adj_list7.append(('H'+str(z),0))
        else:
            adj_list7.append(('B'+str(z),2))
            adj_list7.append(('F'+str(z),1))
            adj_list7.append(('H'+str(z),1))
    adjacency_list['G'+str(y)] = adj_list7

    for x in range(1,6):
        if y < 6:
            adj_list8.append(('G'+str(x),0))
            adj_list8.append(('I'+str(x),0))
            adj_list8.append(('C'+str(x),0))
        else:
            adj_list8.append(('G'+str(x),1))
            adj_list8.append(('I'+str(x),1))
            adj_list8.append(('C'+str(x),2))
    for z in range(6,11):
        if y > 5:
            adj_list8.append(('G'+str(z),0))
            adj_list8.append(('I'+str(z),0))
            adj_list8.append(('C'+str(z),0))
        else:
            adj_list8.append(('G'+str(z),1))
            adj_list8.append(('I'+str(z),1))
            adj_list8.append(('C'+str(z),2))
    adjacency_list['H'+str(y)] = adj_list8

    for x in range(1,6):
        if y < 6:
            adj_list9.append(('H'+str(x),0))
            adj_list9.append(('J'+str(x),0))
            adj_list9.append(('D'+str(x),0))
        else:
            adj_list9.append(('H'+str(x),1))
            adj_list9.append(('J'+str(x),1))
            adj_list9.append(('D'+str(x),2))
    for z in range(6,11):
        if y > 5:
            adj_list9.append(('H'+str(z),0))
            adj_list9.append(('J'+str(z),0))
            adj_list9.append(('D'+str(z),0))
        else:
            adj_list9.append(('H'+str(z),1))
            adj_list9.append(('J'+str(z),1))
            adj_list9.append(('D'+str(z),2))
    adjacency_list['I'+str(y)] = adj_list9

    for x in range(1,6):
        if y < 6:
            adj_list10.append(('I'+str(x),0))
            adj_list10.append(('E'+str(x),0))
        else:
            adj_list10.append(('I'+str(x),1))
            adj_list10.append(('E'+str(x),2))
    for z in range(6,11):
        if y > 5:
            adj_list10.append(('I'+str(z),0))
            adj_list10.append(('E'+str(z),0))
        else:
            adj_list10.append(('I'+str(z),1))
            adj_list10.append(('E'+str(z),2))
    adjacency_list['J'+str(y)] = adj_list10

nn = 10

graph1 = Graph(adjacency_list)
graph1.update_adjacency_list(sys.argv[1])
graph1.update_adjacency_list(sys.argv[2])

p, a = graph1.astar(sys.argv[1], sys.argv[2])

excluded = []

if len(p) < nn:
    for k in ['A','B','C','D','E','F','G','H','I','J']:
        if k not in [x[:1] for x in p]:
            excluded.append(k)

print("Excluded letter states:" + str(excluded))
p1 = []
b = {}
st = []

for k in p:
    del a[k]

for k in p:
    print (k)
    for key in a.keys():
        if k in [x[0] for x in a[key]]:
            for idx, kk in enumerate(a[key]):
                if k == kk[0]:
                    a[key].remove(kk)

#print("a keys")
#print(a.keys())

#print(a)

if len(excluded) > 2:
    g2 = Graph(a)
    for e in excluded:
        st.append([x for x in a.keys() if x[:1] == e])
#    print(st)
    i = st[0]
    j = st[-1]
    p1, b = g2.astar(i[0],j[0])

pr = []

if p != None and p1 != None:
    print("SOLUTION FOUND: ")
    pr = p+p1
    print(pr)
else:
    p1 = [x for x in a.keys()]
    pr = p+p1
    print ("SOLUTION FOUND: |" + str(pr) + "|")

# print (b)

#with open("hw1/data/hw1-inst1.txt", "r") as f:
#    d = f.readlines()

#process_preference_matrix(d)

#for ss in range(len(preference_matrix)):
#    print(preference_matrix[ss])






i = 0
j = 0
total = 0

class Person:
    def __init__(self, seat, no, g, h):
        self.seat = seat
        self.no = no
        self.g = g
        self.h = h

ps = []

for kkk in range(len(pr)):
    if pr[kkk][:1] == 'A':
        i = 1
        j = int(pr[kkk][1:])
        v=preference_matrix[i-1][j-1]
        print("({},{}):{}".format(i,j,v))
        ps.append(Person('A',j, 0,0))
    elif pr[kkk][:1] == 'B':
        i = 2
        j = int(pr[kkk][1:])
        v=preference_matrix[i-1][j-1]
        print("({},{}): {}".format(i,j,v))
        ps.append(Person('B',j,0,0))
    elif pr[kkk][:1] == 'C':
        i = 3
        j = int(pr[kkk][1:])
        v=preference_matrix[i-1][j-1]
        print("({},{}): {}".format(i,j,v))
        ps.append(Person('C',j,0,0))
    elif pr[kkk][:1] == 'D':
        i = 4
        j = int(pr[kkk][1:])
        v=preference_matrix[i-1][j-1]
        print("({},{}): {}".format(i,j,v))
        ps.append(Person('D',j,0,0))
    elif pr[kkk][:1] == 'E':
        i = 5
        j = int(pr[kkk][1:])
        v=preference_matrix[i-1][j-1]
        print("({},{}): {}".format(i,j,v))
        ps.append(Person('E',j,0,0))
    elif pr[kkk][:1] == 'F':
        i = 6
        j = int(pr[kkk][1:])
        v=preference_matrix[i-1][j-1]
        print("({},{}): {}".format(i,j,v))
        ps.append(Person('F',j,0,0))
    elif pr[kkk][:1] == 'G':
        i = 7
        j = int(pr[kkk][1:])
        v=preference_matrix[i-1][j-1]
        print("({},{}): {}".format(i,j,v))
        ps.append(Person('G',j,0,0))
    elif pr[kkk][:1] == 'H':
        i = 8
        j = int(pr[kkk][1:])
        v=preference_matrix[i-1][j-1]
        print("({},{}): {}".format(i,j,v))
        ps.append(Person('H',j,0,0))
    elif pr[kkk][:1] == 'I':
        i = 9
        j = int(pr[kkk][1:])
        v=preference_matrix[i-1][j-1]
        print("({},{}): {}".format(i,j,v))
        ps.append(Person('I',j,0,0))

cost = 0
for ii in range(len(ps)):
    if ps[ii].seat == 'A':
        pera = int(ps[ii].no)
        for x in range(len(ps)):
            if ps[x].seat == 'B':
                perb = int(ps[x].no)
                if perb <= 5 and pera >5 or perb >5 and pera <= 5:
                    cost +=1
                    cost += int(preference_matrix[pera][perb]) + int(preference_matrix[perb][pera])
            if ps[x].seat == 'F':
                perc = int(ps[x].no)
                if pera <= 5 and perc > 5 or pera >5 and perc <=5:
                    cost +=1
                    cost += int(preference_matrix[pera][perc]) + int(preference_matrix[perc][pera])
        print(cost)
    if ps[ii].seat == 'B':
        perb = ps[ii].no
        for x in range(len(ps)):
            if ps[x].seat == 'A':
                pera = ps[x].no
                if perb <= 5 and pera > 5 or pera <= 5 and perb > 5:
                    cost +=1
                    cost += int(preference_matrix[pera][perb]) + int(preference_matrix[perb][pera])
            if ps[x].seat == 'C':
                perc = ps[x].no
                if perb <= 5 and perc > 5 or perc <= 5 and perb > 5:
                    cost += 1
                    cost += int(preference_matrix[perc][perb]) + int(preference_matrix[perb][perc])
            if ps[x].seat == 'G':
                perg = ps[x].no
                if perb <= 5 and perg > 5 or perg <= 5 and perb > 5:
                    cost += 2
                    cost += int(preference_matrix[perg][perb]) + int(preference_matrix[perb][perg])
        print(cost)
    if ps[ii].seat == 'C':
        perc = ps[ii].no
        for x in range(len(ps)):
            if ps[x].seat == 'B':
                perb = ps[x].no
                if perc <= 5 and perb > 5 or perc > 5 and perb <= 5:
                    cost += 1
                    cost += int(preference_matrix[perc][perb]) + int(preference_matrix[perb][perc])
            if ps[x].seat == 'D':
                perd = ps[x].no
                if perc > 5 and perd <= 5 or perd > 5 and perc <= 5:
                    cost += 1
                    cost += int(preference_matrix[perc][perd]) + int(preference_matrix[perd][perc])
            if ps[x].seat == 'H':
                perh = ps[x].no
                if perc <= 5 and perh > 5 or perc > 5 and perh <= 5:
                    cost += 2
                    cost += int(preference_matrix[perc][perh]) + int(preference_matrix[perh][perc])
        print(cost)
    if ps[ii].seat == 'D':
        perd = ps[ii].no
        for x in range(len(ps)):
            if ps[x].seat == 'C':
                perc = ps[x].no
                if perd <= 5 and perc > 5 or perd > 5 and perc <= 5:
                    cost += 1
                    cost += int(preference_matrix[perd][perc]) + int(preference_matrix[perc][perd])
            if ps[x].seat == 'E':
                pere = ps[x].no
                if pere <= 5 and perd > 5 or pere > 5 and perd <= 5:
                    cost += 1
                    cost += int(preference_matrix[perd][pere]) + int(preference_matrix[pere][perd])
            if ps[x].seat == 'I':
                peri = ps[x].no
                if peri <= 5 and perd > 5 or perd <= 5 and peri > 5:
                    cost += 2
                    cost += int(preference_matrix[perd][peri]) + int(preference_matrix[peri][perd])
        print(cost)
    if ps[ii].seat == 'E':
        pere = ps[ii].no
        for x in range(len(ps)):
            if ps[x].seat == 'D':
                perd = ps[x].no
                if perd > 5 and pere <= 5 or perd <= 5 and pere > 5:
                    cost += 1
                    cost += int(preference_matrix[pere][perd]) + int(preference_matrix[perd][pere])
            if ps[x].seat == 'J':
                perj = ps[x].no
                if pere <= 5 and perj > 5 or pere > 5 and perj <= 5:
                    cost += 2
                    cost += int(preference_matrix[pere][perj]) + int(preference_matrix[perj][pere])
        print(cost)
    if ps[ii].seat == 'F':
        perf = ps[ii].no
        for x in range(len(ps)):
            if ps[x].seat == 'A':
                pera = ps[x].no
                if perf > 5 and pera <= 5 or perf <= 5 and pera > 5:
                    cost += 2
                    cost += int(preference_matrix[pera][perf]) + int(preference_matrix[perf][pera])
            if ps[x].seat == 'G':
                perg = ps[x].no
                if perf > 5 and perg <= 5 or perf <= 5 and perg > 5:
                    cost += 1
                    cost += int(preference_matrix[perf][perg]) + int(preference_matrix[perg][perf])
        print(cost)
    if ps[ii].seat == 'G':
        perg = ps[ii].no
        for x in range(len(ps)):
            if ps[x].seat == 'F':
                perf = ps[x].no
                if perf > 5 and perg <= 5 or perf <= 5 and perg > 5:
                    cost += 1
                    cost += int(preference_matrix[perg][perf]) + int(preference_matrix[perf][perg])
            if ps[x].seat == 'H':
                perh = ps[x].no
                if perh > 5 and perg <= 5 or perg > 5 and perh <= 5:
                    cost += 1
                    cost += int(preference_matrix[perg][perh]) + int(preference_matrix[perh][perg])
            if ps[x].seat == 'B':
                perb = ps[x].no
                if perb > 5 and perg <= 5 or perb <= 5 and perg > 5:
                    cost += 2
                    cost += int(preference_matrix[perg][perb]) + int(preference_matrix[perb][perg])
        print(cost)
    if ps[ii].seat == 'H':
        perh = ps[ii].no
        for x in range(len(ps)):
            if ps[x].seat == 'G':
                perg = ps[x].no
                if perh > 5 and perg <= 5 or perg > 5 and perh <= 5:
                    cost += 1
                    cost += int(preference_matrix[perh][perg]) + int(preference_matrix[perg][perh])
            if ps[x].seat == 'I':
                peri = ps[x].no
                if perh <= 5 and peri > 5 or peri <= 5 and perh > 5:
                    cost += 1
                    cost += int(preference_matrix[perh][peri]) + int(preference_matrix[peri][perh])
            if ps[x].seat == 'C':
                perc = ps[x].no
                if perh <= 5 and perc > 5 or perc <= 5 and perh > 5:
                    cost += 2
                    cost += int(preference_matrix[perh][perc]) + int(preference_matrix[perc][perh])
        print(cost)
    if ps[ii].seat == 'I':
        peri = ps[ii].no
        for x in range(len(ps)):
            if ps[x].seat == 'H':
                perh = ps[x].no
                if peri <= 5 and perh > 5 or peri > 5 and perh <= 5:
                    cost +=1
                    cost += int(preference_matrix[peri][perh]) + int(preference_matrix[perh][peri])
            if ps[x].seat == 'J':
                perj = ps[x].no
                if perj <= 5 and peri > 5 or perj > 5 and peri <= 5:
                    cost += 1
                    cost += int(preference_matrix[peri][perj]) + int(preference_matrix[perj][peri])
            if ps[x].seat == 'D':
                perd = ps[x].no
                if peri <= 5 and perd > 5 or peri > 5 and perd <= 5:
                    cost += 2
                    cost += int(preference_matrix[peri][perd]) + int(preference_matrix[perd][peri])
        print(cost)
    if ps[ii].seat == 'J':
        perj = ps[ii].no
        for x in range(len(ps)):
            if ps[x].seat == 'I':
                peri = ps[x].no
                if peri <= 5 and perj > 5 or peri > 5 and perj <= 5:
                    cost += 1
                    cost += int(preference_matrix[perj][peri]) + int(preference_matrix[peri][perj])
            if ps[x].seat == 'E':
                pere = ps[x].no
                if pere <= 5 and perj > 5 or pere > 5 and perj <= 5:
                    cost += 2
                    cost += int(preference_matrix[perj][pere]) + int(preference_matrix[pere][perj])
        print(cost)


print("COST:")

print(cost)
