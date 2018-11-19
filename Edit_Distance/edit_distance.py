"""
Jack Weissenberger, CS 222
Edit Distance
"""

import numpy as np


# diff from text book, 1 if the letters are different, 0 if they are the same
def diff(word_a, word_b, x, y):
    if word_a[x] == word_b[y]:
        return 0
    else:
        return 1


# returns the minimum of the 3 inputted integers
def minim(x, y, z):
    if x < y and x < z:
        return x
    elif y < z and y < x:
        return y
    else:
        return z


if __name__ == '__main__':

    # get each of the words from input
    word1 = str(input("Input word 1:\n"))
    word2 = str(input("Input word 2:\n"))

    word1_len = len(word1)
    word2_len = len(word2)

    # initialize table
    table = np.zeros((word1_len+1, word2_len+1))

    # the next 3 for loops are the fundamental edit distance algorithm
    for i in range(word1_len+1):
        table[i, 0] = i

    for j in range(word2_len+1):
        table[0, j] = j

    for i in range(1, word1_len+1):
        for j in range(1, word2_len+1):
            a = table[i-1, j] + 1
            b = table[i, j-1] + 1
            c = table[i-1, j-1] + diff(word1, word2, i-1, j-1)
            table[i, j] = minim(a, b, c)

    m = word1_len
    n = word2_len
    path = []

    # search through the table getting the path
    while not (m == 0 and n == 0):
        top = table[m-1, n]
        left = table[m, n-1]
        diag = table[m-1, n-1]
        if n == 0:
            path.append("top")
            m -= 1
        elif m == 0:
            path.append("left")
            n -= 1
        elif diag <= left and diag <= top:
            path.append("diag")
            m -= 1
            n -= 1
        elif left <= top:
            path.append("left")
            n -= 1
        else:
            path.append("top")
            m -= 1

    word1_index = 0
    word2_index = 0
    output_word1 = ''
    output_word2 = ''

    # print out each of the words with the correct spacing
    for i in list(reversed(path)):
        if i == 'diag':
            output_word1 += word1[word1_index]
            output_word2 += word2[word2_index]
            word1_index += 1
            word2_index += 1
        if i == 'top':
            output_word1 += word1[word1_index]
            output_word2 += '-'
            word1_index += 1
        if i == 'left':
            output_word2 += word2[word2_index]
            output_word1 += '-'
            word2_index += 1

    print(output_word1)
    print(output_word2)
    print("Edit distance:", int(table[-1, -1]))
