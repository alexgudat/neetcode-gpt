class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations == 0:
            return init
        x1:float = float(init)
        for i in range(iterations):
            f_prime = 2*x1
            x2 = x1 - (learning_rate * f_prime)
            x1 = x2
        return round(x1, 5)
