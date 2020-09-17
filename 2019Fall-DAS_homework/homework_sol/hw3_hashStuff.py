# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:57:57 2019

@author: alizadeh
"""

def hashf1(k,A,m):
    import numpy as np
    return(int(m*(k*A % 1)))

def hashf2(k,m):
    return(k % m)
    
def hashit(keys,A,m,hf=hashf1):
    import numpy as np
    h=list(map(lambda x: hf(x,A,m),  keys))
    T=[[] for _ in range(m)] #initialize T ro a an array of empty lists
    t=list(map(int, np.zeros(m))) #Array t keeps track of lenght of chains,
    #initialize t to array of int zeros
    for i in range(len(keys)):
        T[hf(keys[i],A,m)].append(keys[i]) #Assign keys chains in T
        t[h[i]]=t[h[i]]+1
    return(T,t,h)    
 
#driver code:
if __name__ == '__main__': 
    import numpy as np
    np.random.seed(15)
    N=10000
    n=500
    m=127
    keys=np.random.randint(0,N,n) #generate random keys
    print("These are the keys: ",keys)
    A1=(np.sqrt(5)-1)/2
    T1,c1,h1=hashit(keys,A1, m) # First hash table: T1 is the table, c1 lengths of chains
    A2=np.pi/6
    T2,c2,h2=hashit(keys,A2, m) # Second hash table
    m=63
    T3,c3,h3=hashit(keys,0, m,lambda k,A,m: (k%m)) # Third hash  table
    

    print("T1 hashed keys with A= (sqrt(5)-1)/2:\n")
    display([lambda x: print(x,sep='\n'), T1])
    print("T2 hashed with A= pi/6:\n")
    display([lambda x:print(x,sep='\n'), T2])
    print( "T3 hashed with division method % 63:\n")
    display([print(lambda x: x,sep='\n'), T3])
    
    print("var c1: ", np.var(c1), "  max c1: ", max(c1), "empty cells: ", sum(list(map(lambda x:x==0, c1))))
    print("var c2: ", np.var(c2), "  max c2: ", max(c2), "empty cells: ", sum(list(map(lambda x:x==0, c2))))
    print("var c3: ", np.var(c3), "  max c3: ", max(c3), "empty cells: ", sum(list(map(lambda x:x==0, c3))))
        
    import matplotlib.pyplot as plt
    plt.hist(c1)
    plt.show()
    plt.hist(c2)
    plt.show()
    plt.hist(c3)
    plt.show()
    print("putting all three in a graph:")
    plt.plot(np.sort(c1),'cornflowerblue')
    plt.plot(np.sort(c2),'orange')
    plt.plot(np.sort(c3),'red')
    plt.show()
