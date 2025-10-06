"""module for convulation opearation"""

import numpy as np

class Convulution:
    
    def __init__(self, input_matrix: np.ndarray, kernel: np.ndarray) -> None:
        """__init__ method for Convulation Class"""

        self.input_matrix = input_matrix
        self.kernel = kernel

    def conv_nd(self) -> np.ndarray:
        """convulution method for 1D and 2D arrays(matrices)"""

        output_array = []
        kernel_length = len(self.kernel)
        strides = [self.input_matrix[idx: idx+3] for idx in range(len(self.input_matrix)) if len(self.input_matrix[idx: idx+3]) == kernel_length]
            
        return strides
    


if __name__ == "__main__":
    
    input = np.array([3,3,2,1,0,0,0,1,3,1])
    kernel = np.array([1, 0, -1])
    obj = Convulution(input_matrix=input, kernel=kernel)
    print(obj.conv_nd())