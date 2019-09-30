import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

learning_rate = 0.1
max_iters = 1000
#precision = getPrecision()

def normalize(data):
    d = (data - min(data)) / (max(data) - min(data))
    return (d)

def denormalize(data):
    d = (data * (max(data) - min(data)) + min(data))
    return (d)

def gradientDescent(X, Y):
    x_mean = np.mean(X)
    y_mean = np.mean(Y)

    m = len(X)
    tmp0 = 0
    tmp1 = 0
    for j in range(0, max_iters):
        numerator = 0
        denominator = 0
        for i in range(0, m):
            numerator += (X[i] - x_mean) * (Y[i] - y_mean)
            denominator += (X[i] - x_mean) ** 2
        theta1 = numerator / denominator
        theta0 = y_mean - (learning_rate * theta1 * x_mean)

    print(theta1, theta0)
    plotLine(X, Y, theta0, theta1)
    return (theta0,theta1)

def plotLine(X, Y, theta0, theta1):
    x_max = np.max(X) + 100
    x_min = np.min(X) - 100

    x = np.linspace(x_min, x_max, 1000)
    y = theta0 + theta1 * x

    plt.plot(x, y, color='#00ff00', label='Linear Regression')
    plt.scatter(X, Y, color='#ff0000', label='Data Point')
    plt.xlabel('Kilometers')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def main():
    try:
        data = pd.read_csv("data.csv")
    except FileNotFoundError as e:
        print(e)
        exit()
    except pd.errors.EmptyDataError as e:
        print(e)
        exit()
    X = data['km'].values
    Y = data['price'].values

    theta0, theta1 = gradientDescent(X, Y)
    with open("theta.csv","w+") as f:
        f.write('0,1\n{0},{1}\n'.format(float(theta0), float(theta1)))
    f.close()

if __name__ == '__main__':
    main()
