# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 21:21:12 2021

@author: HP
"""

import matplotlib.pyplot as plt
import numpy as np
import csv




def moving_avg(width, newave, signals):
    for i in range(width,len(signals)):
        ave = np.average(signals[(i - width):i])
        newave.append(float(ave))



tA = [] # time for signal A
tB = [] # time for signal B
tC = [] # time for signal C
tD = [] # time for signal D
dataA = [] # signal A
dataB = [] # signal B
dataC = [] # signal C
dataD = [] # signal D


with open('sigA.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tA.append(float(row[0])) # leftmost column
        dataA.append(float(row[1])) # second column
        ##data2.append(float(row[2])) # third column


#Calculating sample rate
Fs_A = len(dataA)/ max(tA)
Ts_A = 1.0/Fs_A; # sampling interval
ts_A = np.arange(0,tA[-1],Ts_A) # time vector
yA = dataA # the data to make the fft from
nA = len(yA) # length of the signal
kA = np.arange(nA)
T_A = nA/Fs_A
frqA = kA/T_A # two sides frequency range
frqA = frqA[range(int(nA/2))] # one side frequency range
Y_A = np.fft.fft(yA)/nA # fft computing and normalization
Y_A = Y_A[range(int(nA/2))]


A_a = 0.99
B_a = 0.01
LP_A = [0]
for i in range(1,len(yA)):
    LP_A.append((A_a*LP_A[i-1]) + (B_a*yA[i]))
    

Fs_Afilt = Fs_A
nAfilt = len(LP_A) # length of the signal
kAfilt = np.arange(nAfilt)
T_Afilt = nAfilt/Fs_Afilt
frqAfilt = kAfilt/T_Afilt # two sides frequency range
frqAfilt = frqAfilt[range(int(nAfilt/2))] # one side frequency range
Y_Afilt = np.fft.fft(LP_A)/nAfilt # fft computing and normalization
Y_Afilt = Y_Afilt[range(int(nAfilt/2))]

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(yA,'b', label='Unfiltered')
ax1.plot(LP_A,'r', label='Filtered')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frqA,abs(Y_A),'b', label='Unfiltered') # plotting the fft
ax2.loglog(frqAfilt,abs(Y_Afilt),'r', label='Filtered') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.legend()
plt.show()







with open('sigB.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tB.append(float(row[0])) # leftmost column
        dataB.append(float(row[1])) # second column
        ##data2.append(float(row[2])) # third column



#Calculating sample rate
Fs_B = len(dataB)/ max(tB)
Ts_B = 1.0/Fs_B; # sampling interval
ts_B = np.arange(0,tB[-1],Ts_B) # time vector
yB = dataB # the data to make the fft from
nB = len(yB) # length of the signal
kB = np.arange(nB)
T_B = nB/Fs_B
frqB = kB/T_B # two sides frequency range
frqB = frqB[range(int(nB/2))] # one side frequency range
Y_B = np.fft.fft(yB)/nB # fft computing and normalization
Y_B = Y_B[range(int(nB/2))]

A_b = 0.99
B_b = 0.01
LP_B = [0]
for i in range(1,len(yB)):
    LP_B.append((A_b*LP_B[i-1]) + (B_b*yB[i]))
    
    
Fs_Bfilt = Fs_B
nBfilt = len(LP_B) # length of the signal
kBfilt = np.arange(nBfilt)
T_Bfilt = nBfilt/Fs_Bfilt
frqBfilt = kBfilt/T_Bfilt # two sides frequency range
frqBfilt = frqBfilt[range(int(nBfilt/2))] # one side frequency range
Y_Bfilt = np.fft.fft(LP_B)/nBfilt # fft computing and normalization
Y_Bfilt = Y_Bfilt[range(int(nBfilt/2))]

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(yB,'b', label='Unfiltered')
ax1.plot(LP_B,'r', label='Filtered')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frqB,abs(Y_B),'b', label='Unfiltered') # plotting the fft
ax2.loglog(frqBfilt,abs(Y_Bfilt),'r', label='Filtered') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.legend()
plt.show()



with open('sigC.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tC.append(float(row[0])) # leftmost column
        dataC.append(float(row[1])) # second column
        ##data2.append(float(row[2])) # third column

#Calculating sample rate
Fs_C = len(dataC)/ max(tC)
Ts_C = 1.0/Fs_C; # sampling interval
ts_C = np.arange(0,tC[-1],Ts_C) # time vector
yC = dataC # the data to make the fft from
nC = len(yC) # length of the signal
kC = np.arange(nC)
T_C = nC/Fs_C
frqC = kC/T_C # two sides frequency range
frqC = frqC[range(int(nC/2))] # one side frequency range
Y_C = np.fft.fft(yC)/nC # fft computing and normalization
Y_C = Y_C[range(int(nC/2))]

A_c = 0.6
B_c = 0.4
LP_C = [0]
for i in range(1,len(yC)):
    LP_C.append((A_c*LP_C[i-1]) + (B_c*yC[i]))


Fs_Cfilt = Fs_C
nCfilt = len(LP_C) # length of the signal
kCfilt = np.arange(nCfilt)
T_Cfilt = nCfilt/Fs_Cfilt
frqCfilt = kCfilt/T_Cfilt # two sides frequency range
frqCfilt = frqCfilt[range(int(nCfilt/2))] # one side frequency range
Y_Cfilt = np.fft.fft(LP_C)/nCfilt # fft computing and normalization
Y_Cfilt = Y_Cfilt[range(int(nCfilt/2))]

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(yC,'b', label='Unfiltered')
ax1.plot(LP_C,'r', label='Filtered')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frqC,abs(Y_C),'b', label='Unfiltered') # plotting the fft
ax2.loglog(frqCfilt,abs(Y_Cfilt),'r', label='Filtered') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.legend()
plt.show()



with open('sigD.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tD.append(float(row[0])) # leftmost column
        dataD.append(float(row[1])) # second column
        ##data2.append(float(row[2])) # third column

#Calculating sample rate
Fs_D = len(dataD)/ max(tA)
Ts_D = 1.0/Fs_D; # sampling interval
ts_D = np.arange(0,tD[-1],Ts_D) # time vector
yD = dataD # the data to make the fft from
nD = len(yD) # length of the signal
kD = np.arange(nD)
T_D = nD/Fs_D
frqD = kD/T_D # two sides frequency range
frqD = frqD[range(int(nD/2))] # one side frequency range
Y_D = np.fft.fft(yD)/nD # fft computing and normalization
Y_D = Y_D[range(int(nD/2))]

A_d = 0.9
B_d = 0.1
LP_D = [0]
for i in range(1,len(yD)):
    LP_D.append((A_d*LP_D[i-1]) + (B_d*yD[i]))


Fs_Dfilt = Fs_D
nDfilt = len(LP_D) # length of the signal
kDfilt = np.arange(nDfilt)
T_Dfilt = nDfilt/Fs_Dfilt
frqDfilt = kDfilt/T_Dfilt # two sides frequency range
frqDfilt = frqDfilt[range(int(nDfilt/2))] # one side frequency range
Y_Dfilt = np.fft.fft(LP_D)/nDfilt # fft computing and normalization
Y_Dfilt = Y_Dfilt[range(int(nDfilt/2))]

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(yD,'b', label='Unfiltered')
ax1.plot(LP_D,'r', label='Filtered')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frqD,abs(Y_D),'b', label='Unfiltered') # plotting the fft
ax2.loglog(frqDfilt,abs(Y_Dfilt),'r', label='Filtered') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.legend()
plt.show()


