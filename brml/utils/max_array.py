#File :  max_array.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-06
#License : BSD 3 clause
#Description :

import numpy as np
from .index_to_assignment import index_to_assignment
from .assignment_to_index import assignment_to_index


def max_array(x, max_over, return_states=False):
    """Maximise a multi-dimensional array over a set of dimensions.

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

        max_state : nd.array[n_left_dims, n_dims_of_x] :
            The row vetcor in max_state[i, :] is the assignments in x. That
            is, x[max_state[i, :]] == max_val[i].

    Raises :
        None

    Notes :
        max_val = max_array(x, max_over)
        max_val, max_state = max_array(x, max_over, return_states=True)

    Examples :
        max_val, max_state = max_array(np.rand(3,4,2), [3, 1])

        We maximise over the 3rd and 1st dimensions, of the 3x4x2 table. This
        means that after maximising, the remaining array is a 4x1 array.
        x[max_state[i, :]] == max_val[i]
    """
    if not isinstance(max_over, np.ndarray):
        max_over = np.array(max_over)

    if return_states is False:
        # works faster if just need max value
        xx = np.array(x)
        for dim in np.sort(max_over)[::-1]:
            xx = np.max(xx, axis=dim)
        max_val = np.squeeze(xx)
        return max_val
    else:
        shape = np.array(x.shape)
        n_dims = x.ndim
        dims = np.arange(n_dims)
        left = np.setdiff1d(dims, max_over)
        dim_left = np.prod(shape[left])
        dim_over = np.prod(shape[max_over])
        concat_left_over = np.concatenate((left, max_over))
        xx = np.transpose(x, concat_left_over)
        s = np.reshape(xx, [dim_left, dim_over])
        max_val, idx = s.max(1), s.argmax(1)

        ranges_left = np.arange(dim_left).reshape(dim_left, -1)
        c = np.concatenate((ranges_left, idx.reshape(dim_left, -1)), axis=1)

        idxs_all = []
        for assignment in c:
            idxs_all.append(assignment_to_index(assignment,
                                                [dim_left, dim_over]))

        ass_all = []
        for idx in idxs_all:
            ass_all.append(index_to_assignment(idx, shape[concat_left_over]))
        max_state = np.array(ass_all)
        q = concat_left_over.argsort()

        if len(left) > 1:
            max_val = max_val.reshape(shape[left])
        return max_val, max_state[:, q]
