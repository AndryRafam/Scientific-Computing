# SIR epidemic model
# Runge-Kutta 3(2) solver
# Runge-Kutta 5(4) solver
# Radau

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

N = 1000 # number of population
I0, R0 = 1., 0 # initial number of infected and recovered individual
S0 = N - I0 - R0 # susceptible individuals to infection initially is deduced
beta = 4/10
gamma = 1/10
tmax = 100 # grid of time points (in days)
Nt = 100
t = np.linspace(0,tmax,Nt+1)

# define the ODE
def diff_equation(t,X,beta,gamma):
	S, I, R = X
	dSdt = -beta * S * I / N
	dIdt = beta * S * I / N - gamma * I
	dRdt = gamma * I
	return np.array([dSdt, dIdt, dRdt])

X0 = S0, I0, R0 # initial conditions

# Explicit Runge-Kutta 3(2) solver
solrk23 = integrate.solve_ivp(
	diff_equation,
	[0, tmax],
	X0,
	method="RK23",
	args=(beta,gamma),
	t_eval=t)
print(solrk23)

# plotting
plt.figure(facecolor = "#dddddd", figsize=(12,8))
plt.title("SIR Model: Explicit Runge-Kutta 3(2)")
plt.grid()
plt.plot(solrk23.t, solrk23.y[0], "orange", lw=2, label="Susceptible")
plt.plot(solrk23.t, solrk23.y[1], "r", lw=2, label="Infected")
plt.plot(solrk23.t, solrk23.y[2], "g", lw=2, label="Recovered with immunity")
plt.xlabel("Time t, [days]")
plt.ylabel("Numbers of individuals")
plt.ylim([0,N+100])
plt.legend()
plt.savefig("SIR_RK23.pdf"); plt.savefig("SIR_RK23.png")
plt.show()

# Explicit Runge-Kutta 5(4) solver
solrk45 = integrate.solve_ivp(
	diff_equation,
	[0, tmax],
	X0,
	method="RK45",
	args=(beta,gamma),
	t_eval=t)
print(solrk45)

# plotting
plt.figure(facecolor = "#dddddd", figsize=(12,8))
plt.title("SIR Model: Explicit Runge-Kutta 5(4)")
plt.grid()
plt.plot(solrk45.t, solrk45.y[0], "orange", lw=2, label="Susceptible")
plt.plot(solrk45.t, solrk45.y[1], "r", lw=2, label="Infected")
plt.plot(solrk45.t, solrk45.y[2], "g", lw=2, label="Recovered with immunity")
plt.xlabel("Time t, [days]")
plt.ylabel("Numbers of individuals")
plt.ylim([0,N+100])
plt.legend()
plt.savefig("SIR_RK45.pdf"); plt.savefig("SIR_RK45.png")
plt.show()

# Implicit Runge-Kutta method of the Radau IIA family
solradau = integrate.solve_ivp(
	diff_equation,
	[0, tmax],
	X0,
	method="Radau",
	args=(beta,gamma),
	t_eval=t)
print(solradau)

# plotting
plt.figure(facecolor = "#dddddd", figsize=(12,8))
plt.title("SIR Model: Implicit Runge-Kutta method of the Radau IIA family")
plt.grid()
plt.plot(solradau.t, solradau.y[0], "orange", lw=2, label="Susceptible")
plt.plot(solradau.t, solradau.y[1], "r", lw=2, label="Infected")
plt.plot(solradau.t, solradau.y[2], "g", lw=2, label="Recovered with immunity")
plt.xlabel("Time t, [days]")
plt.ylabel("Numbers of individuals")
plt.ylim([0,N+100])
plt.legend()
plt.savefig("SIR_Radau.pdf"); plt.savefig("SIR_Radau.png")
plt.show()
