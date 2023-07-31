def ft_statistics(*args, **kwargs):
    """
    Compute various statistics for the given numeric arguments.

    Args:
        *args: Variable-length argument list containing numeric values.
        **kwargs: Keyword arguments specifying the statistics to compute.
            Available keyword arguments:
                'mean': Compute the mean (average) of the numeric values.
                'median': Compute the median of the numeric values.
                'quartile': Compute the 25th and 75th quartiles of
                the numeric values.
                'std': Compute the standard deviation of the numeric values.
                'var': Compute the variance of the numeric values.

    Returns:
        None: Prints the computed statistics.

    Example:
        ft_statistics(1, 2, 3, 4, mean='mean',
        median='median', quartile='quartile', std='std', var='var')
    """
    if len(args) == 0:
        print("Please provide arguments as numbers")
        return

    for key, value in kwargs.items():
        if "mean" == value:
            mean = sum(args) / len(args)
            print(f"Mean: {mean}")

        elif "median" == value:
            sorted_args = sorted(args)
            n = len(sorted_args)
            mid = n // 2

            if n % 2 == 0:
                median = (sorted_args[mid - 1] + sorted_args[mid]) / 2
            else:
                median = sorted_args[mid]
            print(f"Median: {median}")

        elif "quartile" == value:
            sorted_args = sorted(args)
            n = len(sorted_args)
            mid = n // 2

            if n % 2 == 0:
                lower_half = sorted_args[:mid]
                upper_half = sorted_args[mid:]
            else:
                lower_half = sorted_args[:mid]
                upper_half = sorted_args[mid + 1:]

            q1 = sum(lower_half) / len(lower_half)
            q3 = sum(upper_half) / len(upper_half)
            print(f"25th Quartile: {q1}")
            print(f"75th Quartile: {q3}")

        elif "std" == value:
            mean = sum(args) / len(args)
            squared_diff = [(x - mean) ** 2 for x in args]
            std_dev = (sum(squared_diff) / len(args)) ** 0.5
            print(f"Standard Deviation: {std_dev}")

        elif "var" == value:
            mean = sum(args) / len(args)
            squared_diff = [(x - mean) ** 2 for x in args]
            variance = sum(squared_diff) / len(args)
            print(f"Variance: {variance}")

        else:
            print(f"Unknown statistic '{value}' for '{key}'")
