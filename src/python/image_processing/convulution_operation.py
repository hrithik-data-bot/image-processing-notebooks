"""module for convulution opearation"""

import numpy as np

class Convulution1D:
    
    def __init__(self, input_array: np.ndarray, kernel: np.ndarray) -> None:
        """__init__ method for Convulation1D Class"""

        self.input_array = input_array
        self.kernel = kernel

    def conv_1d(self) -> np.ndarray:
        """convulution method for 1D arrays"""

        output = []
        strides = [self.input_matrix[idx: idx+3] for idx in range(len(self.input_matrix)) if len(self.input_matrix[idx: idx+3]) == len(self.kernel)]
        for array in strides:
            output.append(float(sum([array[i]*self.kernel[i] for i in range(len(self.kernel))])))            
        return output


class Convulution2D:

    def __init__(self, input_matrix: np.ndarray, kernel: np.ndarray):
        """__init__ method for Convulation2D Class"""

        self.input_matrix = input_matrix
        self.kernel = kernel

    def conv_2d(self) -> np.ndarray:
        """convulution method for 2D arrays"""

        kernel_shape = self.kernel.shape
        return kernel_shape
    

if __name__ == "__main__":
    np.random.seed(52)
    input_matrix = np.random.randint(low=0, high=10, size=(9,9))
    kernel = np.array([[1,1,1], [0,0,0], [-1,-1,-1]])
    obj = Convulution2D(input_matrix=input_matrix, kernel=kernel)
    print(obj.conv_2d())
