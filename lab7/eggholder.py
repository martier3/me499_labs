import numpy as np
from scipy import optimize


def eggholder(x, y):
    """
    Takes in either a scalar x and y, or a 1-D numpy array for both x and y.
    """
    if (isinstance(x, np.ndarray) and not isinstance(y, np.ndarray)) or (
            isinstance(y, np.ndarray) and not isinstance(x, np.ndarray)):
        pass

    result = -(y + 47) * np.sin(np.sqrt(np.abs(x / 2 + (y + 47)))) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))
    if isinstance(x, np.ndarray):
        outside = (np.abs(x) > 512) | (np.abs(y) > 512)
        result[outside] = 2000
        return result
    else:
        return 2000 if (abs(x) > 512 or abs(y) > 512) else result

def minimize_eggholder(guess=[0,0], max_calls=100):
    eggholder_minimized = optimize.fmin(func=eggholder(guess), x0=guess, maxfun=max_calls)
    return eggholder_minimized


print(minimize_eggholder([5, 5], 100))