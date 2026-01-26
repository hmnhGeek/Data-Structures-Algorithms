class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance_from(self, target_point):
        x0 = target_point.x
        y0 = target_point.y
        return ((self.x - x0)**2 + (self.y - y0)**2)**0.5


class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def slope(self):
        return -self.a/self.b

    def get_y_from_x(self, x):
        return -(self.c + self.a*x)/self.b


class Solution:
    @staticmethod
    def get_optimum_point_location(line: Line, points):
        eps = 1e-9
        x_low, x_high = -1e6, 1e6
        while x_high - x_low > eps:
            mid1 = (x_low + (x_high - x_low)/3)
            mid2 = (x_high - (x_high - x_low)/3)
            y1 = line.get_y_from_x(mid1)
            y2 = line.get_y_from_x(mid2)
            point1 = Point(mid1, y1)
            point2 = Point(mid2, y2)
            d1 = Solution.get_summed_distance(points, point1)
            d2 = Solution.get_summed_distance(points, point2)
            if d1 < d2:
                x_high = mid2
            else:
                x_low = mid1
        x_avg = (x_low + x_high)/2
        y_avg = line.get_y_from_x(x_avg)
        return Solution.get_summed_distance(points, Point(x_avg, y_avg))

    @staticmethod
    def get_summed_distance(points, line_point):
        _summed = 0
        for point in points:
            _summed += line_point.get_distance_from(point)
        return _summed


print(
    Solution.get_optimum_point_location(
        Line(1, -1, -3),
        [
            Point(-3, -2),
            Point(-1, 0),
            Point(-1, 2),
            Point(1, 2),
            Point(3, 4)
        ]
    )
)
