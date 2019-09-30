import sys
import pandas as pd
import numpy as py
import matplotlib.pyplot as plt

theta0 = 0.0
theta1 = 0.0

def estimatePrice(mileage):
    return (theta0 + (theta1 * mileage))

"""
def estimatePrice(x,theta):
    return np.dot(x,theta)
"""

def learningRate(x,theta,Y):
    prediction = estimatePrice(x,theta)
    return ((prediction - Y)**2).mean()/2

def main():
    print("Please enter valid mileage (int):")
    for line in sys.stdin:
        line.rstrip()
        try:
            mileage = int(line)
            if mileage > 0:
                break
            else:
                print("Mileage can't be negative, try again:")
        except ValueError:
            print("Error, please enter valid mileage (int):")
    print(estimatePrice(mileage))

if __name__ == '__main__':
    main()
