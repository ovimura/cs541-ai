#### CS541 - Artificial Intelligence
#### Student: Ovidiu Mura
#### Email: mura@pdx.edu
#### Date: Oct 20, 2019
#### Assignment 1: Dinner Party
##### Requirements: https://moodle.cs.pdx.edu/mod/assign/view.php?id=146

#### To execute the project run the following command:
###### make
#### 
#### The make command will execute all 3 goals, each goal executing one of the 3 data instances
#### 

I implemented the solution using Python programming language on the following hardware specifications:

###### Server: linux.cs.pdx.edu
###### OS: Ubuntu 18.04.3 LTS
###### Memory: 24GiB, 3 x 8GiB SODIMM DDR3 Synchronous 1600 MHz
###### Architecture:        x86_64
###### CPU op-mode(s):      32-bit, 64-bit
###### Byte Order:          Little Endian
###### CPU(s):              12
###### On-line CPU(s) list: 0-11
###### Thread(s) per core:  1
###### Core(s) per socket:  1
###### Socket(s):           12
###### NUMA node(s):        1
###### Vendor ID:           GenuineIntel
###### CPU family:          6
###### Model:               58
###### Model name:          Intel Xeon E3-12xx v2 (Ivy Bridge)
###### Stepping:            9
###### CPU MHz:             2499.998
###### BogoMIPS:            4999.99
###### Hypervisor vendor:   KVM
###### Virtualization type: full
###### L1d cache:           32K
###### L1i cache:           32K
###### L2 cache:            4096K
###### NUMA node0 CPU(s):   0-11

Abstraction: The table represents an undirected weighted graph with each seat representing a node. Weights are 1,2, and
0 assigned based on the combination person types they form as described in requirements.

The adjacent nodes are generated based on the value of n, and the A* search is performed on this graph. 

I use a combination of all possible (seat, person) as input for the program.

I read the datasets (3 datasets, n=10, n=30, n=30) from the 'data' directory which is placed in the current directory.
I store the content of the dataset representing the preference matrix in memory and also the program reads the value of
'n' from the first line of the dataset file.

Once the n is known, I generate the adjacent nodes of the graph. The table represents an undirected weighted graph with
weights as described in the requirements, 1 for different adjacent persons types (host/guest) and 1 for different opposite adjacent persons types.
I perform a Complete search useing a different version of A* searrch algorithm, select the path of maximum cost, for each selection, such as: 
###### self.g[v] + self.h(v,n) > self.g[n] + self.h(n,v), line 124 in hw1.py file

After the A* search returns the found nodes, I check the result and add the missing nodes which represents a combination
of (seats, person number), run_search method always returns a state of the table which represents a (seat, person_no) for total of seats.

Each node of the result of the A* search is sotred in a Person object. The score is computed for the complete table using
the g + h where g is the cost of each node and h is the heuristic function computed from the preference matrix, then the
score is printed then all the (seat, person_number) combinations of the table with n seats and n persons.

Time complexity in worst case in performance is O(|E|) = O(b^d), where E is the number of edges,
b is the branching factor (the avg number of successors per state) and d is the depth of the solution
(in this case is the most expensive path)
Time complexity in worst case in space is O(|V|) = O(b^d), where V is the number of vertexes, b - branching
factor, and d - depth of solution

I generate the adjacency lists in time compexity O(n).

The program has the highest time complexity in the main execution of the program which executes 'run_search' method in
four nested 'for' loops which gives an uppuer time complexity of O(n^4). These four loops executes the run_search for all the
possible combination of start and target nodes.

A* search algorithm returns the highest score from start to taget and if this path does not include all the nodes, the program
includes them randomly.

Space complexity is very high running this program, I clean the memory after each iteration.

Results:
The first result set for n=10 is the largest from the three sets, because the graph with n=10 is smaller than the other
two and the preference matrix is smaller with less variable cels' magnitudes compared with the other 2 sets.

The second result set for n=30 is the second largest from the three sets, then the third result set.

Comparing the second result set with the third result set, I can see the preference matrix computation takes more work
for the third dataset. There are more negative values in the third dataset's preference matrix and they produce more
magnitude defifference in minimums and maximums for heuristic values compared to the second datase.

Output score values for the three datasets are as following:

n = 10, instance 1, optimal score is 104
n = 30, instance 2, optimal score ~500s (231 during 2 hour execution)
n = 30, instance 3, optimal score -6 (60 seconds execution time)

The results are taken from the program running execution of 60 seconds.

