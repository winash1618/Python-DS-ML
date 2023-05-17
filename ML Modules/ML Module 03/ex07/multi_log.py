"""
The idea now is to apply what is called one-versus-all classification. It's quite straightforward:
Your program (in multi_log.py) will:
    1. Split the dataset into a training and a test set.
    2. Train 4 logistic regression classifiers to discriminate each class from the others (the
    way you did in part one).
    3. Predict for each example the class according to each classifiers and select the one
    with the highest output probability.
    4. Calculate and display the fraction of correct predictions over the total number of
    predictions based on the test set.
    5. Plot 3 scatter plots (one for each pair of citizen features) with the dataset and the
    final prediction of the model.
"""

import sys
from data_spliter import data_spliter
from my_logistic_regression import MyLogisticRegression as MyLR
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def multi_log_trainer():
    """Mono log program

    Args:
        zipcode (string): zipcode specifies in which planet they are in.
    """
    solar_people_census = pd.read_csv("solar_system_census.csv")
    solar_planet_census = pd.read_csv("solar_system_census_planets.csv")
    x = np.array(solar_people_census[['weight', 'height', 'bone_density']])
    y = np.array(solar_planet_census[['Origin']])
    train_set_x, test_set_x, train_set_y, test_set_y = data_spliter(x, y, 0.8)
    thetas = np.array([[0.5], [77.1], [154.3], [2.09]])
    mylr = MyLR(thetas)
    mylr.fit_(train_set_x, train_set_y)

def main():
    """main
    """
    if len(sys.argv[1:]) != 1:
        print("Usage: python multi_log.py")
    else:
        multi_log_trainer()

if __name__ == "__main__":
    main()
