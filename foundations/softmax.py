import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        maxi = max(z)
        denominator:np.float64 = 0
        array:NDArray[np.float64] = []
        for input in z:
            value = np.round(np.exp(input-maxi), 4)
            array.append(value)
            denominator += value
        output_array:NDArray[np.float64]=[]
        for val in array:
            result = np.round(val/denominator, 4)
            output_array.append(result)
        return np.array(output_array)
