from sys import maxsize  # get largest value
from itertools import permutations  # getting all the possible paths

V = 6  # taking 6 nodes as example

# TSP function
def TSP_travellingSalesman(graph, s):
    node = []  # storing node excluding start
    for i in range(V):
        if i != s:
            node.append(i)

    # store least weighted path in hamiltonian graph
    shortest_path = maxsize
    next_pathPermutation = permutations(node)
    for i in next_pathPermutation:
        current_pathCost = 0  # store cost of current path
        k = s  # calculate cost
        for j in i:
            current_pathCost += graph[k][j]
            k = j
        current_pathCost += graph[k][s]
        shortest_path = min(shortest_path, current_pathCost)  # refresh least cost

    return shortest_path

# adjacency matrix for the nodes
graph = [[0, 10, 15, 20, 25, 15], [10, 0, 35, 25, 10, 20], [20, 0, 15, 45, 10, 50],
        [15, 35, 0, 30, 55, 25], [20, 25, 30, 0, 45, 25], [10, 25, 35, 0, 45, 15]]
s = 0
matrix_output = str(TSP_travellingSalesman(graph, s))
print("The answer to this set of problem is:    " + matrix_output + "units.")