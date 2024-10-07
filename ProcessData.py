import matplotlib.pyplot as plt
import scienceplots 
import numpy as np
import os


filename = "Force-data.txt"
data = []


with open(filename, 'r') as file:
    i = 0
    for line in file:
        if i != 0:
            values = line.split()
            data.append(values)
        #update index
        i += 1


plt.figure()
plt.title('Force vs DC')
plt.xlabel("DC Offeset (A)")
plt.ylabel("Break Force (N)")

# #get 0AC trend, ignore first element which is 0AC header
# y = data[1][1:]
y = []
for num in data[1][1:]:
    y.append(float(num))

# x = data[0
x = []
for num in data[0]:
    x.append(float(num))

plt.grid(True)
# Enable minor gridlines
plt.minorticks_on()  # Turn on the minor ticks
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)  # Customize minor gridlines

plt.plot(x,y)
plt.savefig("Force-data.png")



#####---------------------------------------------------------------------------
# do again for AC
plt.figure()
plt.title('Force vs DC Bias')
plt.xlabel("DC Offeset (A)")
plt.ylabel("Break Force (N)")

x = []
for num in data[0]:
    x.append(float(num))

y = []
for i in range(2,6):
    for num in data[i][1:]:
        y.append(float(num))

    plt.plot(x,y,label = data[i][0] + "A AC")
    y = []
plt.grid(True)
# Enable minor gridlines
plt.minorticks_on()  # Turn on the minor ticks
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)  # Customize minor gridlines

plt.legend()
plt.savefig("Force-data-ac.png")