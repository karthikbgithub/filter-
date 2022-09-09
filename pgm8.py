from scipy.io import wavfile
from scipy import signal
import dspalgorithm as dsp
import numpy  as np
import matplotlib.pyplot as plt
fs,x=wavfile.read('for1.wav')
x=np.double(x)
fp=1500
fs=3000
ap=3
as1=10
F=8000
N,wc=dsp.buttord(fp,fs,ap,as1,F)
print(N)
print(wc)
b,a=signal.butter(N,wc)
print(b)
print(a)
y=signal.lfilter(b,a,x)
plt.subplot(2,1,1)
plt.plot(x)
plt.subplot(2,1,2)
plt.plot(y)
plt.show()
y=np.int16(y)
wavfile.write(example, 20,y)
