import matplotlib.pyplot as plt
import numpy as np
import csv

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

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(tA,yA,'b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frqA,abs(Y_A),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.show()


with open('sigB.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tB.append(float(row[0])) # leftmost column
        dataB.append(float(row[1])) # second column




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

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(tB,yB,'r')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frqB,abs(Y_B),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.show()


with open('sigC.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tC.append(float(row[0])) # leftmost column
        dataC.append(float(row[1])) # second column

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

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(tC,yC,'g')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frqC,abs(Y_C),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.show()


with open('sigD.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tD.append(float(row[0])) # leftmost column
        dataD.append(float(row[1])) # second column

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

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(tD,yD,'b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frqD,abs(Y_D),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.show()




