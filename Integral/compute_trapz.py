# The scipy.integrate sub-package contains trapezoid method
# Lets compare with our built hand trapezoid method

# Our built hand trapezoid method

import numpy as np
from scipy.integrate import trapezoid

def trap(f,a,b,n):
	h = (b-a)/(n-1)
	computed = (h/2)*(f[0]+\
		2*sum(f[1:n-1])+f[n-1])
	return computed

a = 0
b = np.pi
n = 100 # number of trapezoid
h = (b-a)/(n-1)
x = np.linspace(a,b,n)
f = np.sin(x)

I_trapz = trapezoid(f,x) # scipy.integrate trapezoid method
I_trap = trap(f,a,b,n)

print(I_trapz)
print(I_trap)
