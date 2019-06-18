import math

def calc_min_degree(min, sec):
    """

    :param min:
    :param sec:
    :return:
    """
    return (min * math.pi / 30.0 + sec * math.pi / 1800.0)


def calc_hour_degree(hour, min, sec):
    """

    :param hour:
    :param min:
    :param sec:
    :return:
    """
    return (hour * math.pi / 6.0 + calc_min_degree(min, sec))

def calc_degree_between_hm(hour, min, sec):
    """

    :param hour:
    :param min:
    :param sec:
    :return:
    """
    degree_of_hour = calc_hour_degree(hour, min, sec)
    degree_of_min = calc_min_degree(min, sec)
    gap = math.abs(degree_of_min - degree_of_hour)
    if gap > math.pi:
        gap = 2*math.pi - gap
    return gap

if __name__ == "main":
    pass

