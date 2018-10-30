# Jack Weissenberger
# 222 Lab 2, Kruskal's minimum spanning tree algorithm

from queue import PriorityQueue


def print_htable(h):

    for key, value in h.items():
        print('%s: %s' % (key, value))

    return


def find(a, parent_dictionary):
    # we need to input the parent dictionary as well so that it can be updated

    if a != parent_dictionary[a]:
        parent_dictionary[a], parent_dictionary = find(parent_dictionary[a], parent_dictionary)

    return parent_dictionary[a], parent_dictionary

if __name__ == '__main__':
    edge_priority_q = PriorityQueue()

    edge_priority_q.put((2, 'AB'))
    edge_priority_q.put((12, 'AC'))
    edge_priority_q.put((2, 'BC'))
    edge_priority_q.put((10, 'BD'))
    edge_priority_q.put((2, 'CD'))
    edge_priority_q.put((13, 'AJ'))

    num_edges = 6

    # need to figure out how to get this from the input file
    # vertex and its parent
    # vertex # this needs to be global so that the find function can update and compress all of the parents
    vertex = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'J': 'J'}

    # list of the edges were gonna add to the path
    x = []

    for i in range(num_edges):
        edge = edge_priority_q.get()

        print('Vertex 0:', edge[1][0], 'Vertex 1:', edge[1][1], 'size:', edge[0])
        print("Parent 0:", vertex[edge[1][0]], 'Parent 1:', vertex[edge[1][1]])
        print("")

        # get the parent of the first vertex and update the vertex dictionary
        parent0, vertex = find(edge[1][0], vertex)
        # do the same for the second
        parent1, vertex = find(edge[1][1], vertex)

        # if they are in different sets, combine the sets and add this edge to X
        if parent0 != parent1:
            x.append(edge)

            # make the parent of edge[1][1], edge[1][0]
            vertex[edge[1][1]] = edge[1][0]

    # length of the final path
    path = 0

    print("Edges in final path:")
    for i in x:
        print(i[1])
        path += i[0]

    print('Final path length:', path)


