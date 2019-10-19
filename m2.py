from collections import deque
import sys

class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {}
        for x in range(1,11):
            H['A'+str(x)] = 1
            H['B'+str(x)] = 10
            H['C'+str(x)] = 1
            H['D'+str(x)] = 1
            H['E'+str(x)] = 1
            H['F'+str(x)] = 1
            H['G'+str(x)] = 1
            H['H'+str(x)] = 1
            H['I'+str(x)] = 1
            H['J'+str(x)] = 1
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
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
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;
            if n == None:
                print('Path does not exist!')
                return None
            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            print (n)
            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                return reconst_path
            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                print('all neigh')
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    print(m)
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] < g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)
        print('Path does not exist!')
        return None

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
        adj_list1.append(('F'+str(x),0))
        adj_list1.append(('B'+str(x),0))
    for z in range(6,11):
        adj_list1.append(('F'+str(z),2))
        adj_list1.append(('B'+str(z),1))
    adjacency_list['A'+str(y)] = adj_list1

    for x in range(1,6):
        adj_list2.append(('A'+str(x),0))
        adj_list2.append(('C'+str(x),0))
        adj_list2.append(('G'+str(x),0))
    for z in range(6,11):
        adj_list2.append(('A'+str(z),1))
        adj_list2.append(('C'+str(z),1))
        adj_list2.append(('G'+str(z),2))
    adjacency_list['B'+str(y)] = adj_list2

    for x in range(1,6):
        adj_list3.append(('B'+str(x),0))
        adj_list3.append(('H'+str(x),0))
        adj_list3.append(('D'+str(x),0))
    for z in range(6,11):
        adj_list3.append(('B'+str(z),1))
        adj_list3.append(('H'+str(z),2))
        adj_list3.append(('D'+str(z),1))
    adjacency_list['C'+str(y)] = adj_list3

    for x in range(1,6):
        adj_list4.append(('C'+str(x),0))
        adj_list4.append(('E'+str(x),0))
        adj_list4.append(('I'+str(x),0))
    for z in range(6,11):
        adj_list4.append(('C'+str(z),1))
        adj_list4.append(('E'+str(z),1))
        adj_list4.append(('I'+str(z),2))
    adjacency_list['D'+str(y)] = adj_list4

    for x in range(1,6):
        adj_list5.append(('D'+str(x),0))
        adj_list5.append(('J'+str(x),0))
    for z in range(6,11):
        adj_list5.append(('D'+str(z),1))
        adj_list5.append(('J'+str(z),2))
    adjacency_list['E'+str(y)] = adj_list5

    for x in range(1,6):
        adj_list6.append(('A'+str(x),0))
        adj_list6.append(('G'+str(x),0))
    for z in range(6,11):
        adj_list6.append(('A'+str(z),2))
        adj_list6.append(('G'+str(z),1))
    adjacency_list['F'+str(y)] = adj_list6

    for x in range(1,6):
        adj_list7.append(('B'+str(x),0))
        adj_list7.append(('F'+str(x),0))
        adj_list7.append(('H'+str(x),0))
    for z in range(6,11):
        adj_list7.append(('B'+str(z),2))
        adj_list7.append(('F'+str(z),1))
        adj_list7.append(('H'+str(z),1))
    adjacency_list['G'+str(y)] = adj_list7

    for x in range(1,6):
        adj_list8.append(('G'+str(x),0))
        adj_list8.append(('I'+str(x),0))
        adj_list8.append(('C'+str(x),0))
    for z in range(6,11):
        adj_list8.append(('G'+str(z),1))
        adj_list8.append(('I'+str(z),1))
        adj_list8.append(('C'+str(z),2))
    adjacency_list['H'+str(y)] = adj_list8

    for x in range(1,6):
        adj_list9.append(('H'+str(x),0))
        adj_list9.append(('J'+str(x),0))
        adj_list9.append(('D'+str(x),0))
    for z in range(6,11):
        adj_list9.append(('H'+str(z),1))
        adj_list9.append(('J'+str(z),1))
        adj_list9.append(('D'+str(z),2))
    adjacency_list['I'+str(y)] = adj_list9

    for x in range(1,6):
        adj_list10.append(('I'+str(x),0))
        adj_list10.append(('E'+str(x),0))
    for z in range(6,11):
        adj_list10.append(('I'+str(z),1))
        adj_list10.append(('E'+str(z),2))
    adjacency_list['J'+str(y)] = adj_list10


graph1 = Graph(adjacency_list)
graph1.a_star_algorithm(sys.argv[1], sys.argv[2])


