'''
Homework 03 - Question 05
Name: Weijun Zhu
'''
from math import floor, sqrt, pi
import random
# import matplotlib as mpl
# mpl.use('TkAgg')
from matplotlib import pylab as plt


# Question a
def hashf1(k, A, m):
    return floor(m * (k * A) % 1)


# Question b
def hashit(keys, A, m):
    h = []
    for key in keys:
        temp = hf(key, A, m)
        h.append(temp)
    T = dict(zip(keys, h))
    c = {}
    for value in T.values():
        if value not in c.values():
            c[value] = -1
    for value in T.values():
        if value in c.keys():
            c[value] += 1
    for i in c.keys():
        c[i] += 1
    print(' h: ', h, '\n', 'T: ', T, '\n', 'c: ', c)
    return h, T, c


def hf(k, A, m):
    return floor(m * ((k * A) % 1))


# Question c
def createRandomSample():
    keys = []
    for i in range(100):
        temp = random.randint(0, 9999)
        keys.append(temp)
    # print(keys)
    return keys


# Question f
def hashit1(keys, m):
    h2 = []
    for i in keys:
        temp1 = h(i, m)
        h2.append(temp1)
    T2 = dict(zip(keys, h2))
    c2 = {}
    for value in T2.values():
        if value not in c2.values():
            c2[value] = -1
    for value in T2.values():
        if value in c2.keys():
            c2[value] += 1
    for i in c2.keys():
        c2[i] += 1
    print(' h: ', h2, '\n', 'T: ', T2, '\n', 'c: ', c2)
    return h2, T2, c2


def h(k, m=63):
    return k % m


if __name__ == '__main__':
    # # Quesion a
    # k = int(input('k = '))
    # A = int(input('A = '))
    # m = int(input('m = '))
    # hashf1(k, A, m)
    # print('#' * 100)

    # Question c
    createRandomSample()

    # Question d
    print('Question d : ')
    keys = createRandomSample()
    hashit(keys, A=(sqrt(5) - 1) / 2, m=10)
    print('#' * 100)

    # Question e
    print('Question e : ')
    hashit(keys, A=pi / 6, m=10)
    print('#' * 100)

    # Question f
    print('Question f : ')
    hashit1(keys, m=63)
    print('#' * 100)

    # Question g
    print('Question g : ')
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)

    ax1.hist(hashit(keys, A=(sqrt(5) - 1) / 2, m=10)[0])  # 5d
    ax1.set_title('5d')
    ax2.hist(hashit(keys, A=pi / 6, m=10)[0])  # 5e
    ax2.set_title('5e')
    ax3.hist(hashit1(keys, m=63)[0])  # 5f
    ax3.set_title('5f')

    fig.show()
