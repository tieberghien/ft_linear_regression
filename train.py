import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from optparse import OptionParser

learning_rate = 0.1
max_iters = 1000

def normalize(data):
    new = []
    d = max(data)
    e = min(data)
    for i in range(len(data)):
        new.append((data[i] - e) / (d - e))
    return (new)

def denormalize(theta_0,theta_1,X,Y):
    minx = min(X)
    miny = min(Y)
    maxx = max(X)
    maxy = max(Y)
    theta0 = (theta_0 + theta_1 * (-minx) / (maxx - minx)) * (maxy - miny) + miny
    theta1 = (theta_0 + theta_1 * (1.0 - minx) / (maxx - minx)) * (maxy - miny) + miny - theta0
    return (theta0,theta1)

def calculateError(x,y,m,b):
    error = 0
    for i in range(len(x)):
        error += ((m *x[i] +b - y[i]) **2)
    error /= len(x)
    return (np.sqrt(error))

def gradientDescent(theta0,theta1,X,Y):
    m_gradient=0
    b_gradient=0
    n = len(X)
    for i in range(0,n):
        b_gradient += (theta1*X[i]+theta0) - Y[i]
        m_gradient += ((theta1*X[i]+theta0) - Y[i]) * X[i]
    b_new=theta0-(learning_rate)* (b_gradient / n)
    m_new=theta1-(learning_rate)* (m_gradient / n)
    return (b_new, m_new)

def train(X,Y,theta0,theta1):
    x_norm = normalize(X)
    y_norm = normalize(Y)
    for _ in range(max_iters):
        theta0,theta1 = gradientDescent(theta0,theta1,x_norm,y_norm)
    print(calculateError(x_norm, y_norm, theta0, theta1))
    theta0, theta1 = denormalize(theta0,theta1,X,Y)
    return (theta0, theta1)

def plotLine(X,Y,theta0,theta1):
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
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-g", "--graph", action="store_true")
    (options, args) = parser.parse_args()
    try:
        data = pd.read_csv("data.csv", delimiter=",")
    except FileNotFoundError as e:
        exit(e)
    except pd.errors.EmptyDataError as e:
        exit(e)
    try:
        X = data['km'].values
        Y = data['price'].values
    except Exception as e:
        print("Missing " + str(e))
        exit()
    theta0 = 0
    theta1 = 0
    theta0, theta1 = train(X, Y, theta0, theta1)
    with open("theta.csv","w+") as f:
        f.write('0,1\n{0},{1}\n'.format(float(theta0), float(theta1)))
    f.close()
    if options.graph is True:
        plotLine(X, Y, theta0, theta1)

if __name__ == '__main__':
    main()
