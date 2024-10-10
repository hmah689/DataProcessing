import matplotlib.pyplot as plt
import scienceplots
import numpy as np
import os

folder = 'NotShorted'
subfolderList = ['10AC', '50AC', '90AC']
filenameList = ['0ATime.txt']
resultPath = 'TimeSeries'

plt.style.use('science')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=2)
fig, ax = plt.subplots(3, 1, figsize=(15, 10))

fig.suptitle("Acceleration Signals with Varying AC", fontsize=14, y=0.9)

# Initialize a list to hold y data for setting limits later
y_values = []

for n, subfolder in enumerate(subfolderList):
    dataPath = os.path.join(folder, subfolder, filenameList[0])
    
    with open(dataPath, 'r') as file:
        data = file.readlines()

    # Read and parse the data
    dataArray = np.array([line.strip().split('\t') for line in data[2:]], dtype=float)
    
    # Assuming time is in the first column
    time = dataArray[:, 0]
    index = np.where(time == 0.5)[0]

    if index.size == 0:
        print(f"No 0.5s timestamp found in {dataPath}. Skipping...")
        continue

    x = time[:index[0]]
    y = dataArray[:index[0], 1]
    y_values.append(y)  # Store y values for later use

    ax[n].plot(x, y)  # Plot without legend
    ax[n].set_title(subfolder)  # Keep titles for each subplot

# Set the same y-limits for all plots based on the min and max of all y values
y_min = min(y.min() for y in y_values)
y_max = max(y.max() for y in y_values)

for a in ax:
    a.set_ylim(y_min, y_max)  # Apply uniform y-axis limits

# Master labels
fig.text(0.5, 0.09, 'Frequency (Hz)', ha='center', fontsize=14)
fig.text(0.08, 0.5, 'Magnitude', va='center', rotation='vertical', fontsize=14)

plt.tight_layout(rect=[0.1, 0.1, 0.9, 0.9])
fig.savefig('Vibrations-in-Time.png')
