import numpy as np

def brute_force_optimized(f,a,b,n):
	x = np.linspace(a,b,n)
	y = f(x)
	# Let maxima and minima hold the indices corresponding
	# to (local) maxima and minima points
	minima = []
	maxima = []

	for i in range(1,n-1):
		if y[i-1] < y[i] > y[i+1]:
			maxima.append(i)
		if y[i-1] > y[i] < y[i+1]:
			minima.append(i)

	# End points
	y_max_inner = max([y[i] for i in maxima])
	y_min_inner = min([y[i] for i in minima])
	if y[0] > y_max_inner:
		maxima.append(0)
	if y[len(x)-1] > y_max_inner:
		maxima.append(len(x)-1)
	if y[0] < y_min_inner:
		minima.append(0)
	if y[len(x)-1] < y_min_inner:
		minima.append(len(x)-1)

	# Return x and y values
	return [(x[i], y[i]) for i in minima], \
		   [(x[i], y[i]) for i in maxima]

if __name__ == "__main__":
	# numpy style of minima and maxima
	minima_np, maxima_np = brute_force_optimized(
		lambda x: np.exp(-x**2)*np.cos(4*x), 0,4,1001)

	# pythonic style
	minima_py = [(float(x_val), float(y_val)) for x_val, y_val in minima_np]
	maxima_py = [(float(x_val), float(y_val)) for x_val, y_val in maxima_np]

	print('Minima:\n',minima_py)
	print('Maxima:\n',maxima_py)
