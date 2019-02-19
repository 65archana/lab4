import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
def mean(lst): return sum(lst)/len(lst)
fs,l=wav.read('amma.wav')
t=np.arange(0,len(l)/fs,1.0/fs)
noise=np.random.normal(0,10,l.shape)
plt.subplot(411)
plt.title('sin wave')
plt.plot(t,l)
a=list([l])
noise1=l+noise
plt.subplot(412)
plt.title('noise')
plt.plot(noise)
plt.subplot(413)
plt.title('noise sin')
l=abs(l)
rea=np.zeros_like(l)
for i in range(len(l)):
		rea[i]=mean(g[max(i-1000,0):i+1])
plt.subplot(414)
plt.title('mean avg')
plt.plot(range(len(l)))
plt.show()
#l=noise
