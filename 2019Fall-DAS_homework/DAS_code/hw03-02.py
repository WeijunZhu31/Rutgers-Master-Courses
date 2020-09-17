# Question b:
print('Question b : ')


def computeAlice(la, phi):
    for i in range(1, phi):
        if (i * la % phi) == 1:
            print(i)


def computeBob(lb, phi):
    for i in range(1, phi):
        if (i * lb % phi) == 1:
            print(i)


computeAlice(73, 10752)
computeBob(41, 9072)

print('#' * 100)

# Question c:
print('Question c : ')
message = [3, 22, 26, 28, 8, 16, 16, 8, 13, 6]


def encrypted(message):
    message_exchange = []
    for i in range(0, len(message)):
        message_exchange.append(message[i] ** 73 % 10961)
    print(message_exchange)
    return message_exchange


encrypted(message)
print('#' * 100)

# Question d:
print('Question d : ')
message1 = [3, 22, 26, 28, 8, 16, 16, 8, 13, 6]


def sign(message1):
    message_exchange1 = []
    for i in range(len(message1)):
        message_exchange1.append(message1[i] ** 41 % 9271)
    print(message_exchange1)


sign(message1)

'''
So the encrypted message is: [9222, 6957, 8645, 8726, 1159, 6866, 6866, 1159, 5606, 6389]

Then Bob sign his name end the of the message, so 
[9222, 6957, 8645, 8726, 1159, 6866, 6866, 1159, 5606, 6389, 3, 16, 3]

Bob encrypt the message with signature using Alice's public key.
'''

message2 = [9222, 6957, 8645, 8726, 1159, 6866, 6866, 1159, 5606, 6389, 3, 16, 3]


def encrypted(message2):
    message_exchange2 = []
    for i in range(0, len(message2)):
        message_exchange2.append(message2[i] ** 73 % 10961)
    print(message_exchange2)
    return message_exchange2


encrypted(message2)

'''
The message becomes: 
[8205, 3713, 6681, 578, 4184, 2014, 2014, 4184, 634, 9404, 870, 8164, 870], 
then Alice receives the message from Bob, and the she needs to decrypt this message by 
using her private key.

At last, the message which Alice receives from Bob is: 
[9222, 6957, 8645, 8726, 1159, 6866, 6866, 1159, 5606, 6389, 3, 16, 3], and '3, 16, 3'
represents signature of Bob, and the message is 'buy google'.
'''

