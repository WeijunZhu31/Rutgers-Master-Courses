# From wikibooks.org
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


"""
Created on Thu Nov 28 11:34:37 2019

@author: alizadeh
"""

# compute inverse of a mod n, that is solve ax=1 mod n
def inv(a,n):
    g,y,x=xgcd(n,a)
    if g==1:
        return x
    else:    #gcd is not 1, thre is no inverse, return NaN
        import numpy as np
        return(np.NaN)
        
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:32:37 2019

@author: alizadeh
"""
# -*- coding: utf-8 -*-
# Turn characters from a to z and blank into integers from 2 to 28
def f(x):
    if (x>='a') & (x<='z'):
        return (ord(x)-ord('a')+2)
    elif (x>='A') & (x<='Z'):
        return(ord(x)-ord('A')+2)
    elif x==' ':
        return (28)
    else:
        return(-1)
        
        
def charToInt (S):
  return([f(x) for x in S])
    


"""
Created on Thu Oct 31 10:43:53 2019

@author: alizadeh
"""

# Find integer power x^n mod m by repeated squaring algorithm
def power(x, n, m):
  c=0
  d=1
  nn=list(bin(n)) #turns n to an array of 0 and 1 binary representation
  nn=nn[2:len(nn)]
  #b=dec2bin(n)
  import numpy as np
  k=int(np.ceil(np.log2(n)))
  #tobin=lambda x: (x=='1')-(x=='0')#returns 1 if ==1, and -1 if ==0
  for i in range(k,-1,-1): 
    c=2*c
    d=d*d % m
    #if (nn[i]=='1'):
    if((n & 2**i) > 0): # n & 2**i takes bitwise 'and' it checks ith bit of n
      c=c+1
      d=(d*x) % m
  return(d)

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:49:37 2019

@author: alizadeh
"""

# This function takes a key l and integer n and an array M of integers,
# and encrypt/decrypt them using power to l mod n

def crypt(M, l, n):
    return(list(map(lambda x:power(x,l,n),M)))


# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:27:22 2019

@author: alizadeh
"""

# intToChar turns an array character of numbers between 2 and 28 to letter
# to ASCII. Note a is mapped to 2, b to 3, etc. 
def intToChar (M):
    #import numpy as np
    S=list(len(M)*' ')
    import string
    letters=list(string.ascii_lowercase+' ')
    for i in range(0,len(M)):
      if ((M[i]>=2) & (M[i]<27)):
        S[i]=letters[M[i]-2]
      elif (M[i]==28):
          S[i]=" "
      else:
        print("Illegal array")
        S[i]=-1
    return(S)

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:49:37 2019

@author: alizadeh
"""

# Quick function for decryption of an array of integers E using key k and n
def RSAtoTxt(E, k, n):
    return(intToChar(crypt(E,k,n)))

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:43:10 2019

@author: alizadeh
"""

# Quick function to encrypt with key k and n. M is a string.
def sendRSA(M,k,n):
  MM=list(M)
  E=charToInt(MM)
  E=crypt(E,k,n)
  return(E)

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:43:10 2019

@author: alizadeh
"""

# Driver Code 
if __name__ == '__main__': 
   pa,qa,pb,qb=97,113,127,73 #initialize 
   la,lb=73,41

   na,nb = pa*qa, pb*qb
   phia,phib=(pa-1)*(qa-1),(pb-1)*(qb-1)
   print("Q2a: na = ",na, " nb = ",nb, " phia= ",phia, " phib= ",phib)

   #junk1,ka,junk2=xgcd(phia,la)
   #junk1,kb,junk2=xgcd(phib,lb)
   #junk1,junk2,ka=xgcd(phia,la)
   #junk1,junk2,kb=xgcd(phib,lb)
   ka=inv(la,phia)
   kb=inv(lb,phib)
   if ka < 0:
       ka=phia+ka
   if kb < 0:
       kb=phib+kb
   print("Q2b: ka = ",ka, "kb= ",kb)
   M="buy google"
   print("Mesage from Bob to Alice: \"", M,"\"")
   SA=sendRSA(M,la,na)
   print("Q2c: Encryption of \"buy google\" using Alice's public key la: ",SA)
   signB=sendRSA("bob",kb,nb)
   print("Q2d: Bob's signature \"Bob\" encrypted using Bob's private key kb: ",signB)
   # Note: s.join(a) takes an array of strings and concatenates then with s as separator:
   print("Q2d: Alices's decryption of Bob's signature using Bob's public key lb: ","".join(intToChar(crypt(signB,lb,nb))))
   print("Q2d: Alices's decryption of Bob's message usin her own private key ka: ","".join(intToChar(crypt(SA,ka,na))))

   
   
