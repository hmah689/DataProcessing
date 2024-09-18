import matplotlib.pyplot as plt
import scienceplots 
import numpy as np
import os

folder = 'NotShorted'
# subfolder = '100AC'
# filename = '1AFreq.txt'

# subfolderList = ['10AC','20AC','30AC','40AC','50AC','60AC','70AC','80AC','90AC','100AC']
# filenameList = ['0AFreq.txt','1AFreq.txt','5AFreq.txt','10AFreq.txt','15AFreq.txt']

subfolderList = ['10AC','50AC','90AC']
filenameList = ['0AFreq.txt','1AFreq.txt','5AFreq.txt','10AFreq.txt']

# subfolderList = ['10AC']
# filenameList = ['0AFreq.txt','1AFreq.txt','5AFreq.txt','10AFreq.txt']


for subfolder in subfolderList:
    resultPath = subfolder + " Freq Plots"
    try:
        os.mkdir(resultPath)
    except:
        print('Directory Exists')


    plt.style.use('science')
    # Adjust the spacing between subplots
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=2)
    # `wspace` controls the width space between columns
    # `hspace` controls the height space between rows
    fig, ax = plt.subplots(4,1,figsize=(15,10))
    n = 0
    fig.suptitle(subfolder + " Frequency Spectrum", fontsize=14, y=0.9)  # Adjust y to lower the title

    for filename in filenameList:
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

        x = np.array(dataArray[2:,0],dtype= float)
        y = np.array(dataArray[2:,1], dtype= float)

        ax[n].plot(x,y,label=filename.removesuffix("Freq.txt"))
        ax[n].set_xticks(np.arange(0,1300,100))    
        ax[n].set_xlim(0,1300)
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

    fig.savefig(os.path.join(resultPath, subfolder + '.png'))

        # newPlot.show()
