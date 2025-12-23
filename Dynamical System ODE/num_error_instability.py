import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

# define step size
h = 0.1
# define numerical grid
t = np.arange(0,5.1,h)
# oscillation freq. of pendulum
w = 4
s0 = np.array([[1],[0]])

# define matrix of explicit euler
m_e = np.array([[1,h],[-w**2*h,1]])

# define matrix of implicit euler
m_i = inv(np.array([[1,-h],[w**2*h,1]]))

# define matrix of trapezoidal
m_t = np.dot(inv(np.array([[1,-h/2],[w**2*h/2,1]])), np.array([[1,h/2],[-w**2*h/2,1]]))

s_e = np.zeros((len(t),2))
s_i = np.zeros((len(t),2))
s_t = np.zeros((len(t),2))

# do integrations
s_e[0,:] = s0.T
s_i[0,:] = s0.T
s_t[0,:] = s0.T

for x in range(0,len(t)-1):
	s_e[x+1,:] = np.dot(m_e,s_e[x,:])
	s_i[x+1,:] = np.dot(m_i,s_i[x,:])
	s_t[x+1,:] = np.dot(m_t,s_t[x,:])

plt.figure(figsize = (12,8))
plt.plot(t,s_e[:,0],"b-")
plt.plot(t,s_i[:,0],"g:")
plt.plot(t,s_t[:,0],"r--")
plt.plot(t,np.cos(w*t),"k")
plt.ylim([-3,3])
plt.xlabel("t")
plt.ylabel("$\Theta(t)$")
plt.legend(["Explicit","Implicit","Trapezoidal","Exact"],loc="upper left")
plt.show()