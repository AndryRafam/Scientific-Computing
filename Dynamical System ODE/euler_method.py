# Suppose the following ODE df(t)/dt = exp(-t)
# f0 = -1, initial condition
# f(t) = -exp(-t), exact solution

import numpy as np
import matplotlib.pyplot as plt

f = lambda t,s: np.exp(-t) # ODE
s0 = -1 # intial condition

# lets see for step size 0.1
h1 = 0.1 # step size
t1 = np.arange(0,1+h1,h1) # numerical grid
s = np.zeros(len(t1))
s[0] = s0

for i in range(0,len(t1)-1):
	s[i+1] = s[i] + h1*f(t1[i],s[i])

plt.figure(figsize = (12,8))
plt.subplot(121)
plt.plot(t1,s,"bo--",label="Approximate Solution")
plt.plot(t1,-np.exp(-t1),"g",label="Exact Solution")
plt.title("Approximate and Exact Solution step size = 0.1")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid()
plt.legend(loc="lower right")

# lets see for step size 0.01
h2 = 0.01 # another step size
t2 = np.arange(0,1+h2,h2) # another numerical grid
s = np.zeros(len(t2))
s[0] = s0

for j in range(0,len(t2)-1):
	s[j+1] = s[j] + h2*f(t2[j],s[j])

plt.subplot(122)
plt.plot(t2,s,"b--",label="Approximate Solution")
plt.plot(t2,-np.exp(-t2),"g",label="Exact Solution")
plt.title("Approximate and Exact Solution step size = 0.01")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid()
plt.legend(loc="lower right")
plt.tight_layout()
plt.show()
