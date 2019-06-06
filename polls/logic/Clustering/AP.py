import numpy as np
import numpy.matlib as mlib
import numpy.linalg as lalib
import matplotlib.pyplot as plt


def inverseEuclid(data):
    n = data.shape[0]  # database size
    S = np.zeros([n, n])  # similarity matrix
    s = np.zeros(n * n - n)  # store pairwise similarities
    idx = 0

    for i in range(n):
        for j in range(n):
            if i != j:
                s[idx] = -lalib.norm(data[i, :] - data[j, :])
                S[i, j] = s[idx]
                idx = idx + 1

    for i in range(n):
        S[i, i] = -50  # np.median(s)

    return S


def affinityPropagationR(data, similarityFunction, lam=0.5, maxiter=100):
    '''
    data: database (n x m matrix)
    lam: dumping factor
    maxiter: maximum number of iterations
    '''

    realmax = np.inf
    n = data.shape[0]  # database size

    S = similarityFunction(data)  # similarity matrix
    R = np.zeros([n, n])  # responsibility matrix
    A = np.zeros([n, n])  # availability matrix

    # Compute similarities #IMPLEMENT THIS!!!

    for it in range(0, maxiter):
        # Compute responsibilities
        Rold = R
        AS = A + S

        ########################
        # print(AS)

        y = np.max(AS, 0)
        idx = np.argmax(AS, 0)

        ########################
        # print(idx)

        for i in range(0, n):
            AS[i, idx[i]] = -realmax  # check this

        ########################
        # print(AS)

        y2 = np.max(AS, 0)
        # idx2 = np.argmax(AS, 0) # Dead code (I think) delete after tests

        # Compute responsibilities
        R = S - mlib.repmat(y, n, 1)

        ###########################
        # print(R)

        for i in range(0, n):
            R[i, idx[i]] = S[i, idx[i]] - y2[i]

        ###########################
        # print(y2)
        # print(R)

        # Dampen responsibilities
        R = (1 - lam) * R + lam * Rold;

        # Compute availabilities
        Aold = A

        # Get the matrix with positive responsibility values
        Rp = np.maximum(R, np.zeros([n, n]))

        # Copy the main diagonal
        for i in range(0, n):
            Rp[i, i] = R[i, i]

        A = mlib.repmat(np.sum(Rp, 1), n, 1) - Rp
        ################
        # print(Rp)

        # Get diagonal of A
        dA = np.diag(A)
        A = np.minimum(A, np.zeros([n, n]))

        for i in range(0, n):
            A[i, i] = dA[i]

        # Dampen availabilities
        A = (1 - lam) * A + lam * Aold

    # End of iteration

    E = R + A  # Pseudo marginals
    ####################
    # print(R)
    # print(A)
    # print(np.diag(E))
    # print(np.diag(E)>0)

    idx = np.argwhere(np.diag(E) > 0)  # Indices of exemplars
    idx = idx[:, 0]
    c = np.argmax(S[:, idx], 0)
    exemplars = idx

    return (c, exemplars)


def affinityPropagationR2(data, similarityFunction, lam=0.5, maxiter=100):
    '''
    data: database (n x m matrix)
    lam: dumping factor
    maxiter: maximum number of iterations
    '''

    realmax = np.inf
    n = data.shape[0]  # database size

    S = similarityFunction(data)  # similarity matrix
    R = np.zeros([n, n])  # responsibility matrix
    A = np.zeros([n, n])  # availability matrix

    # Compute similarities #IMPLEMENT THIS!!!

    for it in range(0, maxiter):

        # print('{:d} of {:d}'.format(it,maxiter))
        # Compute responsibilities
        Rold = R
        AS = A + S

        # print('Compute responsibilities...')
        for i in range(0, n):
            for j in range(0, n):
                # find max in row i (of AS) such that k != j
                maxAS = -realmax
                for k in range(0, n):
                    if k != j and AS[i, k] > maxAS:
                        maxAS = AS[i, k]
                R[i, j] = S[i, j] - maxAS

        # Dampen responsibilities
        R = (1 - lam) * R + lam * Rold;

        # print('Compute Availabilities...')
        # Compute availabilities
        Aold = A

        # Get the matrix with positive responsibility values
        for i in range(0, n):
            for j in range(0, n):
                acc = 0
                if i != j:
                    for k in range(0, n):
                        if k != i and k != j:
                            acc = acc + np.maximum(0, R[k, j])
                    A[i, j] = np.minimum(0, R[j, j] + acc)
                else:
                    for k in range(0, n):
                        if k != j:
                            acc = acc + np.maximum(0, R[k, j])
                    A[i, j] = acc

        # Dampen availabilities
        A = (1 - lam) * A + lam * Aold

    # End of iteration

    E = R + A  # Pseudo marginals
    ####################
    print(E)
    # print(A)
    # print(np.diag(E))
    # print(np.diag(E)>0)

    idx = np.argwhere(np.diag(E) > 0)  # Indices of exemplars
    idx = idx[:, 0]
    c = np.argmax(S[:, idx], 0)
    exemplars = idx

    return (c, exemplars)