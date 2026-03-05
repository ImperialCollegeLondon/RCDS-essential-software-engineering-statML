def linear_interpolation(x1, y1, x2, y2, x):
    """Perform linear interpolation between two points in 2D Cartesian space.

    Given two points ``(x1, y1)`` and ``(x2, y2)``, this function computes the
    ``y`` value at a specified ``x`` value using linear interpolation. The
    ``x`` value must lie in the closed interval ``[x1, x2]``.

    Parameters
    ----------
    x1 : float
        The x-coordinate of the first point.
    y1 : float
        The y-coordinate of the first point.
    x2 : float
        The x-coordinate of the second point.
    y2 : float
        The y-coordinate of the second point.
    x : float
        The x-value at which to interpolate the y-value.

    Returns
    -------
    float
        The interpolated y-value at ``x``.

    Raises
    ------
    ValueError
        If ``x`` is not between ``x1`` and ``x2`` (inclusive).
    ZeroDivisionError
        If ``x1`` and ``x2`` are equal, causing a vertical line segment.
    """
    if x < x1 or x > x2:
        raise ValueError(f"x value {x} is outside the range [{x1}, {x2}]")

    gradient = (y2 - y1) / (x2 - x1)
    y_intercept = y1 - gradient * x1
    return gradient * x + y_intercept
