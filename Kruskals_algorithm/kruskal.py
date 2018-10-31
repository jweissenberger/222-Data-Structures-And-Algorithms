# Jack Weissenberger
# 222 Lab 2, Kruskal's minimum spanning tree algorithm

from queue import PriorityQueue


def find(a, parent_dictionary):
    """
    This method finds the parent of a node while simultaneously compressing the tree so that all leafs of a tree point 
    to the root of the tree
    
    :param a: the vertex that you want to find the parent of
    :param parent_dictionary: the dictionary of nodes and their parents
    :return: the parent of a, the same parent dictionary but compressed to that all leafs of a tree point to the parent
    """
    if a != parent_dictionary[a]:
        parent_dictionary[a], parent_dictionary = find(parent_dictionary[a], parent_dictionary)

    return parent_dictionary[a], parent_dictionary

if __name__ == '__main__':
    edge_priority_q = PriorityQueue()

    # read in the file and store the input into a variable names lines
    # change the name of the text file here to read in a different graph
    f = open('input3.txt')
    lines = f.readlines()
    f.close()

    vertex = {}  # this dictionary will contain every node as the key and it's parent as the value
    num_edges = 0  # this is the number of usable edges in the graph (does not include loops)

    for ln in lines:
        split_ln = ln.split(',')
        num = int(split_ln[0])
        verts = str(split_ln[1])
        verts.strip()  # remove preceding and trailing whitespace
        verts = verts[0] + verts[1]  # make sure to only grab letters and not new lines

        # this handles the case for loops because if an edge loops back to the same node, the vertices will be the same
        if verts[0] != verts[1]:
            edge_priority_q.put((num, verts))  # put the tuple of the number and edge into the priority q
            vertex[verts[0]] = verts[0]  # fill the dictionary with each of the vertices and have the parent be itself
            vertex[verts[1]] = verts[1]
            num_edges += 1

    # list of the edges were gonna add to the path
    x = []

    # iterates over each of the edges
    for i in range(num_edges):
        edge = edge_priority_q.get()

        # get the parent of the first vertex and update the vertex dictionary
        parent0, vertex = find(edge[1][0], vertex)
        # do the same for the second
        parent1, vertex = find(edge[1][1], vertex)

        # if they are in different sets, combine the sets and add this edge to X
        if parent0 != parent1:
            x.append(edge)

            # this is the equivalent of the Union method from the text book
            # I do not have to worry about rank because I my find method compresses the tree
            # make the parent of edge[1][1], edge[1][0]
            vertex[edge[1][1]] = edge[1][0]

    path = 0  # length of the final path
    print("\nEdges in final path:")
    for i in x:
        print(i[1])
        path += i[0]

    print('\nFinal path length:', path)



