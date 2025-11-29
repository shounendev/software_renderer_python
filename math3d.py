import numpy as np


def normalize(v):
    return v / np.linalg.norm(v)


def rotation_y(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, 0, s, 0], [0, 1, 0, 0], [-s, 0, c, 0], [0, 0, 0, 1]])


def rotation_x(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[1, 0, 0, 0], [0, c, -s, 0], [0, s, c, 0], [0, 0, 0, 1]])


def orthographic():
    """For now, identity is enough."""
    return np.eye(4)


def apply_matrix(v, M):
    return (M @ v.reshape(4, 1)).flatten()


def face_normal(v0, v1, v2):
    a = v1[:3] - v0[:3]
    b = v2[:3] - v0[:3]
    n = np.cross(a, b)
    return normalize(n)
