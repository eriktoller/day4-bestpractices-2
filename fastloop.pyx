# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:15:13 2021

@author: erito849
"""

#NOT COMPLETED DUE TO UNABLE TO RUN BUILD ON WINDOWS

def rbf_network_cython(int X, float beta, int theta):
    
    cdef float N[X.size()]
    cdef float N[X[0].size()]
    cdef int Y[N]

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y