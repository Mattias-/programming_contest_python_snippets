
import sys
import pprint


def main():
    res = string_matrix_columns()
    print res
    #pprint.pprint(res)


def int_matrix(rows=5):
    """ Integer matrix with no spaces
Input:
00000
00000
00000
00000

Output:
[[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]]
"""
    matrix = []
    for _ in xrange(rows):
        r = [int(x) for x in list(sys.stdin.readline().rstrip())]
        matrix.append(r)
    return matrix


def int_matrix_spaced(rows=5):
    """ Integer matrix with spaces
Input:
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

Output:
[[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]]
"""
    matrix = []
    for _ in xrange(rows):
        r = [int(x) for x in sys.stdin.readline().split()]
        matrix.append(r)
    return matrix


def int_list():
    """ read line to int list
Input:
1 2 3 4 5

Output:
[1,2,3,4,5]
"""
    return [int(x) for x in sys.stdin.readline().split()]


def int_column(rows=5):
    """ read strings from many lines
Input:
1
3
4
-5000
5

Output:
[1, 3, 4, -5000, 5]
"""
    col = []
    for _ in xrange(rows):
        r = int(sys.stdin.readline().rstrip())
        col.append(r)
    return col


def int_values():
    """ read integer tuples
Input:
5 5

Output:
(5, 5)
"""
    (rows, cols) = [int(x) for x in sys.stdin.readline().split()]
    return (rows, cols)


def int_single():
    """ read a single int
Input:
-345

Output:
-345
"""
    i = int(sys.stdin.readline.rstrip())
    return i


def float_values():
    (first, second) = [float(x) for x in sys.stdin.readline().split()]
    return (first, second)


def string_matrix(rows=5):
    """
Input:
..........
..O....O..
.\....../.
..\____/..
..........

Output:
[['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', 'O', '.', '.', '.', '.', 'O', '.', '.'],
['.', '\\', '.', '.', '.', '.', '.', '.', '/', '.'],
['.', '.', '\\', '_', '_', '_', '_', '/', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
"""
    matrix = []
    for _ in xrange(rows):
        r = list(sys.stdin.readline().rstrip())
        matrix.append(r)
    return matrix


def string_matrix_spaced(rows=5):
    """
Input:
A A A X
A A B X
A B A X
A B B X
B A A Y

Output:
[['A', 'A', 'A', 'X'],
 ['A', 'A', 'B', 'X'],
 ['A', 'B', 'A', 'X'],
 ['A', 'B', 'B', 'X'],
 ['B', 'A', 'A', 'Y']]
"""
    matrix = []
    for _ in xrange(rows):
        r = sys.stdin.readline().split()
        matrix.append(r)
    return matrix


def string_matrix_columns(rows=5):
    """ Columns of a non-spaced string matrix, ASCII art.
Input:
***
  *
***
  *
***

Output:
[['*', ' ', '*', ' ', '*'],
 ['*', ' ', '*', ' ', '*'],
 ['*', '*', '*', '*', '*']]
"""
    matrix = []
    for _ in xrange(rows):
        r = list(sys.stdin.readline().rstrip())
        matrix.append(r)
    rotated = []
    # Assuming all rows have same length
    for col in xrange(len(matrix[1])):
        c_list = [matrix[row][col] for row in xrange(rows)]
        rotated.append(c_list)
    return rotated


def string_list():
    """ read strings from one line
Input:
Hello world how are you

Output:
['Hello', 'world', 'how', 'are', 'you']
"""
    return sys.stdin.readline().split()


def string_column(rows=5):
    """ read strings from many lines
Input:
Hello
world
how
are
you

Output:
['Hello', 'world', 'how', 'are', 'you']
"""
    col = []
    for _ in xrange(rows):
        r = sys.stdin.readline().rstrip()
        col.append(r)
    return col


def string_single():
    return sys.stdin.readline().rstrip()

if __name__ == '__main__':
    main()
