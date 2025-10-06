"""module for convulution opearation"""

import numpy as np

class Convulution:
    
    def __init__(self, input_matrix: np.ndarray, kernel: np.ndarray) -> None:
        """__init__ method for Convulation Class"""

        self.input_matrix = input_matrix
        self.kernel = kernel

    def conv_1d(self) -> np.ndarray:
        """convulution method for 1D arrays"""

        output = []
        strides = [self.input_matrix[idx: idx+3] for idx in range(len(self.input_matrix)) if len(self.input_matrix[idx: idx+3]) == len(self.kernel)]
        for array in strides:
            output.append(float(sum([array[i]*self.kernel[i] for i in range(len(self.kernel))])))            
        return output
