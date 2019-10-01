import sys
import pandas as pd
import numpy as py
import matplotlib.pyplot as plt
import train

theta0 = 0.0
theta1 = 0.0

def estimatePrice(mileage):
    return (float(theta0) + (float(theta1) * mileage))

def predict():
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
    print("The estimated price for a second-hand car with a given mileage of " + str(mileage) + " would be around " + str(estimatePrice(mileage)))

if __name__ == '__main__':
    try:
        data = pd.read_csv("theta.csv")
    except FileNotFoundError as e:
        predict()
        exit()
    except pd.errors.EmptyDataError as e:
        print(e)
        exit()
    theta0 = data['0'].values
    theta1 = data['1'].values   
    predict()
