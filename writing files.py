import os
import soundfile as sf
import numpy as np
files = os.listdir(r'C:\Users\Hp\Desktop\music')
s = 'C:/Users/Hp/Desktop/music/'
s1 = 'C:/Users/Hp/Desktop/music/written/'
for i in range(len(files)):
    [data,samplerate] = sf.read(s+files[i])
    data = data[0::20,0]
    np.interp(data, (data.min(), data.max()), (-1, +1))
    
    s1 = s1 + files[i][0:len(files[0])-4] + '.wav'
    sf.write(s1, data, samplerate)
    