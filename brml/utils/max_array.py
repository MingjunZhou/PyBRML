#File :  max_array.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-06
#License : BSD 3 clause
#Description :

import numpy as np
import .set_diff import set_diff

def max_array(x, max_over):
    """Maximise a multi-dimensional array over a set of dimensions.

    Usage :
        max_val, max_state = max_array(x, max_over)

    Parameters :
        x : nd.array[n_dim1, n_dim2, ...] :
            The multi-dimensional array to be maximised. After the
            maximisation, the origin array is not changed, instead we get a
            new array.

        max_over : sequence[n_over, ] or nd.ndarray[n_over, ] :
            The dimensions to maximise the array over.

    Returns :
        max_val : nd.array[n_remaining_dim1, ...] :
            The remaining array.

        max_state : nd.array[n_over, ] :
            When the variables in max_over equal to the states in max_state,
            we get the maximised array.

    Examples :
        max_val, max_state = max_array(np.rand(3,4,2), [3, 1])

        We maximise over the 3rd and 1st dimensions, of the 3x4x2 table. This
        means that after maximising, the remaining array is a 4x1 array.
        max_val(i) contains the maximum value of the array when the second
        dimension is in state i.

    Raises :
        None

    """
    shape = x.shape
    n_dims = x.ndim
    dims = range(n_dims)
    left = set_diff(dims, max_over)
    dim_left = np.prod(shape[left])
    dim_over = np.prod(shape[max_over])
    
    for dim in max_over:
        max_val = np.amax(x, dim)

    return max_val, 
    
