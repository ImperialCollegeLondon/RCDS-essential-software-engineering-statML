def linear_interpolation(x1, y1, x2, y2, x):
    """
    Perform linear interpolation to find the y value at a specified x value between two points (x1, y1) and (x2, y2).

    Parameters:
    x1 (float): x-coordinate of the first point.
    y1 (float): y-coordinate of the first point.
    x2 (float): x-coordinate of the second point.
    y2 (float): y-coordinate of the second point.
    x (float): x-coordinate at which to interpolate.

    Returns:
    float: Interpolated y-coordinate at the specified x value.

    Raises:
    ValueError: If the specified x value is outside the range [x1, x2].
    """
    if x < x1 or x > x2:
        raise ValueError(f'x value {x} is outside the range [{x1}, {x2}]')
    

    #hhgjjhg

    gradient = (y2 - y1) / (x2 - x1)
    y_intercept = y1 - gradient * x1
    return gradient * x + y_intercept
