
import pprint


def main():
    in_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
    res = chunks(in_list, 3)
    pprint.pprint(res)


def chunks(li, n):
    """ Divides a list to a list of lists of size n
Input:
li = [1, 2, 3, 4, 5]
n = 2

Output:
[[1, 2], [3, 4], [5]]
"""
    return [li[i:i+n] for i in xrange(0, len(li), n)]


if __name__ == '__main__':
    main()
