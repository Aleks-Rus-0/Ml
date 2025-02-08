def prod_non_zero_diag(x):
    ans = 1
    for i in range(min(len(x), len(x[0]))):
        if x[i][i] != 0:
            ans *= x[i][i];
    return ans;


def are_multisets_equal(x, y):
    if x.shape[0] != y.shape[0]:
        return False
    x.sort()
    y.sort()
    for i in range(x.shape[0]):
        if x[i] != y[i]:
            return False
    return True


def max_after_zero(x):
   def max_after_zero(x):
    ans = -1
    for i in range(1, len(x)):
        if x[i - 1] == 0:
            ans = max(ans, x[i])
    return ans


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    pass


def run_length_encoding(x):
    x.sort()
    element = [x[0]]
    count = []
    cnt = 1
    for i in range(1, len(x)):
        if x[i - 1] != x[i]:
            element.append(x[i])
            count.append(cnt)
            cnt = 1
        else:
            cnt += 1
    count.append(cnt)
    return [element, count]


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """

    pass
