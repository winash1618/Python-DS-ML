"""
Implementation of a basic Kmeans algorithm
• People are slender on Venus than on Earth.
• People of the Martian Republic are taller than on Earth.
• Citizens of the Belt are the tallest of the solar system and
have the lowest bone density due to the lack of gravity.
"""


class KmeansClustering:
    """
    Kmeans class
    """

    def __init__(self, max_iter=20, ncentroid=5):
        """
        Class initializer

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
        self.centroids = np.array([X[elem] for elem in np.random.choice(
            np.arange(X.shape[0]), self.ncentroid, replace=False)])
        for cur in range(self.max_iter):
            x_cpy = np.empty((X.shape[0], self.ncentroid)) * 0
            index = 0
            for elem in self.centroids:
                # x_cpy[..., index] = np.sum(np.abs(X - elem), axis=1)
                x_cpy[..., index] = np.sqrt(np.sum((X - elem)**2, axis=1))
                # cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
                index += 1
            tot = []
            for ind in range(self.ncentroid):
                single = []
                for index in range(x_cpy.shape[0]):
                    if min(x_cpy[index]) == x_cpy[index, ind]:
                        single.append(index)
                tot.append(single)
            temp = []
            for elem in tot:
                centroids_cpy = np.empty((1, X.shape[1])) * 0
                for index in elem:
                    centroids_cpy += X[index]
                temp.append(centroids_cpy / len(elem))
            self.centroids = np.squeeze(np.array(temp))
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
        x_cpy = np.empty((X.shape[0], self.ncentroid)) * 0
        i = 0
        for elem in self.centroids:
            x_cpy[..., i] = np.sum(np.abs(X - elem), axis=1)
            i += 1
        tot = []
        for d in range(self.ncentroid):
            single = []
            for i in range(x_cpy.shape[0]):
                if min(x_cpy[i]) == x_cpy[i, d]:
                    single.append(i)
            tot.append(single)
        print(tot)


if __name__ == "__main__":
    import argparse
    import matplotlib.pyplot as plt
    import numpy as np
    print("Usage: python Kmeans.py './resources/solar_system_census.csv' 4 30")
    parser = argparse.ArgumentParser(
        description='Perform K-means clustering on data.')
    parser.add_argument('filepath', type=str,
                        help='Path to the CSV file containing the data')
    parser.add_argument('ncentroid', type=int,
                        help='Number of clusters to find')
    parser.add_argument('max_iter', type=int,
                        help='Maximum number of iterations to perform')
    args = parser.parse_args()
    data = np.genfromtxt(args.filepath, delimiter=',', skip_header=True)
    data = data[..., 1:]
    kmeanObject = KmeansClustering(30, 4)
    print(data[:100])
    kmeanObject.fit(data[:100])
    kmeanObject.predict(data[101:])
    fig, ax = plt.subplots()
    plt.scatter(data[..., 0], data[..., 1])
    plt.scatter(kmeanObject.centroids[..., 0],
                kmeanObject.centroids[..., 1], c='r')
    ax.set_xlabel('height')
    ax.set_ylabel('weight')
    ax.set_title('Height vs Weight')
    plt.show()
    plt.savefig("Height vs Weight")
    fig, ax = plt.subplots()
    plt.scatter(data[..., 0], data[..., 2])
    plt.scatter(kmeanObject.centroids[..., 0],
                kmeanObject.centroids[..., 2], c='r')
    ax.set_xlabel('height')
    ax.set_ylabel('bone density')
    ax.set_title('Height vs bone density')
    plt.show()
    plt.savefig("Height vs bone density")
    fig, ax = plt.subplots()
    plt.scatter(data[..., 2], data[..., 1])
    plt.scatter(kmeanObject.centroids[..., 2],
                kmeanObject.centroids[..., 1], c='r')
    ax.set_xlabel('bone density')
    ax.set_ylabel('weight')
    ax.set_title('bone density vs Weight')
    plt.show()
    plt.savefig("bone density vs Weight")
