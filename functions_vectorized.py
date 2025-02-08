import numpy as np


def prod_non_zero_diag(x):
    return x.diagonal().prod()


def are_multisets_equal(x, y):
    np.sort(x)
    np.sort(y)
    return np.array_equal(x, y)


def max_after_zero(x):
    index_zero = np.array(np.where(x == 0)) + 1
    element_after_zero = x[index_zero]
    if element_after_zero.shape[0] > 0:
        return -1
    return element_after_zero.max()


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Vectorized implementation.
    """

    pass


def run_length_encoding(x):
    return np.unique(x, return_counts=True)


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Vctorized implementation.
    """

    pass
