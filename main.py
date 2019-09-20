import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

def plotLine(theta0, theta1, X, y):
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100

    xplot = np.linspace(min_x, max_x, 1000)
    yplot = theta0 + theta1 * xplot

    plt.plot(xplot, yplot, color='#ff0000', label='Regression Line')
    plt.scatter(X,y)
    plt.axis([-10, 10, 0, 200])
    plt.show()

def predictPrice(x,theta):
    return np.dot(x,theta)

def calculateCost(x,theta,Y):
    prediction = predictPrice(x,theta)
    return ((prediction - Y)**2).mean()/2

def main():
    data = pd.read_csv("data.csv") 
    print(data['km'].values)

if __name__ == '__main__':
    main()
