import matplotlib.pyplot as plt
import numpy as np

N = 500
k = 4
plt.figure(1)

s = np.exp(1j*2*np.pi*k/N*np.arange(-N/2, N/2))
plt.subplot(1, 2, 1)
plt.plot(np.arange(-N/2, N/2), np.real(s))
plt.axvline(0, color='r')
plt.axis([-N/2,N/2,-1,1])
plt.title ('cosine')
plt.subplot(1, 2, 2)
plt.plot(np.arange(-N/2, N/2), np.imag(s))
plt.axvline(0, color='r')
plt.axis([-N/2,N/2,-1,1])
plt.title ('sine')
plt.show()