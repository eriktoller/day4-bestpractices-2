"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    simple_add(a,b)
    
    This fucntion resturns the sum of 'a' and 'b'.
    
    Parameters	
	----------	
	a: float, an arbirary input value
    b: float, an arbirary input value		
			
	Returns	
	-------	
    a+b: float, the sum of 'a' and 'b'
	
    Examples
	--------	
	>>>	simple_add(1,2)	
	3
    >>>	simple_add(10,5)	
	15
    """
    return a+b

def simple_sub(a,b):
    """
    simple_sub(a,b)
    
    This fucntion resturns the difference between 'a' and 'b'.
    
    Parameters	
	----------	
	a: float, a constant
    b: float, a constant		
			
	Returns	
	-------	
    a-b: float, the difference of 'a' and 'b'
	
    Examples
	--------	
	>>>	simple_sub(1,2)	
	-1
    >>>	simple_sub(10,5)	
	5
    """
    return a-b

def simple_mult(a,b):
    """
    simple_mult(a,b)
    
    This fucntion resturns multiplication of 'a' and 'b'.
    
    Parameters	
	----------	
	a: float, a constant
    b: float, a constant		
			
	Returns	
	-------	
    a*b: float, the mutiplication of 'a' and 'b'
	
    Examples
	--------	
	>>>	simple_mult(1,2)	
	2
    >>>	simple_mult(10,5)	
	50
    """
    return a*b

def simple_div(a,b):
    """
    simple_div(a,b)
    
    This fucntion resturns the division of 'a' and 'b'.
    
    Parameters	
	----------	
	a: float, a constant
    b: float, a constant		
			
	Returns	
	-------	
    a/b: float, the division of 'a' and 'b'
	
    Examples
	--------	
	>>>	simple_div(1,2)	
	.5
    >>>	simple_div(10,5)	
	2
    """
    return a/b

def poly_first(x, a0, a1):
    """
    poly_first(x, a0, a1)
    
    This fucntion resturns the first order polynomial y = a0 + a1*x.
    
    Parameters	
	----------	
	a0: float, a constant
    a1: float, the multiplicand
    x: float, the multiplier
			
	Returns	
	-------	
    a0 + a1*x: float, result of the first order polynomial
	
    Examples
	--------	
	>>>	poly_first(1,2,3)	
	5
    >>>	poly_first(2,5,3)	
	11
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    poly_second(x, a0, a1, a2)
    
    This fucntion resturns the second order polynomial y = a0 + a1*x + a2**x.
    The function calls the poly_first(x, a0, a1) funciton.
    
    Parameters	
	----------	
	a0: float, a constant
    a1: float, the multiplicand
    a2: float, the base
    x: float, the multiplier and exponent
			
	Returns	
	-------	
    a0 + a1*x + a2**x: float, result of the second order polynomial
	
    Examples
	--------	
	>>>	poly_second(1,2,3,4)	
	9
    >>>	poly_first(2,5,3,6)	
	35
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
