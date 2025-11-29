from math3d import face_normal, normalize, apply_matrix
import numpy as np


def edge(a, b, c):
    return (c[0] - a[0]) * (b[1] - a[1]) - (c[1] - a[1]) * (b[0] - a[0])


def draw_triangle(fb, p0, p1, p2, intensity):
    # bounding box
    min_x = max(int(min(p0[0], p1[0], p2[0])), 0)
    max_x = min(int(max(p0[0], p1[0], p2[0])), fb.width - 1)
    min_y = max(int(min(p0[1], p1[1], p2[1])), 0)
    max_y = min(int(max(p0[1], p1[1], p2[1])), fb.height - 1)

    area = edge(p0, p1, p2)
    if area == 0:
        return

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            w0 = edge(p1, p2, (x, y))
            w1 = edge(p2, p0, (x, y))
            w2 = edge(p0, p1, (x, y))

            if (w0 >= 0 and w1 >= 0 and w2 >= 0) or (w0 <= 0 and w1 <= 0 and w2 <= 0):
                fb.set_pixel(x, y, intensity)


def project_vertex(v, width, height):
    # Orthographic projection:
    x, y = v[0], v[1]

    # map -1..1 → screen
    sx = int((x + 1) * 0.5 * width)
    sy = int((1 - (y + 1) * 0.5) * height)
    return (sx, sy)


def shade_face(v0, v1, v2, light_dir):
    n = face_normal(v0, v1, v2)

    # backface cull
    if n[2] > 0:
        return None

    intensity = -np.dot(n, light_dir)
    return max(0.0, min(1.0, intensity))


def draw_mesh(fb, vertices, faces, M, light_dir):
    # transform all vertices
    transformed = [apply_matrix(v, M) for v in vertices]

    for f in faces:
        v0 = transformed[f[0]]
        v1 = transformed[f[1]]
        v2 = transformed[f[2]]

        intensity = shade_face(v0, v1, v2, light_dir)
        # intensity = 1
        if intensity is None:
            continue

        p0 = project_vertex(v0, fb.width, fb.height)
        p1 = project_vertex(v1, fb.width, fb.height)
        p2 = project_vertex(v2, fb.width, fb.height)

        draw_triangle(fb, p0, p1, p2, intensity)
