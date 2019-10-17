from collections import deque

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

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        gprev = 0
        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) > g[n] + self.h(n):
                    n = v;
                    gprev += g[n]
            print ("n::: " + str(n))
            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
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
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                print ("m: " + str(m))
                print ("wei: " + str(weight))
                print ("n: " + str(n))
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    print ("g[m]: " + str(g[m]) + str(m))
                    print ("g[n]: " + str(g[n]) + str(n))
                    print ("m weight: " + str(weight))
                    if g[m] > g[n] + weight:
                        print ("--")
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
#    'A1': [('F2', 0), ('F3', 0), ('F4', 0), ('F5', 0), ('F6', 2), ('F7', 2), ('F8', 2), ('F9',2), ('F10',2), ('B2',0),('B3',0),('B4',0),('B5',0),('B6',1),('B7',1),('B8',1),('B9',1),('B10',1)],
#    'B1': [('A1', 0), ('C', 0), ('G', 2)],
#    'C': [('B1', 0), ('D', 0), ('H', 2)],
#    'D': [('C', 0), ('E', 0), ('I', 2)],
#    'E': [('D', 0), ('J', 2)],
#    'F1': [('A1', 2), ('G', 0)],
#    'G': [('B1', 2), ('F1', 0), ('H', 0)],
#    'H': [('G', 0), ('I', 0), ('C', 2)],
#    'I': [('H', 0), ('J', 0), ('D', 2)],
#    'J': [('I', 0), ('E', 2)]
#}
for y in range(1,11):
    adj_list = []
    for x in range(1,6):
        adj_list.append(('F'+str(x),0))
        adj_list.append(('B'+str(x),0))
    for z in range(6,11):
        adj_list.append(('F'+str(z),2))
        adj_list.append(('B'+str(z),1))
    adjacency_list['A'+str(y)] = adj_list
    adj_list.clear()

    for x in range(1,6):
        adj_list.append(('A'+str(x),0))
        adj_list.append(('C'+str(x),0))
        adj_list.append(('G'+str(x),0))
    for z in range(6,11):
        adj_list.append(('A'+str(z),1))
        adj_list.append(('C'+str(z),1))
        adj_list.append(('G'+str(z),2))
    adjacency_list['B'+str(y)] = adj_list
    adj_list.clear()

    for x in range(1,6):
        adj_list.append(('B'+str(x),0))
        adj_list.append(('H'+str(x),0))
        adj_list.append(('D'+str(x),0))
    for z in range(6,11):
        adj_list.append(('B'+str(z),1))
        adj_list.append(('H'+str(z),1))
        adj_list.append(('D'+str(z),2))
    adjacency_list['C'+str(y)] = adj_list



# print(adjacency_list)

# exit(2)

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A1', 'J')



