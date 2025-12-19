# In this simulation, we use the function sin(x)

import numpy as np
import matplotlib.pyplot as plt

# step size
h = 0.1
# define grid
x = np.arange(0,2*np.pi,h)
# compute function
y = np.sin(x)

# computer vector of forward differences
forward_diff = np.diff(y)/h
# computer corresponding grid
x_diff = x[:-1:]
# computer exact solution
exact_solution = np.cos(x_diff)

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
print(max_error)
