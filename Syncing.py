#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sounddevice as sd
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import time
from scipy import signal



# In[2]:


duration = 5  # seconds
fs = 44100
sd.default.device = 1
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)

data, samplerate = sf.read(r'C:\Users\Hp\Desktop\fear2.wav')
print(samplerate)




# In[ ]:

data2 = data[0::30,1]


# o
sd.wait()
tic = time.clock()
a = signal.correlate(data2,myrecording[0::30,0],"full")
toc = time.clock()
print(max(a))
plt.plot(a)
id = a.argmax()
print(id)

ti = 3.02*60
l = len(data)/ti
m = int(30*id + l*(toc-tic+0.5))
y = data[m:,0]
sd.default.device = 3
sd.play(y)
time.sleep(10)
sd.stop()



# In[ ]:




