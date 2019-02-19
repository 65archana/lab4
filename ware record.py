import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plot
fs,d=wav.read('amma.wav')
print(fs,len(d),d)
plot.subplot(411)
plot.plot(d)
t=np.arange(0,len(d)/fs,1.0/fs)
plot.subplot(412)
plot.plot(t,d)
plot.show()
wav.write('ammafast1.wav',2.0*fs,d)
wav.write('ammaslow1.wav',0.7*fs,d)

