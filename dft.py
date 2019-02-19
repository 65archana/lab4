import matplotlib.pyplot as plt
import numpy as np
p=complex(0,1)
x=[1,5,6,7,8,9]
k=[1,2,3,4,5,6]
N=1000
k=[]
for i in range(0,N-1):
	d=0
	d=d+i
X=[]
w=np.linspace(-np.pi,np.pi,N-1)
for i in range(0,N-1):
	b=0
	for n in range(0,len(x)):
		b=b+(x[n]*np.exp(-n*w[i]*2*np.pi*d*p)/N)
	X.append(b)
plt.subplot(211)
plt.plot(w,np.abs(X))
plt.xlabel('frequency(w/2*m.pi)')
plt.ylabel('magnitude')
plt.title('magnitude spectrum')
plt.subplot(212)
plt.plot(w,np.angle(X))
plt.xlabel('freq(w/2*m.pi)')
plt.ylabel('phase angle in radian')
plt.title('phase spectrum')
plt.show()
