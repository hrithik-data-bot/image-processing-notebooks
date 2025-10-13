"""module for convulution opearation"""

from typing import Tuple
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

    def _output_shape(self) -> Tuple:
        """method calculates shape of output matrix 
           Note:- No Padding and 1 Stride
        """
        output_w = (self.input_matrix.shape[0]-self.kernel.shape[0])+1  
        output_h = (self.input_matrix.shape[1]-self.kernel.shape[1])+1
        return output_w, output_h

    def _dot_product(self, matrix_1: np.ndarray, matrix_2: np.ndarray) -> float:
        """find dot product 2 same shaped matrices"""

        dot_product = matrix_1 * matrix_2
        return dot_product

    def conv_2d(self) -> np.ndarray:
        """convulution method for 2D arrays"""

        sub_matrices = []
        kernel_shape = self.kernel.shape
        for col in range(self.input_matrix.shape[1]):
            current_col_until = col + 3
            for row in range(input_matrix.shape[0]):
                current_sub_matrix = self.input_matrix[row: row+kernel_shape[0], col: current_col_until]
                if current_sub_matrix.shape == kernel_shape:
                    sub_matrices.append(current_sub_matrix)
        interim_matrix = np.array(sub_matrices)
        final_array = np.array([sum(self._dot_product(self.kernel, matrix).flatten()) for matrix in interim_matrix]).reshape(self._output_shape())
        return final_array
