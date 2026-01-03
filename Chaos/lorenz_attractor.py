# Lorenz attractor

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

"""
Lorenz system differential equations.
t (float): required by solve_ivp
coords: contains the current [x,y,z] coordinates (can be list or array)
sigma (float): The Prandtl number.
rho (float): The Rayleigh number.
beta (float): The geometric factor.
"""

def diff_lorenz(t,coords,sigma,rho,beta):
	x,y,z = coords
	dxdt = sigma*(y-x)
	dydt = x*(rho-z)-y
	dzdt = x*y-beta*z
	return [dxdt,dydt,dzdt]

# define the parameters
sigma = 10.0
rho = 28.0
beta = 8/3.0

# initial conditions
"""
a small change in the initial conditions will
lead to different result.
"""
initial_conditions = [0.0,1.2,1.05]

# time span
t_span = (0,80)

# time points where to evaluate the solution
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# solving the equation using Explicit Runge-Kutta of order 5(4)
print(f"Solving Lorenz system with initial conditions: {initial_conditions} and parameters: sigma={sigma}, rho={rho}, beta={beta}")
solution = integrate.solve_ivp(
	fun=diff_lorenz,
	t_span=t_span,
	y0=initial_conditions,
	method="RK45",
	args=(sigma,rho,beta),
	t_eval=t_eval)

if solution.success:
	x_coords, y_coords, z_coords = solution.y

	print(solution)

	fig = plt.figure(figsize=(10,8))
	ax = plt.axes(projection="3d") # add 3D subplot to the figure

	ax.set_xlim(np.min(x_coords), np.max(x_coords))
	ax.set_ylim(np.min(y_coords), np.max(y_coords))
	ax.set_zlim(np.min(z_coords), np.max(z_coords))
	ax.set_title("Lorenz Attractor Animation")

	# plot the trajectory
	ax.plot3D(x_coords, y_coords, z_coords, lw=1, color="black",alpha=1)
	ax.set_xlabel("X")
	ax.set_ylabel("Y")
	ax.set_zlabel("Z")
	ax.set_title("The Lorenz Attractor")
	ax.grid(True)
	plt.savefig("Lorenz Attractor.pdf"); plt.savefig("Lorenz Attractor.png")
	plt.show()

else:
	print(f"\nSolver failed: {solution.message}")
