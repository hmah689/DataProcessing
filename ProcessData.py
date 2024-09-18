import matplotlib.pyplot as plt
import scienceplots 
from scipy import integrate
import numpy as np
import os



folder = 'NotShorted'
subfolderList = ['10AC','50AC','90AC']
filenameList = ['0ATime.txt','1ATime.txt','5ATime.txt','10ATime.txt']


for subfolder in subfolderList:

    #make result directory
    resultPath = subfolder + " Freq Plots"
    try:
        os.mkdir(resultPath)
    except:
        print('Directory Exists')
    #file
    plt.style.use('science')
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=2)     # Adjust the spacing between subplots
    # `wspace` controls the width space between columns
    # `hspace` controls the height space between rows
    fig, ax = plt.subplots(4,1,figsize=(15,10))
    fig.suptitle(subfolder + " Frequency Spectrum", fontsize=14, y=0.9)  # Adjust y to lower the title

    n = 0
    for filename in filenameList:

        #Get the data
        dataPath = os.path.join(folder,subfolder,filename)
        with open(dataPath,'r') as file:
            data = file.readlines()

        line = data[0].replace('\n','')
        cols = line.split('\t')
        dataArray = np.array(cols)

        for i in range(1,len(data)):
            line = data[i].replace('\n','') #remove the newline char
            cols = line.split('\t')
            dataArray = np.vstack([dataArray,cols]) #vertically append



        time = np.array(dataArray[2:,0],dtype= float)
        index = np.where(time == 0.5)[0] #find index for 1 second

        x = np.array(time[0:index[0]],dtype= float)
        y = np.array(dataArray[2:index[0]+2,1], dtype= float)

        velocity_cumulative = integrate.cumulative_trapezoid(y, x,initial=2)
        displacement_cumulative = integrate.cumulative_trapezoid(velocity_cumulative,x,initial = 0)

        ax[n].plot(x,displacement_cumulative,label=filename.removesuffix("Freq.txt"))
        # ax[n].set_xticks(np.arange(0,1300,100))    
        # ax[n].set_xlim(0,1300)
        # ax[n].set_ylim(0,0.015)

        # title = filename.removesuffix('Freq.txt') + ' DC'
        # ax[n].set_title(title)
        # ax[n].set_ylabel("Magnitude")
        # ax[n].set_xlabel("Frequency (Hz)")
        # Add master x and y axis labels

        ax[n].legend()
        n += 1


    fig.text(0.5, 0.09, 'Frequency (Hz)', ha='center', fontsize=14)
    fig.text(0.08, 0.5, 'Magnitude', va='center', rotation='vertical', fontsize=14)

    # Adjust layout to prevent overlap
    plt.tight_layout(rect=[0.1, 0.1, 0.9, 0.9])  # Leave space for master labels

    fig.savefig(os.path.join(resultPath, subfolder + ' Time' +'.png'))

        # newPlot.show()
