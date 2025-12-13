from numpy import linspace, sum

def midpoint(f,a,b,n):
	h = (b-a)/n
	x = linspace(a + h/2, b - h/2, n)
	return h*sum(f(x))
