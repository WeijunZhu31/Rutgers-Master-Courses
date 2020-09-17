'''
Homework 03 - Quesiont 02
Name : Weijun Zhu
'''


# Question b
def euclid_algo(l, phi, n):
    for k in range(1, phi):
        if (k * l) % n == 1:
            print('The value of k is : ', k)
            print('public key: ', l, n)
            print('private key: ', k, n)
            return k
        else:
            continue


# Question c
def encrypted(string, l, n):
    dictionary = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7,
                  'g': 8, 'h': 9, 'i': 10, 'j': 11, 'k': 12, 'l': 13,
                  'm': 14, 'n': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19,
                  's': 20, 't': 21, 'u': 22, 'v': 23, 'w': 24, 'x': 25,
                  'y': 26, 'z': 27, ' ': 28}
    message = []
    for i in string:
        temp = (dictionary[i] ** l) % n
        message.append(temp)
    print('encrypted message: ', message)
    return message


# # Question d
# def sentMessage(p, q, text, l, n):
#     for i in range(1, 100):
#         x = 1 + i * phi
#         if x % l == 0:
#             k = int(x / l)
#             break
#             print(k)
#     # cipher text
#     ct = (text ** l) % n
#
#     # decrypted text
#     dt = (ct ** k) % n
#     print('n = ' + str(n) + ' l = ' + str(l) + ' phi = ' + str(phi) + ' k = '
#           + str(k) + ' cipher text = ' + str(ct) + ' decrypted text = ' + str(dt))
#     return ct, dt

def sign(m):
    temp_E = []
    for i in range(len(m)):
        temp_E.append(m[i] ** 41 % 9271)
    print(temp_E)
    return temp_E


def sign1(temp_E):
    for i in range(len(temp_E)):
        print(temp_E[i] ** 73 % 10961)


if __name__ == '__main__':
    # Question b:
    print('Question b')
    print('Alice : ')
    pA = 97
    qA = 113
    nA = pA * qA
    lA = 73
    phiA = (pA - 1) * (qA - 1)
    euclid_algo(lA, phiA, nA)

    print('Bob : ')
    pB = 127
    qB = 73
    nB = pB * qB
    lB = 41
    phiB = (pB - 1) * (qB - 1)
    euclid_algo(lB, phiB, nB)
    print('#' * 100)

    # Question c:
    print('Question c')
    p1 = 97
    q1 = 113
    n1 = p1 * q1
    l1 = 73
    phi2 = (p1 - 1) * (q1 - 1)
    string = input('enter your message: ')  # enter the message: "buy google"
    encrypted(string, l1, n1)
    print('#' * 100)

    # Question d:
    print('Question d')
    # # kB = 5753    lB = 41
    # p3 = 127
    # q3 = 73
    # l3 = 41
    # n3 = p3 * q3
    # phi = (p3 - 1) * (q3 - 1)
    # text = int(input('Enter Bob\'s signs: '))  # enter the sign: "buy google"
    # sentMessage(p3, q3, text, l3, n3)

    sign(m=[3, 22, 26, 28, 8, 16, 16, 8, 13, 6])
    sign1(temp_E=[9222, 6957, 8645, 8726, 1159, 6866, 6866, 1159, 5606, 6389, 3, 16, 3])
