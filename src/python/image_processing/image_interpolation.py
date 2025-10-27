"""module having nearest neighbour and bilinear interpolation"""

from typing import Tuple
from dataclasses import dataclass

@dataclass
class ImageInterPolation():
    """class for image interpolation 2X2"""

    coordinate_value_11: Tuple[Tuple, float] # ((x1, y1), Q11) 
    coordinate_value_21: Tuple[Tuple, float] # ((x2, y1), Q21)
    coordinate_value_12: Tuple[Tuple, float] # ((x1, y2), Q12)
    coordinate_value_22: Tuple[Tuple, float] # ((x2, y2), Q22)
    

    def nearest_neighbour_interpolation(self, new_coordinate: Tuple) -> float:
        """calculates intensity value using KNN method"""

        rounded_value = (round(value) for value in new_coordinate)
        


    def bilinear_interpolation(self) -> float:
        """calculates intensity value using Bilinear method"""
        pass
