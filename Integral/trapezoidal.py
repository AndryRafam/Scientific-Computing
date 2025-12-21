# Trapezoidal method to compute the value of integrals

import numpy as np

def trap(f,a,b,n):
	h = (b-a)/(n-1)
	computed = (h/2)*(f[0]+\
		2*sum(f[1:n-1])+f[n-1])
	return computed

if __name__ == "__main__":
	a = 0
	b = np.pi
	# number of step
	# the more it is great
	# the more the value of integral is close to the exact value
	n = 100 
	x = np.linspace(a,b,n)
	f = np.sin(x)
	I_trap = trap(f,a,b,n)
	# here the exact value of the integral of sin(x) between 0 and pi is known
	exact_value = 2 
	# difference between the exact value of the integral and its compute value
	err_trap = exact_value-I_trap
	# print both
	print(I_trap)
	print(err_trap)
