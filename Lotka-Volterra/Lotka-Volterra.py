# Lotka-Volterra: Prey - Predator equations
# Runge-Kutta 5(4)

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

alpha = 1. # mortality rate due to predators
beta = 1.
delta = 1.
gamma = 1.

# initial conditions
x0 = 4. # four prey
y0 = 2. # two predators

def diff_equation(t,X,alpha,beta,gamma,delta):
	x,y = X
	dotx = x*(alpha-beta*y)
	doty = y*(-delta+gamma*x)
	return np.array([dotx, doty])

Nt = 1000
tmax = 30.
t = np.linspace(0.,tmax,Nt)
X0 = [x0,y0]
solrk45 = integrate.solve_ivp(
	diff_equation,
	(0,tmax),
	X0,
	method="RK45",
	args=(alpha,beta,gamma,delta),
	t_eval=t)
print(solrk45)

plt.figure(facecolor = "#dddddd",figsize=(12,8))
plt.grid()
plt.title("Lotka-Volterra: Runge-Kutta 5(4)")
plt.plot(solrk45.t,solrk45.y[0],'ob',label='Deer')
plt.plot(solrk45.t,solrk45.y[1],'+r',label='Wolves')
plt.xlabel('Time t, [days]')
plt.ylabel('Population')
plt.legend()
plt.savefig("Lotka-Volterra: Runge-Kutta.pdf"); plt.savefig("Lotka-Volterra: Runge-Kutta.png")
plt.show()

# Lets see what happens if we change beta

import random
import matplotlib.cm as cm

betas = np.arange(0.9,1.4,0.1)
nums = np.random.random((10,len(betas)))
colors = cm.rainbow(np.linspace(0,1,nums.shape[0])) # generate the colors for each data set

fig, ax = plt.subplots(2,1,facecolor="#dddddd",figsize=(12,6))

for beta, i in zip(betas, range(len(betas))):
	solrk45 = integrate.solve_ivp(
		diff_equation,
		(0,tmax),
		X0,
		method="RK45",
		args = (alpha,beta,gamma,delta),
		t_eval=t)
	ax[0].plot(solrk45.t,solrk45.y[0], color=colors[i], linestyle='-', lw=2, label = r"$\beta = $" + "{0:.2f}".format(beta))
	ax[1].plot(solrk45.t,solrk45.y[1], color=colors[i], linestyle='-', lw=2, label = r"$\beta = $" + "{0:.2f}".format(beta))
	ax[0].legend()
	ax[1].legend()

ax[0].grid()
ax[1].grid()
ax[0].set_xlabel('Time t, [days]')
ax[0].set_ylabel('Deer')
ax[1].set_xlabel('Time t, [days]')
ax[1].set_ylabel('Wolves')
plt.savefig("Deer-Wolves.pdf"); plt.savefig("Deer-Wolves.png")
plt.show()

# Phase portrait

plt.figure(facecolor="#dddddd",figsize=(12,6))
IC = np.linspace(1.0,6.0,21) # initial conditions for deer population (prey)
for deer in IC:
	X0 = [deer, 1.0]
	Xs = integrate.solve_ivp(
		diff_equation,
		(0,tmax),
		X0,
		method="RK45",
		args=(alpha,beta,delta,gamma),
		t_eval=t)
	plt.plot(Xs.y[0], Xs.y[1], "-", label = "$x_0 =$"+str(X0[0]))

plt.xlabel("Deer")
plt.ylabel("Wolves")
plt.legend()
plt.title("Phase portrait: Deer vs Wolves")
plt.savefig("Phase portrait: Deer vs Wolves.pdf"); plt.savefig("Phase portrait: Deer vs Wolves.png")
plt.show()

# Phase plane

plt.figure(facecolor="#dddddd",figsize=(12,6))
plt.plot(solrk45.y[0], solrk45.y[1], "blue", "-")
plt.xlabel("Deer")
plt.ylabel("Wolves")
plt.grid()
plt.title("Phase plane: Deer vs Wolves")
plt.savefig("Phase plane: Deer vs Wolves.pdf"); plt.savefig("Phase plane: Deer vs Wolves.png")
plt.show()
