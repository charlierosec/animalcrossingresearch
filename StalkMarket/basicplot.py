# Author : Charlie Rose
#   Date : 5.15.2020
#
# Basic Plot of Selling Prices
#   Uses matplotlib library to plot out the basic selling trends

import matplotlib.pyplot as plt

if __name__ == "__main__":
    fin = open("sellingprices.csv")
        
    fdata = []
    pltdata = []
    firstLine = True

    for line in fin.readlines():
        if firstLine:
            firstLine = False
            continue
        point = line.split(",")
        point[-1] = int(point[-1][:-1])
        point[-2] = int(point[-2])

        fdata.append(point)
        pltdata.append(point[-2])
    
    plt.plot(pltdata)
    plt.savefig("basictrend.png")
    plt.show()

