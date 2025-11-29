import numpy as np


def normalize(v):
    return np.linalg.norm(v)


def rotaion_y(theta):
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 0]])


def rotaion_x(theta):
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 0]])


def orthographic():
    # returns 2d array with ones on the diagonal and zero in all other places
    # AKA: identity matrix
    return np.eye(4)


def apply_matrix(v, M):
    return (M @ v.reshape(4, 1)).flatten()


def face_normal(v0, v1, v2):
    a = v1[:3] - v0[:3]
    b = v2[:3] - v0[:3]
    n = np.cross(a, b)
    return normalize(n)


def dot(v0, v1):
    if len(v0) != len(v1):
        raise Exception("Vecots don't have same nuber of components")
    sum = 0
    for i, x in enumerate(v0):
        y = v1[i]
        sum = sum + x * y
    return sum
