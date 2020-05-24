def rec_sum(start, total=0):
    """
    Sums the values from start to 1 in increments of 1
    :param start: The value to sum
    :param total: The total of start and the subsequent values
    :return: total of summed values
    """
    num = start
    if start == 1:
        return total + 1
    else:
        return rec_sum((start - 1), (total + num))
