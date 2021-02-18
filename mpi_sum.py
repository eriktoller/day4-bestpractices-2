# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 13:36:58 2021

@author: erito849
"""
import numpy
import sys	
from mpi4py import MPI	

comm=MPI.COMM_WORLD	
rank=comm.Get_rank()	
size=comm.Get_size()	

n=int(sys.argv[1])	

x=numpy.random.random(int(n/size))		

#initializing	variables.	mpi4py	requires	that	we	pass	numpy	objects.	
integral=numpy.zeros(1)	
total=numpy.zeros(1)	

#	perform	local	computation.	Each	process	integrates	its	own	interval	
integral[0]=numpy.sum(x)

comm.Reduce(integral, total, op=MPI.SUM, root=0)

if comm.rank ==	0:
    print("The sum of %i ramdon numbers is %f" % (n, total))