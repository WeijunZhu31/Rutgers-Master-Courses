from math import floor


def binarysearch(L, x):
    print(L)
    mid = floor(len(L) / 2)
    print('mid={0},number={1}'.format(mid, L[mid]))
    if L[mid] == x:
        return mid
    elif len(L) == 1:
        if L[0] > x:
            return 'x not in the L'
        if L[0] < x:
            return 'x not in the L'

    elif L[mid] < x:
        try:
            return mid + binarysearch(L[mid:], x)
        except BaseException:
            print('x not in the L')
    elif L[mid] > x:
        return binarysearch(L[:mid], x)


print(binarysearch([3, 5, 7, 9, 11, 13, 15, 17], 19))
