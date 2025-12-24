import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# ODE: dS(t)/dt = cos(t)
# S0 = 0, initial value
# S(t) = sin(t), exact solution

F = lambda t,s: np.cos(t)
t_eval = np.arange(0,np.pi,0.1)
sol = solve_ivp(F,[0,np.pi],[0],t_eval=t_eval)

plt.figure(figsize = (12,4))
plt.subplot(121)
plt.plot(sol.t,sol.y[0])
plt.xlabel("t")
plt.ylabel("S(t)")
plt.subplot(122)
plt.plot(sol.t,sol.y[0] - np.sin(sol.t))
plt.xlabel("t")
plt.ylabel("S(t) - sin(t)")
plt.tight_layout()
plt.show()

# Lets use the relative tolerance rtol and the absolute tolerance atol
# to make the difference between the approximate
# and exact solution less than 1e-7

sol = solve_ivp(F,[0,np.pi],[0],t_eval=t_eval,\
	rtol = 1e-8, atol = 1e-8)
plt.figure(figsize = (12,4))
plt.subplot(121)
plt.plot(sol.t,sol.y[0])
plt.xlabel("t")
plt.ylabel("S(t)")
plt.subplot(122)
plt.plot(sol.t,sol.y[0] - np.sin(sol.t))
plt.xlabel("t")
plt.ylabel("S(t) - sin(t)")
plt.tight_layout()
plt.show()

# Consider the ODE: dS(t)/dt = -S(t)
# S0 = 1, initial state
# S(t) = exp(-t)
# interval [0 1]

F = lambda t,s: -s

t_eval = np.arange(0,1.01,0.01)
sol = solve_ivp(F,[0,1],[1],t_eval=t_eval)

plt.figure(figsize = (12,4))
plt.subplot(121)
plt.plot(sol.t, sol.y[0])
plt.xlabel("t")
plt.ylabel("S(t)")
plt.subplot(122)
plt.plot(sol.t,sol.y[0] - np.exp(-sol.t))
plt.xlabel("t")
plt.ylabel("S(t) - exp(-t)")
plt.tight_layout()
plt.show()

# Let S(t) = [[x(t)],[y(t)]]
# dS(t)/dt = [[0 t²],[-t 0]]S(t)
# S0 = [[1],[1]], initial state

F = lambda t,s: np.dot(np.array([[0,t**2], [-t,0]]),s)

t_eval = np.arange(0,10.01,0.01)
sol = solve_ivp(F,[0,10],[1,1],t_eval=t_eval)

plt.figure(figsize = (12,8))
plt.plot(sol.y.T[:,0], sol.y.T[:,1])
plt.xlabel("x")
plt.ylabel("y")
plt.show()