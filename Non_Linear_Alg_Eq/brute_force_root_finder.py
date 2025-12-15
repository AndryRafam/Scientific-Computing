import numpy as np

def brute_force_root_finder(f,a,b,n):
	x = np.linspace(a,b,n)
	y = f(x)
	roots = []
	for i in range(n-1):
		if y[i]*y[i+1] < 0:
			root = x[i] - (x[i+1] - x[i])/(y[i+1] - y[i])*y[i]
			roots.append(root)
		elif y[i] == 0:
			root = x[i]
			roots.append(root)
	return roots

if __name__ == "__main__":
	roots_numpy = brute_force_root_finder(lambda x: np.exp(-x**2)*np.cos(4*x), 0,4,1001) # Solution here is in form of np.float()

	if roots_numpy:
		roots_python_form = [float(r) for r in roots_numpy]
		print(roots_python_form) # Print solution in pythonic style
	else:
		print('Could not find any roots')
