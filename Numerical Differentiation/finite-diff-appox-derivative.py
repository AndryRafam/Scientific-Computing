# In this simulation, we use the function sin(x)

import numpy as np
import matplotlib.pyplot as plt

# step size
h = 0.1
# define grid
x = np.arange(0,2*np.pi,h)
# compute function
y = np.cos(x)

# computer vector of forward differences
forward_diff = np.diff(y)/h
# computer corresponding grid
x_diff = x[:-1:]
# computer exact solution
exact_solution = -np.sin(x_diff)

# Plot solution
plt.figure(figsize = (12,8))
plt.plot(x_diff, forward_diff, '--', \
	label = 'Finite difference approximation')
plt.plot(x_diff, exact_solution, \
	label = 'Exact solution')
plt.legend()
plt.show()

# Computer max error between
# numerical derivative and exact solution
max_error = max(abs(exact_solution - forward_diff))
print("max error = ", max_error)

# The following code computes the numerical derivative of f(x)=sin(x)
# using the forward difference formula for decreasing step sizes, h.
# It then plots the maximum error between the approximated derivative and the true derivative versus h
# as shown in the generated figure.

# define step size
h = 1
# define number of iterations to perform
iterations = 20
# list to store our step sizes
step_size = []
# list to store max error for each step size
max_error = []

for i in range(iterations):
	# halve the step size
	h /= 2
	# store this step size
	step_size.append(h)
	# compute new grid
	x = np.arange(0,2*np.pi,h)
	# computre function value at grid
	y = np.cos(x)
	# compute vector of forward differences
	forward_diff = np.diff(y)/h
	#compute corresponding grid
	x_diff = x[:-1]
	# compute exact solution
	exact_solution = -np.sin(x_diff)

	# Compute max error between
	# numerical derivative and exact solution
	max_error.append(\
		max(abs(exact_solution - forward_diff)))

# produce log-log plot of max error versus step size
plt.figure(figsize = (12,8))
plt.loglog(step_size, max_error, 'v')
plt.show()

