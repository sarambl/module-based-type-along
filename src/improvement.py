import pandas as pd
from matplotlib import pyplot as plt

def plot_temp(temperatures):


    # plot results
    plt.plot(temperatures, 'r-')
    plt.axhline(y=mean, color='b', linestyle='--')

    # visuals for plot:
    plt.xlabel('Time [h]')
    plt.ylabel('Temperature [$^\circ$C]')

    plt.savefig(str(num_measurements)+'.png')

    #plt.clf()
    plt.show()


for num_measurements in [25, 100, 500]:


    # read data from file
    data = pd.read_csv('data/temperatures.csv', nrows=num_measurements)
    temperatures = data['Air temperature (degC)']

    # compute statistics

    mean = sum(temperatures)/num_measurements


    # plot results
    plot_temp(temperatures)

    #plt.clf()
    plt.show()
# %%

