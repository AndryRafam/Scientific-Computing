import numpy as np
from scipy.integrate import quad

I_quad, est_err_quad = \
		quad(np.sin,0,np.pi)
print(I_quad)
err_quad = 2-I_quad
print(est_err_quad,err_quad)
