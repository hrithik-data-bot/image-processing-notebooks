"""module to implement gaussian filter"""

import math

def gaussian_formula(x: int, y: int, sigma: float = 1) -> float:
    """gaussian formula function"""

    coeff_1 = 1/(2*math.pi*(sigma**2))
    coeff_2 = math.exp(-(x**2 + y**2)/(2*sigma**2))
    gaussian = coeff_1*coeff_2
    return gaussian

