# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:42:11 2020

@author: alizadeh
"""

def filter(S, M):
    import numpy as np
    import scipy as sp
    
    SShape=S.shape
    MShape=M.shape
    assert SShape[0]>MShape[0]
    assert SShape[1]>MShape[1]
    
    out=np.zeros(S.shape)
    S=np.append(np.zeros((1,SShape[1])),S, axis=0)
    S=np.append(S,np.zeros((1,SShape[1])), axis=0)
    S=np.append(np.zeros((SShape[0]+2,1)),S,axis=1)
    S=np.append(S,np.zeros((SShape[0]+2,1)),axis=1)

    
    for i in range(out.shape[0]-M.shape[0]):
        for j in range(out.shape[1]-M.shape[1]):
            out[i,j]=sum(sum(np.asarray(S[i:M.shape[0]+i,j:M.shape[1]+j])*np.asarray(M)))
    
    return out
            
    