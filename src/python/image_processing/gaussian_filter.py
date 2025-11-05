"""module to implement gaussian filter"""

import math
import numpy as np

def gaussian_formula(x: int, y: int, sigma: float = 1) -> float:
    """gaussian formula function"""

    coeff_1 = 1/(2*math.pi*(sigma**2))
    coeff_2 = math.exp(-(x**2 + y**2)/(2*sigma**2))
    gaussian = coeff_1*coeff_2
    return round(gaussian, 4)

if __name__ == "__main__":
    my_values = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0),
                 (1, 0), (-1, 1), (0, 1), (1, 1)]
    gaussian_values = [gaussian_formula(pixel_i_j[0], pixel_i_j[1]) for pixel_i_j in my_values]
    normalised = [round(value/sum(gaussian_values), 4) for value in gaussian_values]
    normalised = np.array(normalised).reshape(3,3)
    image_patch = np.array([[10, 20, 30], [20, 40, 20], [30, 20, 10]])
    new_value = round(sum((normalised*image_patch).reshape(-1,1).flatten()))
    print(new_value)
    