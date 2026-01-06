"""
SIRD: Susceptible-Infected-Recovered-Deceased
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

N = 1000 # population size
I0 = 3 # initial infected people
R0 = 0 # initial recovered
D0 = 0 # initial deceased
S0 = N-I0-R0-D0 # 997 at the beginning

beta = 0.4 # rates of infection
gamma = 0.035 # rates of recovery
mu = 0.005 # rates of mortality

tmax = 100 # grid of one hundred days
Nt = 100
t_eval = np.linspace(0,tmax,Nt+1)

#define the ODE
def diff_equation(t,y,beta,gamma,mu):
	S,I,R,D = y
	dSdt = -beta*I*S/N
	dIdt = beta*I*S/N - gamma*I - mu*I
	dRdt = gamma*I
	dDdt = mu*I
	return np.array([dSdt,dIdt,dRdt,dDdt])

Y0 = S0,I0,R0,D0 # initial conditions

# solve the ODE using runge-kutta of order 5
sol = solve_ivp(diff_equation,
	[0,tmax],
	Y0,
	method="RK45",
	args=(beta,gamma,mu),
	t_eval=t_eval)
print(sol)

# plotting the solution
plt.figure(facecolor = "#dddddd",figsize=(12,8))
plt.title("SIRD model (S=997, I=3, beta=0.4, gamma=0.035, mu=0.005)")
plt.grid(linestyle="--")
plt.plot(sol.t,sol.y[0],color="blue",lw=2,label="S")
plt.plot(sol.t,sol.y[1],color="orange",lw=2,label="I")
plt.plot(sol.t,sol.y[2],color="green",lw=2,label="R")
plt.plot(sol.t,sol.y[3],color="red",lw=2,label="D")
plt.xlabel("Time, [days]")
plt.ylabel("Individuals")
plt.xlim([0,tmax])
plt.ylim([0,N])
plt.legend()
plt.savefig("SIRD_RK45.png")
plt.show()
