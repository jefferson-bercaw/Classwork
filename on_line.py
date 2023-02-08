def on_line(point_1, point_2, x):
    m = get_slope(point_1, point_2)
    y = m * (x - point_1[0]) + point_1[1]
    return y


def get_slope(point_1, point_2):
    m = (point_2[1] - point_1[1]) / (point_2[0] - point_1[0])
    return m


if __name__ == 'main':
    on_line()
