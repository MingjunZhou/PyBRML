#File :  max_array.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-06
#License : BSD 3 clause
#Description :

import numpy as np
from .set_diff import set_diff
from .index_to_assignment import index_to_assignment
from .assignment_to_index import assignment_to_index


def max_array(x, max_over, return_states=False):
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

        return_states : boolean, optional, default : False, :
            If return_states is false, just return max_val, otherwise return
            (max_val, max_state).

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
    if return_states is False:
        # works faster if just need max value
        xx = np.array(x)
        for dim in max_over:
            xx = np.max(xx, axis=dim)
        max_val = np.squeeze(xx)
        return max_val
    else:
        if not isinstance(max_over, np.ndarray):
            max_over = np.array(max_over)
        shape = x.shape
        n_dims = x.ndim
        dims = np.arange(n_dims)
        left = dims.differences(max_over)
        dim_left = np.prod(shape[left])
        dim_over = np.prod(shape[max_over])
        xx = np.transpose(x, [left, max_over])
        s = np.reshape(xx, [dim_left, dim_over])
        max_val, idx = s.max(1), s.argmax(1)
        c = np.concatenate(np.arange(dim_left).transpose(), idx.transpose())
        assignment = assignment_to_index(c, [dim_left, dim_over])
        concat_left_over = np.concatenate((left, max_over))
        max_state = index_to_assignment(assignment, dims[concat_left_over])
        p, q = concat_left_over.sort(), concat_left_over.argsort()
        return max_val, max_state[:, q]
