
# Spectra CLustering Algorithm




import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import NearestNeighbors

# import kmeans


def euclid(X, Y):
    """
    Returns the pair-wise euclidean distance between two data matrices.
    :param X: NxD matrix.
    :param Y: MxD matrix.
    :return: NxM euclidean distance matrix.
    """
    return euclidean_distances(X, Y)


def gaussian_kernel(X, sigma):
    """
    Calculates the gaussian kernel similarity of the given distance matrix.
    :param X: A NxN distance matrix.
    :param sigma: The width of the Gaussian in the heat kernel.
    :return: NxN similarity matrix.
    """
    return np.exp(-np.square(X) / (2 * np.square(sigma)))


def mnn(X, m):
    """
    Calculates the m nearest neighbors similarity of the given distance matrix.
    :param X: A NxN distance matrix.
    :param m: The number of nearest neighbors.
    :return: NxN similarity matrix.
    """
    _, indices = NearestNeighbors(n_neighbors=m, metric='euclidean').fit(X).kneighbors(X)

    nn = np.zeros(X.shape)
    np.put_along_axis(nn, indices, 1, axis=1)

    nn += nn.T
    nn[nn == 2] = 1

    return nn


def spectral(X, k, similarity_param, similarity=gaussian_kernel):
    """
    Cluster the data into k clusters using the spectral clustering algorithm.
    :param X: A NxD data matrix.
    :param k: The number of desired clusters.
    :param similarity_param: m for mnn, sigma for the Gaussian kernel.
    :param similarity: The similarity transformation of the data.
    :return: clustering, as in the kmeans implementation.
    """
    S = euclid(X, X)
    W = similarity(S, similarity_param)
    D = np.diag(np.sum(W, axis=1))

    inverse_D_root = np.diag(np.power(D.diagonal(), -0.5))
    L = np.identity(X.shape[0]) - inverse_D_root.dot(W).dot(inverse_D_root)

    eigval, eigvec = np.linalg.eig(L)

    idx = np.argpartition(eigval, k)
    lowest_k = eigvec[:, idx[:k]]

    return 0
