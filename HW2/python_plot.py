import matplotlib.pyplot as plt # for plotting
import numpy as np # for sine function
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

plt.plot(tA,dataA,'b-*')
plt.xlabel('Time [s]')
plt.ylabel('Signal A')
plt.title('Signal A vs Time')
plt.show()


with open('sigB.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tB.append(float(row[0])) # leftmost column
        dataB.append(float(row[1])) # second column
        ##data2.append(float(row[2])) # third column

plt.plot(tB,dataB,'r-*')
plt.xlabel('Time [s]')
plt.ylabel('Signal B')
plt.title('Signal B vs Time')
plt.show()

with open('sigC.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tC.append(float(row[0])) # leftmost column
        dataC.append(float(row[1])) # second column
        ##data2.append(float(row[2])) # third column

plt.plot(tC,dataC,'g-*')
plt.xlabel('Time [s]')
plt.ylabel('Signal C')
plt.title('Signal C vs Time')
plt.show()


with open('sigD.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        tD.append(float(row[0])) # leftmost column
        dataD.append(float(row[1])) # second column
        ##data2.append(float(row[2])) # third column

plt.plot(tD,dataD,'y-*')
plt.xlabel('Time [s]')
plt.ylabel('Signal D')
plt.title('Signal D vs Time')
plt.show()



#Calculating sample rate
samp_rate_A = len(dataA)/ max(tA)
samp_rate_B = len(dataB)/ max(tB)
samp_rate_C = len(dataC)/ max(tC)
samp_rate_D = len(dataD)/ max(tD)


