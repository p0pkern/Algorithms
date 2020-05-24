def Euclid(num_1, num_2):
    """
    Finds the least common factor of the values entered.
    :param num_1: First value
    :param num_2: Last value
    :return: Greatest common factor
    """
    if num_1 == 0:
        return num_2
    elif num_2 == 0:
        return num_1
    if num_1 % num_2 == 0:
        return num_2
    else:
        num_3 = num_1 % num_2
        return Euclid(num_2, num_3)

