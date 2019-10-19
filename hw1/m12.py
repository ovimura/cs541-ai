from collections import defaultdict
import time

preference_matrix = []
adjacent_nodes = {}
n = 10
pr = [] # solution of the run
ps = [] # persons

def process_preference_matrix(data):
    '''
    It processes the preference matrix.
    :param data: the dataset to be stored in the preference matrix
    :return: None
    '''
    global preference_matrix
    for k in range(1,n+1):
        row = data[k].split(' ')
        row[-1] = row[-1].replace('\n', '')
        preference_matrix.append(row)

def read_dataset(data):
    '''
    It reads the given dataset url and process the preference matrix
    :param data: the url of the datase
    :return: None
    '''
    with open(data, "r") as f:
        d = f.readlines()
    process_preference_matrix(d)

read_dataset("data/hw1-inst1.txt")

class Person:
    def __init__(self, seat, no, type, g, h):
        '''
        The constructor for the class Person
        :param seat: the seat where the person seats
        :param no: the number of the person
        :param type: the type of the person; 0 -> host, 1 -> guest
        :param g: the cost from the current seat to adjacent and opposite seat
        :param h: the heuristic of the current person
        '''
        self.seat = seat
        self.no = no
        self.type = type # 0 host, 1 guest
        self.g = g
        self.h = h

    def r(self):
        '''
        It returns the role of the person
        :return: 0 for host, 1 for guest
        '''
        return self.type

