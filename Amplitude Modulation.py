import numpy as np
import matplotlib.pyplot as plt
wc = 50
wm = 3
A = 1
mu1 = 0.5
mu2 = 1
t = np.arange(0,5,0.001)
mt = np.cos(wm*t)
mc = np.cos(wc*t)
am = mt * mc
#plt.plot(t,am)
AM = (A*np.cos(wc*t))*(1+mu1*np.cos(wm*t))
AM2 = (A*np.cos(wc*t))*(1+mu2*np.cos(wm*t))
plt.subplot(3,1,1)
plt.plot(t,AM,color='green',label='AM mu = 0.5')
plt.plot(t,mt,color='blue',label='m(t)')
plt.title('Amplitude Modulation',fontsize='14')
plt.hlines(0,0,5,color='black')
plt.legend()
plt.subplot(3,1,2)
plt.plot(t,AM2,color='red',label='AM mu = 1.0')
plt.plot(t,mt,color='blue',label='m(t)')
plt.hlines(0,0,5,color='black')
plt.legend()
plt.subplot(3,1,3)
plt.plot(t,mt*mc,color='yellow',label='mt.cos(wct)')
plt.plot(t,mt,color='blue',label='m(t)')
plt.hlines(0,0,5,color='black')
plt.legend()
plt.xlabel('time',fontsize='14', loc='left')
plt.show()