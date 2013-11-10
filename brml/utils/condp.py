#File :  condp.py
#Author : Mingjun Zhou <mingjun.zhou@gmail.com>
#Version : 0.1
#Date : 2013-11-08
#License : BSD 3 clause
#Description :

import numpy as np
from .ismember import ismember


def condp(pin, dist_vars=None):
    """Make a conditional distribution from an probabilistic table.

    Usage :
        pnew = condp(pin<, evidences=None | [] | [1, 2<,...>])

    Parameters :
        pin : nd.ndarray[n_dim1, n_dim2, ...] :
            A positive matrix probabilistic table.

        dist_vars : nd.ndarray[n_dim1], optional, default : None :
            This specifies which indices form the distribution variables.
            If variables is None or empty([]), returns a normalised table of
            pin.

    Returns :
        pnew : nd.ndarray[new_n_dim1, new_n_dim2, ...] :
            A conditional distribution equal to
            pin(dist_evidences | evidences). 

    Raises :
        None

    """
    pin = pin.astype(float)
    m = pin.flatten(1).max()
    if m > 0:
        pin = pin / m
    else:
        eps = np.finfo(float).eps
        pin = pin + eps  # in case all unnormalised probabilities are zero.

    if not dist_vars:
        pnew = pin / np.sum(pin)
        return pnew
    else:
        shape = np.array(pin.shape)
        all_vars = range(shape.size)
        if not isinstance(dist_vars, np.ndarray):
            dist_vars = np.array(dist_vars)
        evid_vars = np.setdiff1d(all_vars, dist_vars)
        new_vars = np.concatenate((dist_vars, evid_vars))
        newp = np.transpose(pin, new_vars)
        newp = np.reshape(newp, [np.prod(shape[dist_vars]),
                          np.prod(shape[evid_vars])])
        evi_p = np.tile(np.sum(newp, axis=0),
                        (np.size(newp, axis=0), 1))
        newp = newp / evi_p
        pnew = np.reshape(newp, shape[new_vars])

        intersect, idx_ori_in_new, idx = ismember(all_vars, new_vars)
        pnew = np.transpose(pnew, idx_ori_in_new)
        return pnew
