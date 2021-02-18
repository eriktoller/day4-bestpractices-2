# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:25:19 2021

@author: erito849
"""

from mpi4py import MPI	
comm = MPI.COMM_WORLD	
rank = comm.Get_rank()	
print ("Greating user, I am process of rank: ", rank)

	