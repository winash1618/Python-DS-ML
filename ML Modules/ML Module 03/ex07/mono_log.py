"""
One Label to Discriminate Them All
    You already wrote a Logistic Regression Classifier that can discriminate between two
    classes. We can use it to solve the problem! Let's start by having it discriminate between
    citizens who come from your favorite planet and everybody else!
    Your program (in mono_log.py) will:
        1. Take an argument: -zipcode=x with x being 0, 1, 2 or 3. If no argument, usage
        will be displayed.
        2. Split the dataset into a training and a test set.
        3. Select your favorite Space Zipcode and generate a new numpy.array to label each
        citizen according to your new selection criterion:
            • 1 if the citizen's zipcode corresponds to your favorite planet.
            • 0 if the citizen has another zipcode.
        4. Train a logistic model to predict if a citizen comes from your favorite planet or not,
        using your brand new label.
        5. Calculate and display the fraction of correct predictions over the total number of
        predictions based on the test set.
        6. Plot 3 scatter plots (one for each pair of citizen features) with the dataset and the
        final prediction of the model.
    You can use normalization on your dataset. The question is: Should you?
    You now have a model that can discriminate between citizens that come from one
    specific planet and everyone else. It's a first step, a good one, but we still have work to
    do before we can classify citizens among four planets!
    So how does Multiclass Logistic Regression work?
"""

import sys
from data_spliter import data_spliter
from my_logistic_regression import MyLogisticRegression as MyLR
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def value_corrector(x, zipcode):
    """To avoid log error

    Args:
        x (float): value to converted
        eps (decimal, optional): value to add. Defaults to 1e-15.

    Returns:
        double: converted value
    """
    if x == zipcode:
        return 1
    else:
        return 0

def mono_log_trainer(zipcode):
    """Mono log program

    Args:
        zipcode (string): zipcode specifies in which planet they are in.
    """
    solar_people_census = pd.read_csv("solar_system_census.csv")
    solar_planet_census = pd.read_csv("solar_system_census_planets.csv")
    x = np.array(solar_people_census[['weight', 'height', 'bone_density']])
    y = np.array(solar_planet_census[['Origin']])
    vec_func = np.vectorize(value_corrector)
    y_new = vec_func(y, zipcode)
    train_set_x, test_set_x, train_set_y, test_set_y = data_spliter(x, y_new, 0.8)
    thetas = np.array([[0.5], [77.1], [154.3], [2.09]])
    mylr = MyLR(thetas)
    mylr.fit_(train_set_x, train_set_y)
    predictions = mylr.predict_(test_set_x)
    correct = np.count_nonzero(predictions == test_set_y)
    total = len(predictions)
    accuracy = correct / total
    print("Accuracy:", accuracy)
    for i in range(3):
        plt.scatter(test_set_x[:, i], test_set_y, c=predictions)
        plt.xlabel(solar_people_census.columns[i])
        plt.ylabel("Origin")
        plt.savefig('image.png')

def main():
    """main
    """
    if len(sys.argv[1:]) != 1:
        print("Usage: python monolog.py -zipcode=x")
    else:
        zipcode = int(sys.argv[1].split('=')[1])
        mono_log_trainer(zipcode)

if __name__ == "__main__":
    main()
