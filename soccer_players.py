import csv
import matplotlib.pyplot as plt
import numpy as np
import os

age_list = []
experience_list = []
x = None
y = None
b_0, b_1 = None, None

cwd = os.getcwd()
files = os.listdir(cwd)


def simlincoef(x, y):

    n = 0
    m = 0

    for i in range(len(x)):
        n = n + (x[i]-np.mean(x))*(y[i]-np.mean(y))
        m= m + (x[i] - np.mean(x))**2



    b_1 = n/m
    b_0 = (np.mean(y) - b_1 * np.mean(x))
    print(b_1)
    print(b_0)
    return b_0, b_1

def simlin_plot(x,y, b0,b1):

    plt.scatter(x, y)
    plt.title('Simple Linear Regression')
    plt.xlabel('Age')
    plt.ylabel('Experience')

    A = b_1*x + b_0

    plt.plot(x,A, 'r')
    plt.show()

with open('team.csv', newline='') as csvfile:
    list = csv.reader(csvfile, delimiter=',')
    counter = 0
    for row in list:
        if counter == 0:
            counter += 1
            pass
        else:
            age_list.append(int(row[4]))
            experience_list.append(int(row[6]))
            counter += 1

x = np.array(age_list)
y = np.array(experience_list)

[b_0, b_1] =  simlincoef(x,y)
simlin_plot(x,y,b_0,b_1)
