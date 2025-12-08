def trapezoidal(f,a,b,n):
	h = (b-a)/n
	f_sum = 0
	for i in range(1,n):
		x = a + i*h
		f_sum = f_sum + f(x)
	return h*(0.5*f(a) + f_sum + 0.5*f(b))
