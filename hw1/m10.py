from collections import defaultdict

preference_matrix = []
adjacent_nodes = {}
n = 10
pr = [] # solution of the run
ps = [] # persons

def process_preference_matrix(data):
    global preference_matrix
    for k in range(1,n+1):
        row = data[k].split(' ')
        row[-1] = row[-1].replace('\n', '')
        preference_matrix.append(row)

def read_dataset(data):
    global preference_matrix
    with open(data, "r") as f:
        d = f.readlines()
    process_preference_matrix(d)
    # for ss in range(len(preference_matrix)):
    #     print(preference_matrix[ss])

read_dataset("data/hw1-inst1.txt")

class Person:
    def __init__(self, seat, no, type, g, h):
        self.seat = seat
        self.no = no
        self.type = type # 0 host, 1 guest
        self.g = g
        self.h = h

class Host(Person):
    def r(self):
        return self.type

class Guest(Person):
    def r(self):
        return self.type

class Table:
    def __init__(self, adjacent_nodes):
        self.adjacent_nodes = adjacent_nodes
        self.H = {}
        self.g = {}

    def get_adjacent_nodes(self, v):
        return self.adjacent_nodes[v]

    def update_adjacency_list(self, v):
        ''' 
            Remove all related seats and people numbers from the space states
        '''
        keys = [x for x in self.adjacency_nodes.keys() if x != v and x[1:] != v[1:] and x[:1] != v[:1]]
        keys.insert(0,v)
        excl = [x for x in self.adjacency_nodes.keys() if x not in keys]
        for k in excl:
            del self.adjacency_nodes[k]
        for k in excl:
            for key in self.adjacency_nodes.keys():
                if k in [x[0] for x in self.adjacency_nodes[key]]:
                    for idx, kk in enumerate(self.adjacency_nodes[key]):
                        if k == kk[0]:
                            self.adjacency_nodes[key].remove(kk)

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

    def h(self, v, n):
        self.H[(v[1],n[1])] = int(preference_matrix[v[1]-1][n[1]-1])
        self.H[(n[1],v[1])] = int(preference_matrix[n[1]-1][v[1]-1])
        return self.H[(n[1],v[1])]

    def astar(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        self.g = {}
        self.g[start_node] = 0
        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None
            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or self.g[v] + self.h(v,n) > self.g[n] + self.h(n,v):
                    n = v
            if n == None:
                #print('Path does not exist!')
                return None, None
            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                # print('Path found: {}'.format(reconst_path))
                return reconst_path, self.adjacent_nodes
            # for all neighbors of the current node do
            for (m, weight) in self.get_adjacent_nodes(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    self.g[m] = self.g[n] + weight
                    # self.update_adjacency_list(m)
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if self.g[m] > self.g[n] + weight:
                        self.g[m] = self.g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            # print(parents)
            open_list.remove(n)
            closed_list.add(n)
        #print('Path does not exist!')
        return None, None

def build_adj_list():
    global adjacent_nodes
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
                adj_list1.append(((1,x),0))
                adj_list1.append(((2,x),0))
            else:
                adj_list1.append(((6,x),2))
                adj_list1.append(((2,x),1))
        for z in range(6,11):
            if y > 5:
                adj_list1.append(((6,z),0))
                adj_list1.append(((2,z),0))
            else:
                adj_list1.append(((6,z),2))
                adj_list1.append(((2,z),1))
        adjacent_nodes[(1,y)] = adj_list1

        for x in range(1,6):
            if y < 6:
                adj_list2.append(((1,x),0))
                adj_list2.append(((3,x),0))
                adj_list2.append(((7,x),0))
            else:
                adj_list2.append(((1,x),1))
                adj_list2.append(((3,x),1))
                adj_list2.append(((7,x),2))
        for z in range(6,11):
            if y > 5:
                adj_list2.append(((1,z),0))
                adj_list2.append(((3,z),0))
                adj_list2.append(((7,z),0))
            else:
                adj_list2.append(((1,z),1))
                adj_list2.append(((3,z),1))
                adj_list2.append(((7,z),2))
        adjacent_nodes[(2,y)] = adj_list2

        for x in range(1,6):
            if y < 6:
                adj_list3.append(((2,x),0))
                adj_list3.append(((8,x),0))
                adj_list3.append(((4,x),0))
            else:
                adj_list3.append(((2,x),1))
                adj_list3.append(((4,x),1))
                adj_list3.append(((8,x),2))
        for z in range(6,11):
            if y > 5:
                adj_list3.append(((2,z),0))
                adj_list3.append(((8,z),0))
                adj_list3.append(((4,z),0))
            else:
                adj_list3.append(((2,z),1))
                adj_list3.append(((8,z),2))
                adj_list3.append(((4,z),1))
        adjacent_nodes[(3,y)] = adj_list3

        for x in range(1,6):
            if y < 6:
                adj_list4.append(((3,x),0))
                adj_list4.append(((5,x),0))
                adj_list4.append(((9,x),0))
            else:
                adj_list4.append(((3,x),1))
                adj_list4.append(((5,x),1))
                adj_list4.append(((9,x),2))
        for z in range(6,11):
            if y > 5:
                adj_list4.append(((3,z),0))
                adj_list4.append(((5,z),0))
                adj_list4.append(((9,z),0))
            else:
                adj_list4.append(((3,z),1))
                adj_list4.append(((5,z),1))
                adj_list4.append(((9,z),2))
        adjacent_nodes[(4,y)] = adj_list4

        for x in range(1,6):
            if y < 6:
                adj_list5.append(((4,x),0))
                adj_list5.append(((10,x),0))
            else:
                adj_list5.append(((4,x),1))
                adj_list5.append(((10,x),2))
        for z in range(6,11):
            if y > 5:
                adj_list5.append(((4,z),0))
                adj_list5.append(((10,z),0))
            else:
                adj_list5.append(((4,z),1))
                adj_list5.append(((10,z),2))
        adjacent_nodes[(5,y)] = adj_list5
    
        for x in range(1,6):
            if y < 6:
                adj_list6.append(((1,x),0))
                adj_list6.append(((7,x),0))
            else:
                adj_list6.append(((1,x),2))
                adj_list6.append(((7,x),1))
        for z in range(6,11):
            if y > 5:
                adj_list6.append(((1,z),0))
                adj_list6.append(((7,z),0))
            else:
                adj_list6.append(((1,z),2))
                adj_list6.append(((7,z),1))
        adjacent_nodes[(6,y)] = adj_list6
    
        for x in range(1,6):
            if y < 6:
                adj_list7.append(((2,x),0))
                adj_list7.append(((6,x),0))
                adj_list7.append(((8,x),0))
            else:
                adj_list7.append(((2,x),2))
                adj_list7.append(((6,x),1))
                adj_list7.append(((8,x),1))
        for z in range(6,11):
            if y > 5:
                adj_list7.append(((2,z),0))
                adj_list7.append(((6,z),0))
                adj_list7.append(((8,z),0))
            else:
                adj_list7.append(((2,z),2))
                adj_list7.append(((6,z),1))
                adj_list7.append(((8,z),1))
        adjacent_nodes[(7,y)] = adj_list7
    
        for x in range(1,6):
            if y < 6:
                adj_list8.append(((7,x),0))
                adj_list8.append(((9,x),0))
                adj_list8.append(((3,x),0))
            else:
                adj_list8.append(((7,x),1))
                adj_list8.append(((9,x),1))
                adj_list8.append(((3,x),2))
        for z in range(6,11):
            if y > 5:
                adj_list8.append(((7,z),0))
                adj_list8.append(((9,z),0))
                adj_list8.append(((3,z),0))
            else:
                adj_list8.append(((7,z),1))
                adj_list8.append(((9,z),1))
                adj_list8.append(((3,z),2))
        adjacent_nodes[(8,y)] = adj_list8

        for x in range(1,6):
            if y < 6:
                adj_list9.append(((8,x),0))
                adj_list9.append(((10,x),0))
                adj_list9.append(((4,x),0))
            else:
                adj_list9.append(((8,x),1))
                adj_list9.append(((10,x),1))
                adj_list9.append(((4,x),2))
        for z in range(6,11):
            if y > 5:
                adj_list9.append(((8,z),0))
                adj_list9.append(((10,z),0))
                adj_list9.append(((4,z),0))
            else:
                adj_list9.append(((8,z),1))
                adj_list9.append(((10,z),1))
                adj_list9.append(((4,z),2))
        adjacent_nodes[(9,y)] = adj_list9
    
        for x in range(1,6):
            if y < 6:
                adj_list10.append(((9,x),0))
                adj_list10.append(((5,x),0))
            else:
                adj_list10.append(((9,x),1))
                adj_list10.append(((5,x),2))
        for z in range(6,11):
            if y > 5:
                adj_list10.append(((9,z),0))
                adj_list10.append(((5,z),0))
            else:
                adj_list10.append(((9,z),1))
                adj_list10.append(((5,z),2))
        adjacent_nodes[(10,y)] = adj_list10

def run_search(s,t):
    global pr
    global n
    build_adj_list()
    graph1 = Table(adjacent_nodes)
    p, a = graph1.astar(s,t)
    keys = [x for x in a.keys()]
    pr = p
    alln = range(1,n+1)
    if len(pr) != n:
        x1 = [x[0] for x in pr]
        y1 = [x[1] for x in pr]
        try:
            D1 = defaultdict(list)
            for i, item in enumerate(y1):
                D1[item].append(i)
            D1 = {k:v for k,v in D1.items() if len(v)>1}
            if len(D1.keys()) > 0:
                for d in D1.keys():
                    del pr[D1[d][0]]
            D2 = defaultdict(list)
            for i, item in enumerate(x1):
                D2[item].append(i)
            D2 = {k:v for k,v in D2.items() if len(v)>1}
            if len(D2.keys()) > 0:
                for d in D2.keys():
                    del pr[D2[d][0]]
        except:
            pass

        # adding the vertices not included into A* search to fill the table's seats
        x = [x for x in alln if x not in [y[0] for y in pr]]
        y = [y for y in alln if y not in [y[1] for y in pr]]
        while(len(x) != 0 and len(y) != 0):
            for k in keys:
                if k[0] in x and k[1] in y:
                    x.remove(k[0])
                    y.remove(k[1])
                    pr.append(k)
    print(len(pr))
    return pr

def print_person_number_and_seat_number(ps):
    for x in range(len(ps)):
        print("{} {}".format(ps[x].no, ps[x].seat))

def clear_memory():
    global adjacent_nodes
    global pr
    #global ps
    adjacent_nodes.clear()
    pr.clear()
    #ps.clear()



print(run_search((1,1), (10,2)))
print_person_number_and_seat_number(ps)
clear_memory()

exit(3)

for x in [1,2,3,4,5,6,7,8,9,10]:
    for y1 in range(1, 11):
        for z in [1,2,3,4,5,6,7,8,9,10]:
            for y in range(1,11):
                print(run_search((x,y1), (z,y)))
                print_person_number_and_seat_number(ps)
                clear_memory()

