"""Implementation of a basic Kmeans algorithm
    """


class KmeansClustering:
    """Kmeans class
    """

    def __init__(self, max_iter=20, ncentroid=5):
        """ Class initializer

        Args:
            max_iter (int, optional): number of max iterations to update the centroids
            ncentroid (int, optional):  number of centroids
        """
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        self.centroids = np.random.choice(np.arange(X.shape[0]), self.ncentroid, replace=False)
        print(self.centroids)
        

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """


if __name__ == "__main__":
    import argparse
    import numpy as np
    print("Usage: python Kmeans.py '../ressources/solar_system_census.csv' 4 30")
    parser = argparse.ArgumentParser(description='Perform K-means clustering on data.')
    parser.add_argument('filepath', type=str, help='Path to the CSV file containing the data')
    parser.add_argument('ncentroid', type=int, help='Number of clusters to find')
    parser.add_argument('max_iter', type=int, help='Maximum number of iterations to perform')
    args = parser.parse_args()
    data = np.genfromtxt(args.filepath, delimiter=',', skip_header=True)
    data = data[..., 1:]
    kmeanObject = KmeansClustering(30, 5)
    print(data[:100])
    kmeanObject.fit(data[:100])
    # kmeanObject.predict(data[101:])
    # print(data)
