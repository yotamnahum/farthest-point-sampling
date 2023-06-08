#farthest_point_sampling

import numpy as np

def farthest_point_sampling(arr, n_sample, start_idx=None):
    """Farthest Point Sampling without the need to compute all pairs of distance.

    Parameters
    ----------
    arr : numpy array
        The positional array of shape (n_points, n_dim)
    n_sample : int
        The number of points to sample.
    start_idx : int, optional
        If given, appoint the index of the starting point,
        otherwise randomly select a point as the start point.
        (default: None)

    Returns
    -------
    numpy array of shape (n_sample,)
        The sampled indices.

    Examples
    --------
    >>> import numpy as np
    >>> data = np.random.rand(100, 1024)
    >>> point_idx = farthest_point_sampling(data, 3)
    >>> print(point_idx)
        array([80, 79, 27])

    >>> point_idx = farthest_point_sampling(data, 5, 60)
    >>> print(point_idx)
        array([60, 39, 59, 21, 73])
    """
    n_points, n_dim = arr.shape

    if (start_idx is None) or (start_idx < 0):
        start_idx = np.random.randint(0, n_points)

    sampled_indices = [start_idx]
    min_distances = np.full(n_points, np.inf)
    
    for _ in range(n_sample - 1):
        current_point = arr[sampled_indices[-1]]
        dist_to_current_point = np.linalg.norm(arr - current_point, axis=1)
        min_distances = np.minimum(min_distances, dist_to_current_point)
        farthest_point_idx = np.argmax(min_distances)
        sampled_indices.append(farthest_point_idx)

    return np.array(sampled_indices)
