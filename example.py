import numpy as np

if __name__ == '__main__':
    X = np.array([[0], [1], [2], [3], [4], [5]])
    for element in X[:, None]:
        print(element)