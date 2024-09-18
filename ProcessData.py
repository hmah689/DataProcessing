import matplotlib.pyplot as plt
import scienceplots 
import numpy as np
import os

folder = 'NotShorted'
# subfolder = '100AC'
# filename = '1AFreq.txt'

subfolderList = ['10AC','20AC','30AC','40AC','50AC','60AC','70AC','80AC','90AC','100AC']
filenameList = ['0AFreq.txt','1AFreq.txt','5AFreq.txt','10AFreq.txt','15AFreq.txt']

for subfolder in subfolderList:
    resultPath = subfolder + " Freq Plots"
    try:
        os.mkdir(resultPath)
    except:
        print('Directory Exists')
        
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

        newPlot = plt
        newPlot.figure(figsize=(10, 6))
        newPlot.style.use('science')
        newPlot.xticks(np.arange(0,1300,100))
        # newPlot.yticks(np.arange())

        newPlot.xlim(0,1300)
        newPlot.ylim(0,0.03)
        newPlot.plot(x,y)
        title = "{}A AC and {} DC Frequency Spectrum".format(subfolder.removesuffix("AC"),filename.removesuffix("Freq.txt"))
        newPlot.title(title)
        newPlot.ylabel("Magnitude")
        newPlot.xlabel("Frequency (Hz)")

        newPlot.savefig(os.path.join(resultPath, title + '.svg'))
        # newPlot.show()
