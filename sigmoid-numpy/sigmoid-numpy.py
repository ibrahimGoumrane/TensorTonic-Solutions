import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function that works for scalars, lists, or NumPy arrays.
    """
    # Convert input to NumPy array
    x = np.array(x)
    return 1 / (1 + np.exp(-x))