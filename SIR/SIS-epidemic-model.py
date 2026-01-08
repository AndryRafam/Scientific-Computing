"""
SIS: Susceptible -> Infectous -> Susceptible
No long-lasting immunity.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

N = 1000 # number of population
I0 = 1. # initial number of infected
S0 = N - I0 # susceptible individuals to infection initially is deduced
beta = 0.25 # infectous rate
gamma = 0.1 # recovery rate
tmax = 100 # grid on one hundred days
Nt = 100
t = np.linspace(0,tmax,Nt+1)

# define the ODE
def diff_equation(t,y,beta,gamma):
	S,I = y
	dSdt = -beta*S*I/N + gamma*I
	dIdt = beta*S*I/N - gamma*I
	return np.array([dSdt,dIdt])

Y0 = S0,I0 # initial conditions

# solve using explicit runge-kutta method of order 5(4)
sol = solve_ivp(diff_equation,
	[0,tmax],
	Y0,
	method="RK45",
	args=(beta,gamma),
	t_eval=t)
print(sol)

# plotting
plt.figure(facecolor = "#dddddd",figsize=(12,8))
plt.title("SIS Model: Susceptible->Infected->Susceptible")
plt.grid()
plt.plot(sol.t,sol.y[0],color="yellow",linestyle="--",lw=2,label="Susceptible")
plt.plot(sol.t,sol.y[1],color="maroon",linestyle="--",lw=2,label="Infected")
plt.xlabel("Time t, [days]")
plt.ylabel("Numbers of individuals")
plt.ylim([0,N+100])
plt.legend()
plt.savefig("SIS_RK45.png")
plt.show()
