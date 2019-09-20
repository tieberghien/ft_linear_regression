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

def plot(X, Y, b0, b1):
#plotting values 
    x_max = np.max(X) + 100
    x_min = np.min(X) - 100
    #calculating line values of x and y
    x = np.linspace(x_min, x_max, 1000)
    y = b0 + b1 * x
    #plotting line 
    plt.plot(x, y, color='#00ff00', label='Linear Regression')
    #plot the data point
    plt.scatter(X, Y, color='#ff0000', label='Data Point')
    # x-axis label
    plt.xlabel('Kilometers')
    #y-axis label
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def main():
    data = pd.read_csv("data.csv")
    X = data['km'].values
    Y = data['price'].values

    x_mean = np.mean(X)
    y_mean = np.mean(Y)

    n = len(X)
    numerator = 0
    denominator = 0
    for i in range(n):
        numerator += (X[i] - x_mean) * (Y[i] - y_mean)
        denominator += (X[i] - x_mean) ** 2

    b1 = numerator / denominator
    b0 = y_mean - (b1 * x_mean)
    print(b1, b0)
    plot(X, Y, b0, b1)

if __name__ == '__main__':
    main()
