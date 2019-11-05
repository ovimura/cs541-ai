'''
CS541: Artificial Intelligence
Student: Ovidiu Mura
Email: mura@pdx.edu
Date: Oct 20, 2019
Assignment 1: Dinner Party
'''

from collections import defaultdict
import time
import sys
import collections

preference_matrix = []
adjacent_nodes = {}
n = 0
ps = [] # persons

def process_preference_matrix(data):
    '''
    It processes the preference matrix.
    :param data: the dataset to be stored in the preference matrix
    :return: None
    '''
    global preference_matrix
    global n
    n = int(data[0].replace('\n', ''))
    for k in range(1,n+1):
        row = data[k].split(' ')
        row[-1] = row[-1].replace('\n', '')
        preference_matrix.append(row)
    # for ss in range(len(preference_matrix)):
    #     print(preference_matrix[ss])

def read_dataset(data):
    '''
    It reads the given dataset url and process the preference matrix
    :param data: the url of the datase
    :return: None
    '''
    with open(data, "r") as f:
        d = f.readlines()
    process_preference_matrix(d)

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

if len(sys.argv) != 2:
    print("usage: python3 hw1.py <running_time_in_seconds> <url_of_the_dataset>")
    exit(-1)

#sec = int(sys.argv[1])

read_dataset(sys.argv[1])

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
        It is an informed search algorithm which starts at a specific start node and
        parses the graph to the target node having the largest cost path. It maintains a tree of
        paths originating at the start node and terminates at the target.
        Time complexity in worst case in performance is O(|E|) = O(b^d), where E is the number of edges,
        b is the branching factor (the avg number of successors per state) and d is the depth of the solution
        (in this case is the most expensive path)
        Time complexity in worst case in space is O(|V|) = O(b^d), where V is the number of vertexes, b - branching
        factor, and d - depth of solution
        frontier - a set of nodes visited but who's neighbors haven't been inspected
        closed_list - a set of nodes visited and who's neighbors have been inspected
        :param s: the start node to start the A* searching
        :param t: the target node to stop the A* searching
        :return: the path, if it exists from s, t with maximum cost
        '''
        frontier = set([s])
        closed_list = set([])
        self.g[s] = 0
        # all nodes' adjacency map
        paths = {}
        paths[s] = s

        while len(frontier) > 0:
            n = None
            # find a node with the highest value of evaluation function f() = g(v) + h(v,n)
            for v in frontier:
                if n == None or self.g[v] + self.h(v,n) > self.g[n] + self.h(n,v):
                    n = v
            if n == None:
                return None, None
            # if the current node is the target, then start
            # the construction of the final optimal path
            if n == t:
                the_path = []
                while paths[n] != n:
                    the_path.append(n)
                    n = paths[n]
                the_path.append(s)
                the_path.reverse()
                return the_path, self.adjacent_nodes
            # for all the adjacent nodes
            for (m, w) in self.get_adjacent_nodes(n):
                # if the current node isn't in both frontier and closed_list
                # then add it to the frontier and add n as it's parent
                if m not in frontier and m not in closed_list:
                    frontier.add(m)
                    paths[m] = n
                    self.g[m] = self.g[n] + w
                # else, check if there is higher value path by visiting n first,
                # then m and if it is update the parent and g data
                # also, if the node is in the closed_list, moved it to the frontier
                else:
                    if self.g[m] > self.g[n] + w:
                        self.g[m] = self.g[n] + w
                        paths[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            frontier.add(m)
            # remove n from the frontier, and add it to the closed_list,
            # all adjacent nodes were inspected
            frontier.remove(n)
            closed_list.add(n)
        return None, None

def build_adj_list_n_10():
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

def build_adj_list_n_30():
    '''
    It builds the adjacent nodes list for 10 x 10 table.
    :return: the adjacent_nodes list
    '''
    global adjacent_nodes
    for s in range(1,31):
        for y in range(1,31):
            adj_list = []
            if s == 1:
                for x in range(1,16):
                    if y < 16:
                        adj_list.append(((1,x),0))
                        adj_list.append(((2,x),0))
                    else:
                        adj_list.append(((16,x),2))
                        adj_list.append(((2,x),1))
                for z in range(16,31):
                    if y > 15:
                        adj_list.append(((1,z),0))
                        adj_list.append(((2,z),0))
                    else:
                        adj_list.append(((16,z),2))
                        adj_list.append(((2,z),1))
                adjacent_nodes[(s,y)] = adj_list.copy()
                adj_list.clear()
            elif s > 1 and s < 15:
                for x in range(1,16):
                    if y < 16:
                        adj_list.append(((s-1,x),0))
                        adj_list.append(((s+1,x),0))
                        adj_list.append(((s+15,x),0))
                    else:
                        adj_list.append(((s-1,x),1))
                        adj_list.append(((s+1,x),1))
                        adj_list.append(((s+15,x),2))
                for z in range(16,31):
                    if y > 15:
                        adj_list.append(((s-1,z),0))
                        adj_list.append(((s+1,z),0))
                        adj_list.append(((s+15,z),0))
                    else:
                        adj_list.append(((s-1,z),1))
                        adj_list.append(((s+1,z),1))
                        adj_list.append(((s+15,z),2))
                adjacent_nodes[(s,y)] = adj_list.copy()
                adj_list.clear()
            elif s == 15:
                for x in range(1,16):
                    if y < 16:
                        adj_list.append(((14,x),0))
                        adj_list.append(((30,x),0))
                    else:
                        adj_list.append(((14,x),1))
                        adj_list.append(((30,x),2))
                for z in range(16,31):
                    if y > 15:
                        adj_list.append(((14,z),0))
                        adj_list.append(((30,z),0))
                    else:
                        adj_list.append(((14,z),1))
                        adj_list.append(((30,z),2))
                adjacent_nodes[(s,y)] = adj_list.copy()
                adj_list.clear()
            elif s == 16:
                for x in range(1,16):
                    if y < 16:
                        adj_list.append(((1,x),0))
                        adj_list.append(((17,x),0))
                    else:
                        adj_list.append(((1,x),2))
                        adj_list.append(((17,x),1))
                for z in range(16,31):
                    if y > 15:
                        adj_list.append(((1,z),0))
                        adj_list.append(((17,z),0))
                    else:
                        adj_list.append(((1,z),2))
                        adj_list.append(((17,z),1))
                adjacent_nodes[(s,y)] = adj_list.copy()
                adj_list.clear()
            elif s > 16 and s < 30:
                for x in range(1,16):
                    if y < 16:
                        adj_list.append(((s-15,x),0))
                        adj_list.append(((s-1,x),0))
                        adj_list.append(((s+1,x),0))
                    else:
                        adj_list.append(((s-15,x),2))
                        adj_list.append(((s-1,x),1))
                        adj_list.append(((s+1,x),1))
                for z in range(16,31):
                    if y > 15:
                        adj_list.append(((s-15,z),0))
                        adj_list.append(((s-1,z),0))
                        adj_list.append(((s+1,z),0))
                    else:
                        adj_list.append(((s-15,z),2))
                        adj_list.append(((s-1,z),1))
                        adj_list.append(((s+1,z),1))
                adjacent_nodes[(s,y)] = adj_list.copy()
                adj_list.clear()
            elif s == 30:
                for x in range(1,6):
                    if y < 6:
                        adj_list.append(((29,x),0))
                        adj_list.append(((15,x),0))
                    else:
                        adj_list.append(((29,x),1))
                        adj_list.append(((15,x),2))
                for z in range(6,11):
                    if y > 5:
                        adj_list.append(((29,z),0))
                        adj_list.append(((15,z),0))
                    else:
                        adj_list.append(((29,z),1))
                        adj_list.append(((15,z),2))
                adjacent_nodes[(s,y)] = adj_list.copy()
                adj_list.clear

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
    global adjacent_nodes
    if n == 10:
        build_adj_list_n_10()
    else:
        build_adj_list_n_30()
    tbl = Table(adjacent_nodes)
    p, a = tbl.astar(s,t)

    alln = [x for x in range(1, n+1)]
    keys = [x for x in a.keys()]

    # remove the duplicate seats or persons from the A* found path
    p1 = [x[0] for x in p]
    p2 = [x[1] for x in p]

    dd=[item for item, count in collections.Counter(p1).items() if count > 1]
    while(len(dd) != 0):
        for d in p:
            if d[0] == dd[0]:
                p.remove(d)
        p1 = [x[0] for x in p]
        dd = [item for item, count in collections.Counter(p1).items() if count > 1]

    ee=[item for item, count in collections.Counter(p2).items() if count > 1]
    while(len(ee) != 0):
        for e in p:
            if e[1] == ee[0]:
                p.remove(e)
        p2 = [x[1] for x in p]
        ee = [item for item, count in collections.Counter(p2).items() if count > 1]

    # adding vertices not included into A*
    x = [xx for xx in alln if xx not in [xxx[0] for xxx in p]]
    x1 = [xx1 for xx1 in alln if xx1 not in [xxx[1] for xxx in p]]

    while(len(x) != 0 and len(x1) != 0):
        for k in keys:
            if k[0] in x and k[1] in x1 and k not in p:
                x.remove(k[0])
                x1.remove(k[1])
                p.append(k)

    for node in p:
        ps.append(Person(node[0], node[1], 0 if int(node[1]) <= int(n/2) else 1, 0, 0))
    return p

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
                sc += 1
                h += int(preference_matrix[int(r1[0].no)-1][int(r1[1].no)-1])
                h += int(preference_matrix[int(r1[1].no)-1][int(r1[0].no)-1])
            if item.seat == 1 and r1[0].type != r2[0].type:
                sc += 2
                h += int(preference_matrix[int(r1[0].no)-1][int(r2[0].no)-1])
                h += int(preference_matrix[int(r2[1].no)-1][int(r1[0].no)-1])
            if item.seat == n/2 and r1[int(n/2)-1].type != r1[int(n/2)-2].type:
                sc += 1
                h += int(preference_matrix[int(r1[int(n/2)-1].no)-1][int(r1[int(n/2)-2].no)-1])
                h += int(preference_matrix[int(r1[int(n/2)-2].no)-1][int(r1[int(n/2)-1].no)-1])
            if item.seat == n/2 and r1[int(n/2)-1].type != r2[int(n/2)-1].type:
                sc += 2
                h += int(preference_matrix[int(r1[int(n/2)-1].no)-1][int(r2[int(n/2)-1].no)-1])
                h += int(preference_matrix[int(r2[int(n/2)-1].no)-1][int(r1[int(n/2)-1].no)-1])
            if item.seat == n/2 and r2[int(n/2)-1].type != r2[int(n/2)-2].type:
                sc += 2
                h += int(preference_matrix[int(r2[int(n/2)-1].no)-1][int(r2[int(n/2)-2].no)-1])
                h += int(preference_matrix[int(r2[int(n/2)-2].no)-1][int(r2[int(n/2)-1].no)-1])
            if item.seat == n/2 and (r1[int(n/2)-1].type == r1[int(n/2)-2].type or r1[int(n/2)-1].type == r2[int(n/2)-1].type or r2[int(n/2)-1].type == r2[int(n/2)-2].type):
                h += int(preference_matrix[int(r1[int(n/2)-1].no)-1][int(r2[int(n/2)-1].no)-1])
                h += int(preference_matrix[int(r2[int(n/2)-1].no)-1][int(r1[int(n/2)-1].no)-1])
            elif item.seat == 1 and (r1[0].type == r1[1].type or r1[0].type == r2[0].type or r2[0].type == r2[1].type):
                h += int(preference_matrix[int(r1[0].no)-1][int(r2[0].no)-1])
                h += int(preference_matrix[int(r2[0].no)-1][int(r1[0].no)-1])
        else:
            if r1[i].type != r1[i+1].type:
                sc += 1
                h += int(preference_matrix[int(r1[i].no)-1][int(r1[int(i+1)].no)-1])
                h += int(preference_matrix[int(r1[int(i+1)].no)-1][int(r1[i].no)-1])
            if r1[i-1].type != r1[i].type:
                sc += 1
            if r1[i].type != r2[i].type:
                sc += 2
                h += int(preference_matrix[int(r1[i].no)-1][int(r2[int(i)].no)-1])
                h += int(preference_matrix[int(r2[int(i)].no)-1][int(r1[i].no)-1])
            if r2[i].type != r2[i+1].type:
                sc += 1
                h += int(preference_matrix[int(r2[i].no)-1][int(r2[int(i+1)].no)-1])
                h += int(preference_matrix[int(r2[int(i+1)].no)-1][int(r2[i].no)-1])
            if r2[i-1].type != r2[i].type:
                sc += 1
            if r1[i].type == r1[i+1].type or r1[i].type == r2[i].type or r1[i].type == r1[i-1].type or r2[i].type == r2[i+1].type or r2[i].type == r2[i-1].type:
                h += int(preference_matrix[int(r1[int(i)].no)-1][int(r2[i].no)-1])
                h += int(preference_matrix[int(r2[int(i)].no)-1][int(r1[i].no)-1])
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
    global ps
    adjacent_nodes.clear()
    ps.clear()

t1 = time.time()
ma = 0
for x in range(1,n+1):
    for y1 in range(1,n+1):
        for z in range(1,n+1):
            for y in range(1,n+1):
                run_search((x,y1), (z,y))
                m = score(ps)
                #print(m)
                if m > ma:
                    ma = m
                #print_person_number_and_seat_number(ps)
                clear_memory()
                #print()
                #t2 = time.time() - t1
                #if t2 > sec:
                #    print("max score: {}; duration: {}".format(ma, t2))
                #    exit(0)
        print(ma)
