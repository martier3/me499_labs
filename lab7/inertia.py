import numpy as np

def compute_inertia_matrix(array=np.array([]), mass=1):
    n = np.shape(array)[0]
    m = mass/n
    adjustment_array = np.array([1, -1, -1,
                                 -1, 1, -1,
                                 -1, -1, 1])
    for row in array:
        x = row[0]
        y = row[1]
        z = row[2]
        inertia_array_per_row = np.array([m*(y**2 + z**2), m*x*y, m*x*z,
                                            m*x*y, m*(x**2 + z**2), m*y*z,
                                            m*x*z, m*y*z, m*(x**2 + y**2)])
        inertia = np.add(inertia_array_per_row, inertia_array_per_row)
        return inertia

