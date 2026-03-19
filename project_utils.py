import numpy as np

def kernel_function(xnodes,kernel_index, exponent, oscillation)
    """
    Function that provides decaying oscillating kernels
    
    Parameters
    ------
    xnodes: numpy.ndarray
        mesh node locations
    
    kernel_index: int
        variable that indexes the kernels

    exponent: float
        decay rate (if negative) or growth rate (if positive)

    oscillation: float
        how oscillatory our function is

    Returns
    -------
    np.ndarray: kernel values
    """
    return (
        np.exp(kernel_index*exponent*xnodes)*
        np.cos(2*np.pi*kernel_index*oscillation*xnodes)
    )