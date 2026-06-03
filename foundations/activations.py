import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        outputArray: NDArray[np.float64] =[]
        for input in z:
            output:np.float64 = np.round((1/(1+np.exp(-input))), 5)
            outputArray.append(output)
        return np.array(outputArray)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        outputArray:NDArray[np.float64] = []
        for input in z:
            output:np.float64 = float(max(0, input))
            outputArray.append(output)
        return np.array(outputArray)