import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as const

c = const.c.value
h = const.h.value
k = const.k_B.value

def planck(T, l):
	num = 2.0*h*c**2
	a = h*c/(l*1e-6*k*T)
	denom = (l*1e-6)**5*(np.exp(a)-1.0)
	return num*1e-9/denom

T = [300,1000,3000,6000]
L = np.logspace(-2,3,500)

cm = ['blue','green','yellow','red']
const = []

for i in range(0,4):
	temp = T[i]
	B = planck(temp, L)
	index = np.unravel_index(np.argmax(B),B.shape)
	const.append(L[index]*1e-6*temp)
	plt.plot(L,B*1e9, color=cm[i])
	plt.pause(1e-6)

mean = sum(const)/4
print('The constant \lambda_max * T is ',mean,'m K')

plt.xlabel('$\lambda$ ($\mu$m)')
plt.ylabel('I($\lambda$,T)  W m$^{-2}$ nm$^{-1}$')
plt.xscale('log')
plt.yscale('log')
plt.xlim(0.01,1000)
plt.ylim(1e-3,1e15)
plt.tick_params(axis="y",direction="in",right=True)
plt.tick_params(axis="x",direction="in",top=True)
plt.tick_params(axis="y",direction="in",right=True)
plt.tick_params(axis="x", which = 'minor', bottom=False)
plt.legend(('300 K', '1000 K', '3000 K', '6000 K'),loc='upper right')
plt.title('Blackbody radiation curve')
plt.show()
