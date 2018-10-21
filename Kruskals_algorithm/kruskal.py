# Jack Weissenberger
# 222 Lab 2, Kruskal's minimum spanning tree algorithm

from queue import PriorityQueue


def print_htable(h):

    for key, value in h.items():
        print('%s: %s' % (key, value))

    return


def find(x, parent_dictionary):

    if x!= parent_dictionary[x]:
        parent_dictionary[x] = find(parent_dictionary[x])

    return parent_dictionary[x]

if __name__ == '__main__':
    edge_priority_q = PriorityQueue()

    edge_priority_q.put((2, 'AB'))
    edge_priority_q.put((12, 'AC'))
    edge_priority_q.put((2, 'BC'))
    edge_priority_q.put((10, 'BD'))
    edge_priority_q.put((2, 'CD'))

    num_edges = 5

    # need to figure out how to get this from the input file
    # vertex and its parent
    global vertex # this needs to be global so that the find function can update and compress all of the parents
    vertex = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D'}

    print_htable(vertex)

    for i in range(num_edges):
        edge = edge_priority_q.get()

        print("Parent 0", vertex[edge[1][0]], 'Parent 1', vertex[edge[1][1]])

        if vertex[edge[1][0]] != vertex[edge[1][1]]:
            print("True")
            # change the parent of the second element of the name to the first element
            #TODO This should be find
            vertex[edge[1][1]] = edge[1][0]

        #if vertex[edge[1][0]] != vertex[edge[1][0]]:

    print_htable(vertex)
