# butterfly effect

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
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

sigma = 10.0
rho = 28.0
beta = 8/3.0

# initial conditions
initial_conditions_1 = [0,-2,0]
# slightly perturb the coordinates
initial_conditions_2 = [0,-2-1e-5,0]

t_span = (0,80)
t_eval = np.linspace(t_span[0],t_span[1],7000)

print(f"Trajectory 1 with initial conditions: {initial_conditions_1}")
print(f"Trajectory 2 with initial conditions: {initial_conditions_2}")

# solving the equations using Explicit Runge-Kutta of order 5(4)
sol1 = integrate.solve_ivp(
	diff_lorenz,
	t_span,
	initial_conditions_1,
	method="RK45",
	args=(sigma,rho,beta),
	t_eval=t_eval)

sol2 = integrate.solve_ivp(
	diff_lorenz,
	t_span,
	initial_conditions_2,
	method="RK45",
	args=(sigma,rho,beta),
	t_eval=t_eval)

if sol1.success and sol2.success:
	x1,y1,z1 = sol1.y
	x2,y2,z2 = sol2.y

	fig = plt.figure(figsize=(12,10))

	# Plotting the two trajectories on the same grid
	ax = fig.add_subplot(1,2,1,projection="3d")
	ax.plot(x1,y1,z1,lw=0.5,color="blue",linestyle="-",label="Trajectory 1: {}".format(initial_conditions_1),alpha=1)
	ax.plot(x2,y2,z2,lw=0.5,color="red",linestyle="--",label="Trajectory 2: {}".format(initial_conditions_2),alpha=1)
	ax.set_xlim(np.min(x1), np.max(x1))
	ax.set_ylim(np.min(y1), np.max(y1))
	ax.set_zlim(np.min(z1), np.max(z1))
	ax.set_xlabel("X")
	ax.set_ylabel("Y")
	ax.set_zlabel("Z")
	ax.legend()
	ax.grid(False)

	ax = fig.add_subplot(1,2,2,projection="3d")
	line1, = ax.plot([],[],[],lw=0.5,color="blue",linestyle="-",label='Trajectory 1: {}'.format(initial_conditions_1),alpha=1)
	line2, = ax.plot([],[],[],lw=0.5,color="red",linestyle="--",label='Trajectory 2: {}'.format(initial_conditions_2),alpha=1)
	point1, = ax.plot([],[],[],"ko",markersize=5)
	point2, = ax.plot([],[],[],"go",markersize=5)

	def update(num):
		line1.set_data_3d(x1[:num], y1[:num], z1[:num])
		point1.set_data_3d(x1[num:num+1], y1[num:num+1], z1[num:num+1])
		line2.set_data_3d(x2[:num], y2[:num], z2[:num])
		point2.set_data_3d(x2[num:num+1], y2[num:num+1], z2[num:num+1])
		return line1, point1, line2, point2

	ax.set_xlim(np.min(x1), np.max(x1))
	ax.set_ylim(np.min(y1), np.max(y1))
	ax.set_zlim(np.min(z1), np.max(z1))
	ax.set_xlabel("X")
	ax.set_ylabel("Y")
	ax.set_zlabel("Z")
	ax.legend()
	ax.grid(False)
	
	# Animate the trajectory
	ani = FuncAnimation(fig,update,frames=len(t_eval),
		interval=3, blit=True, repeat=False)
	#ani.save('butterfly_effect.mp4', writer='ffmpeg', fps=30)

	plt.show()

	# euclidean distance between the two trajectories over time
	euclid_dist = np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)

	plt.figure(facecolor="#dddddd",figsize=(10,6))
	plt.plot(t_eval,euclid_dist,color="blue",alpha=1)
	plt.xlabel("Time")
	plt.ylabel("Euclidean distance between trajectories")
	plt.title("Divergence of two lorenz trajectories over time")
	plt.grid(True)
	plt.yscale("log")
	plt.savefig("euclidean distance.pdf"); plt.savefig("euclidean distance.png")
	plt.show()

else:
	# if one or both solutions failed
	print("One or both solvers failed.")
	if not sol1.success: print(f"Solver 1 failed: {sol1.message}")
	if not sol2.success: print(f"Solver 2 failed: {sol2.message}")	
