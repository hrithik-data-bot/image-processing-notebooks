"""module for convulation opearation"""

import numpy as np

class Convulation:
    
    def __init__(self, input_matrix: np.ndarray, kernel: np.ndarray) -> None:
        """__init__ method for Convulation Class"""

        self.input_matrix = input_matrix
        self.kernel = kernel

    def conv_nd(self) -> np.ndarray:
        """convulation method for 1D and 2D arrays(matrices)"""

        
    


if __name__ == "__main__":
    
    input = np.array([[3,3,2,1,0,0,0,1,3,1]])
    kernel = np.array([1, 0, -1])