class Table:
    def __init__(self, adjacent_nodes):
        '''
        The constructor of the Table class
        :param adjacent_nodes: the list of all the adjacent nodes of the graph - Table
        '''
        self.adjacent_nodes = adjacent_nodes
        self.H = {}
        self.g = {}

    def get_adjacent_nodes(self, v):
        '''
        It gets the adjacent nodes for the given node.
        :param v: the given node
        :return: the adjacent nodes of the given node
        '''
        return self.adjacent_nodes[v]

    def h(self, v, n):
        '''
        The heuristic function with values taken from preference matrix
        :param v: the current node heuristic to be calculated
        :param n: the target node heuristic to be calculated
        :return: the heuristic value h(p1,p2) + h(p2,p1)
        '''
        self.H[(v[1],n[1])] = int(preference_matrix[v[1]-1][n[1]-1])
        self.H[(n[1],v[1])] = int(preference_matrix[n[1]-1][v[1]-1])
        return self.H[(n[1],v[1])]

    def astar(self, s, t):
        '''
          The frontier is a list of nodes which have been visited, but who's neighbors
          haven't all been inspected, starts off with the start node
          closed_list is a list of nodes which have been visited
          and who's neighbors have been inspected
        :param s: the start node to start the A* searching
        :param t: the target node to stop the A* searching
        :return: the path, if it exists from s, t with maximum cost
        '''
        frontier = set([s])
        closed_list = set([])
        self.g[s] = 0
        paths = {}
        paths[s] = s

        while len(frontier) > 0:
            n = None
            for v in frontier:
                if n == None or self.g[v] + self.h(v,n) > self.g[n] + self.h(n,v):
                    n = v
            if n == None:
                return None, None
            if n == t:
                the_path = []
                while paths[n] != n:
                    the_path.append(n)
                    n = paths[n]
                the_path.append(s)
                the_path.reverse()
                return the_path, self.adjacent_nodes
            for (m, w) in self.get_adjacent_nodes(n):
                if m not in frontier and m not in closed_list:
                    frontier.add(m)
                    paths[m] = n
                    self.g[m] = self.g[n] + w
                else:
                    if self.g[m] > self.g[n] + w:
                        self.g[m] = self.g[n] + w
                        paths[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            frontier.add(m)
            frontier.remove(n)
            closed_list.add(n)
        return None, None

def build_adj_list():
    '''
    It build the adjacent nodes list for 10 x 10 table.
    :return: the adjacent_nodes list
    '''
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
        return adjacent_nodes

def run_search(s,t):
    '''
    It runs the search from node s to node t.
    :param s: the start node to begin the search
    :param t: the target node to stop the search
    :return: a list of all nodes found with maximum cost from s to t
    '''
    global pr
    global ps
    global n
    build_adj_list()
    tbl = Table(adjacent_nodes)
    p, a = tbl.astar(s,t)
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
    for node in pr:
        ps.append(Person(node[0], node[1], 0 if int(node[1]) <= int(n/2) else 1, 0, 0))
    return pr

def score(ps):
    '''
    It computes the score for all the persons at the table by the following criteria
      1 point for every adjacent pair (seated next to each other) of people with one a host and the other a guest
      2 points for every opposite pair (seated across from each other) of people with one a host and the other a guest
      h(p1, p2) + h(p2, p1) points for every adjacent or opposite pair of people p1, p2
    :param ps: a list of all persons at the table
    :return: the score of the table
    '''
    global preference_matrix
    global n
    sc = 0
    h = 0
    r1 = sorted([x for x in ps if x.seat < n/2+1], key=lambda x:x.seat)
    r2 = sorted([x for x in ps if x.seat > n/2], key=lambda x:x.seat)
    for i, item in enumerate(r1):
        if item.seat == 1 or item.seat == n/2:
            if item.seat == 1 and r1[0].type != r1[1].type:
                sc += 2
            h += int(preference_matrix[int(r1[0].no)-1][int(r1[1].no)-1])
            h += int(preference_matrix[int(r1[1].no)-1][int(r1[0].no)-1])
            if item.seat == 1 and r1[0].type != r2[0].type:
                sc += 4
            h += int(preference_matrix[int(r1[0].no)-1][int(r2[0].no)-1])
            h += int(preference_matrix[int(r2[1].no)-1][int(r1[0].no)-1])
            if item.seat == n/2 and r1[int(n/2)-1].type != r1[int(n/2)-2].type:
                sc += 2
            h += int(preference_matrix[int(r1[int(n/2)-1].no)-1][int(r1[int(n/2)-2].no)-1])
            h += int(preference_matrix[int(r1[int(n/2)-2].no)-1][int(r1[int(n/2)-1].no)-1])
            if item.seat == n/2 and r1[int(n/2)-1].type != r2[int(n/2)-1].type:
                sc += 4
            h += int(preference_matrix[int(r1[int(n/2)-1].no)-1][int(r2[int(n/2)-1].no)-1])
            h += int(preference_matrix[int(r2[int(n/2)-1].no)-1][int(r1[int(n/2)-1].no)-1])
        else:
            if r1[i].type != r1[i+1].type:
                sc += 1
                h += int(preference_matrix[int(r1[i].no)-1][int(r1[int(i+1)].no)-1])
                h += int(preference_matrix[int(r1[int(i+1)].no)-1][int(r1[i].no)-1])
            if r1[i-1].type != r1[i].type:
                sc += 1
                h += int(preference_matrix[int(r1[i-1].no)-1][int(r1[int(i)].no)-1])
                h += int(preference_matrix[int(r1[int(i)].no)-1][int(r1[i-1].no)-1])
            if r1[i].type != r2[i].type:
                sc += 4
                h += int(preference_matrix[int(r1[i].no)-1][int(r2[int(i)].no)-1])
                h += int(preference_matrix[int(r2[int(i)].no)-1][int(r1[i].no)-1])
            if r2[i].type != r2[i+1].type:
                sc += 1
                h += int(preference_matrix[int(r2[i].no)-1][int(r2[int(i+1)].no)-1])
                h += int(preference_matrix[int(r2[int(i+1)].no)-1][int(r2[i].no)-1])
            if r2[i-1].type != r2[i].type:
                sc += 1
                h += int(preference_matrix[int(r2[i-1].no)-1][int(r2[int(i)].no)-1])
                h += int(preference_matrix[int(r2[int(i)].no)-1][int(r2[i-1].no)-1])
    sc += h
    return sc

def print_person_number_and_seat_number(ps):
    '''
    It prints <person number> and <seat number> with a space between
    :param ps: the list of all persons to be printed
    :return: None
    '''
    for x in range(len(ps)):
        print("{} {}".format(ps[x].no, ps[x].seat))

def clear_memory():
    '''
    It cleans the memory allocated during the program execution
    :return: None
    '''
    global adjacent_nodes
    global pr
    global ps
    adjacent_nodes.clear()
    pr.clear()
    ps.clear()

# print(run_search((1,1), (10,2)))
# print(score(ps))
# print_person_number_and_seat_number(ps)
# clear_memory()
#
# exit(3)

t1 = time.time()

for x in [1,2,3,4,5,6,7,8,9,10]:
    for y1 in range(1, 11):
        for z in [1,2,3,4,5,6,7,8,9,10]:
            for y in range(1,11):
                run_search((x,y1), (z,y))
                print(score(ps))
                print_person_number_and_seat_number(ps)
                clear_memory()
                print()
                if time.time() - t1 > 60:
                    exit(1)

