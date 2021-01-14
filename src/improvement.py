import pandas as pd
from matplotlib import pyplot as plt


def plot_data(data, xlabel, ylabel):
    plt.plot(data, 'r-')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axhline(y=mean, color='b', linestyle='--')
    plt.savefig(str(num_measurements)+'.png')
    plt.show()


def compute_statistics(data):
    mean = sum(data)/num_measurements
    return mean


def read_data(file_name, column):
    data = pd.read_csv(file_name, nrows=num_measurements)
    return data[column]


for num_measurements in [25, 100, 500]:

    temperatures = read_data(file_name='data/temperatures.csv', column='Air temperature (degC)')

    mean = compute_statistics(temperatures)

    plot_data(data=temperatures, xlabel='measurements', ylabel='air temperature (deg C)')