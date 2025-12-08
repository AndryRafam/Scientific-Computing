from math import exp
from math import pow
from trapezoidal import trapezoidal

def application():
	v = lambda t: 3*(pow(t,2))*exp(pow(t,3))
	n = int(input('n: '))
	numerical = trapezoidal(v,0,1,n)

	# Compare with exact result
	V = lambda t: exp(pow(t,3)) # dV/dt = v
	exact = V(1) - V(0)
	error = exact - numerical
	print('n={:d}: {:.16f}, error: {:g}'.format(n,numerical,error))

if __name__ == '__main__':
	application()
