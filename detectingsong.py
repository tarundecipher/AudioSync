import sounddevice as sd
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import time
import os
from scipy import signal


# In[2]:
files  = os.listdir(r'C:\Users\Hp\Desktop\music\written')
s = 'C:/Users/Hp/Desktop/music/written/'

duration = 5  # seconds
fs = 44100
sd.default.device = 1
print('Started recording')
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
print('Stopped recording')
m = []
for i in range(len(files)):
    data, samplerate = sf.read(s+files[i])
    a = signal.correlate(data,myrecording[0::20,0])
    m.append(np.max(abs(a)))
I = m.index(max(m))
print(files[I])