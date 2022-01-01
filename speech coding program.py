# -*- coding: utf-8 -*-
"""


@author: swechchha ojha
"""

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf



''' Defining enframe function '''

def enframe(x, winsize, hoplength, fs, wintype):
    hop_samples = int(fs*hoplength)  # number of samples in one hop
    win_samples =int(fs*winsize)     #number of samples in one frame 
    temp = win_samples - (len(x)%hop_samples) 
    z = np.pad(x,(0,temp),'constant')          #zero padding
    if wintype == 'hamm':                      #windowing
        win =np.hamming(win_samples)
    elif wintype=='rect':
        win=np.ones(win_samples)
    frame =[]
    l =len(x)
    for i in range(0,l,hop_samples):
        a = z[i:i+win_samples]*win
        frame.append(a)
    return(frame)
    

''' Reading sound file'''

data,fs=sf.read("should.wav")
print('sampling rate',fs)

N = len(data)      # total number of samples in the input signal
print('total number of samples : N=',N)


''''plotting '''

n = np.linspace(0,N-1,N)
plt.figure(1)
plt.plot(n,data)
plt.legend(['plot of sample'])
plt.xlabel('sample')
plt.ylabel('amplitude')
plt.title("should.wave signal")
plt.grid()


'''Driving code '''
windowdata = enframe(data, 0.03 ,0.015 ,fs, 'hamm') 
# output of enframe function 
print('size of divided frame matrix (p*w) :',np.shape(windowdata))     #where p=(N/h) and w=no of samples in one window