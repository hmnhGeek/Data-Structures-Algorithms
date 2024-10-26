from typing import List


class Line:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def get_x_intercept(self):
        return -self.C/self.A

    def get_slope(self):
        return -self.A/self.B

    def get_y_intercept(self):
        return -self.C/self.B

    def get_x_from_y(self, y):
        return -(self.C + (self.B * y))/self.A

    def get_y_from_x(self, x):
        return -(self.C + (self.A * x))/self.B


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from(self, x0, y0):
        return ((self.x - x0)**2 + (self.y - y0)**2)**0.5

    def __str__(self):
        return f"({self.x}, {self.y})"

    def calculate_distance_sum_from_points(self, points):
        distance_sum = 0
        for point in points:
            distance_sum += self.distance_from(point.x, point.y)
        return distance_sum


class WeiszfeldOptimumPointCalculator:
    def __init__(self, line: Line, points: List[Point], convergence_threshold: float):
        self.line = line
        self.points = points
        self.threshold = convergence_threshold
        self.max_iterations = 1000

    def _update_reference_point(self, reference_point: Point, distances: List[float]) -> Point:
        numerator = 0
        denominator = 0
        for idx in range(len(self.points)):
            point = self.points[idx]
            if distances[idx] != 0:
                numerator += (point.x/distances[idx])
                denominator += (1/distances[idx])

        if denominator == 0:
            return reference_point

        next_x_of_reference_point = numerator/denominator
        next_y_of_reference_point = self.line.get_y_from_x(next_x_of_reference_point)
        return Point(next_x_of_reference_point, next_y_of_reference_point)

    def _within_threshold(self, prev_reference_point: Point, reference_point: Point) -> bool:
        return abs(reference_point.x - prev_reference_point.x) < self.threshold and abs(reference_point.y - prev_reference_point.y) < self.threshold

    def compute_optimum_point(self) -> Point:
        x_intercept = self.line.get_x_intercept()
        reference_point = Point(x_intercept, 0)
        iterations = 0

        while iterations < self.max_iterations:
            distances = []
            for point in self.points:
                distances.append(reference_point.distance_from(point.x, point.y))

            prev_reference_point = reference_point
            reference_point = self._update_reference_point(reference_point, distances)
            if self._within_threshold(prev_reference_point, reference_point):
                return reference_point
            iterations += 1
        return reference_point


# Example
line = Line(1, -1, -3)
points = [Point(-3, -2), Point(-1, 0), Point(-1, 2), Point(1, 2), Point(3, 4)]
woc = WeiszfeldOptimumPointCalculator(line, points, 0.0000001)
result = woc.compute_optimum_point()
print(result, result.calculate_distance_sum_from_points(points))

# Example 2
line = Line(1, 1, -3)
points = [Point(1, 2), Point(2, 1), Point(4, 0)]
woc = WeiszfeldOptimumPointCalculator(line, points, 0.01)
result = woc.compute_optimum_point()
print(result, result.calculate_distance_sum_from_points(points))

# Example 3
line = Line(1, -1, 0)
points = [Point(-1, 1), Point(1, -1)]
woc = WeiszfeldOptimumPointCalculator(line, points, 0.01)
result = woc.compute_optimum_point()
print(result, result.calculate_distance_sum_from_points(points))