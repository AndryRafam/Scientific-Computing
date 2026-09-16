"""
SEIR epidemic model
S: individuals susceptible to the disease
E: individuals who are exposed to the disease
I: individuals who are infected
R: individuals who recovered
"""
# solving using Runge-Kutta of order 5(4)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# define the ODE
def diff_equation(t,y,N,beta,sigma,gamma):
	S,E,I,R = y
	dSdt = -beta*S*I/N
	dEdt = beta*S*I/N - sigma*E
	dIdt = sigma*E - gamma*I
	dRdt = gamma*I
	return np.array([dSdt,dEdt,dIdt,dRdt])

# Initial conditions
N = 1_000_000 # total population (one million)
E0,I0,R0 = 500,100,0
S0 = N-E0-I0-R0
y0 = [S0,E0,I0,R0]

# parameters
beta = 0.5 # transmission rate
sigma = 1/5.2 # incubation rate (5.2 days incubation)
gamma = 1/10 # recovery rate (approx 10 days infectious)

t_span = (0,160) # simulation for 160 days
t_eval = np.linspace(0,160,1000)

# solve the ODE
sol = solve_ivp(diff_equation,
	t_span,
	y0,
	method="RK45",
	args=(N,beta,sigma,gamma),
	t_eval=t_eval)

print(sol)

# plotting
plt.figure(facecolor = "#dddddd", figsize=(12,8))
plt.title("SEIR Model: Explicit Runge-Kutta 5(4)")
#plt.grid(True)
plt.grid(False)
"""
plt.plot(sol.t, sol.y[0], "orange", lw=2, label="S")
plt.plot(sol.t, sol.y[1], "maroon", lw=2, label="E")
plt.plot(sol.t, sol.y[2], "red", lw=2, label="I")
plt.plot(sol.t, sol.y[3], "green", lw=2, label="R")
"""
colors = ["orange", "maroon", "red", "green"]
labels = ["S", "E", "I", "R"]

for i in range(4):
	plt.plot(sol.t, sol.y[i], color=colors[i], lw=2)
	plt.fill_between(sol.t, sol.y[i], color=colors[i], alpha=0.4, label=labels[i])

plt.xlabel("Time t, [days]")
plt.ylabel("Numbers of individuals")
plt.legend()
plt.savefig("SEIR_RK45.pdf"); plt.savefig("SEIR_RK45.png")
plt.show()
