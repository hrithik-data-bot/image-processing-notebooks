"""module having nearest neighbour and bilinear interpolation"""

from typing import Tuple, Dict
from dataclasses import dataclass, asdict
from matplotlib import pyplot as plt


@dataclass
class ImageInterPolation():
    """class for image interpolation 2X2"""

    coordinate_value_11: Dict[Tuple, float] # {(x1, y1): Q11} 
    coordinate_value_21: Dict[Tuple, float] # {(x2, y1): Q21}
    coordinate_value_12: Dict[Tuple, float] # {(x1, y2): Q12}
    coordinate_value_22: Dict[Tuple, float] # {(x2, y2): Q22}


    def return_frame(self) -> None:
        """return the frame of coordinates and new value"""
        pass

    

    def nearest_neighbour_interpolation(self, new_coordinate: Tuple) -> float:
        """calculates intensity value using KNN method"""

        rounded_value = tuple(round(value) for value in new_coordinate)
        return [value[1] for value in asdict(self).values() if value[0]==rounded_value][0]
        


    def bilinear_interpolation(self) -> float:
        """calculates intensity value using Bilinear method"""
        pass


if __name__ == "__main__":
    obj = ImageInterPolation(coordinate_value_11=((0,0), 11), coordinate_value_21=((2,0), 4),
                             coordinate_value_12=((2,2), 45), coordinate_value_22=((0,2), 27))
    print(obj.nearest_neighbour_interpolation(new_coordinate=(0.5,1.8)))

    