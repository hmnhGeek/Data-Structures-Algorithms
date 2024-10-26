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

    def __str__(self):
        return f"{self.A}x + {self.B}y + {self.C} = 0"


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

    def _average_position(self) -> Point:
        """Computes the average position of the points."""
        avg_x = sum(point.x for point in self.points) / len(self.points)
        avg_y = sum(point.y for point in self.points) / len(self.points)
        return Point(avg_x, avg_y)

    def _project_point_on_line(self, point: Point) -> Point:
        """Projects a given point onto the line."""
        # Line equation: Ax + By + C = 0
        # Here, A = self.line.A, B = self.line.B, C = self.line.C
        A, B, C = self.line.A, self.line.B, self.line.C

        # Calculate the projection
        x_proj = (B * (B * point.x - A * point.y) - A * C) / (A ** 2 + B ** 2)
        y_proj = (A * (-B * point.x + A * point.y) - B * C) / (A ** 2 + B ** 2)

        return Point(x_proj, y_proj)

    def _update_reference_point(self, distances) -> Point:
        numerator_for_x = 0
        numerator_for_y = 0
        denominator = 0

        for point in distances:
            distance = distances[point]
            if distance != 0:
                numerator_for_x += (point.x/distance)
                numerator_for_y += (point.y/distance)
                denominator += (1/distance)

        nearest_point_to_all_points = Point(numerator_for_x/denominator, numerator_for_y/denominator)
        return self._project_point_on_line(nearest_point_to_all_points)

    def _within_threshold(self, prev_reference_point: Point, reference_point: Point) -> bool:
        return abs(reference_point.x - prev_reference_point.x) < self.threshold and abs(reference_point.y - prev_reference_point.y) < self.threshold

    def compute_optimum_point(self) -> Point:
        x_intercept = self.line.get_x_intercept()
        # Compute average position
        average_point = self._average_position()

        # Project the average point onto the line
        reference_point = self._project_point_on_line(average_point)
        iterations = 0

        while iterations < self.max_iterations:
            distances = {}
            for point in self.points:
                distances.update({point: reference_point.distance_from(point.x, point.y)})
            prev_reference_point = reference_point
            reference_point = self._update_reference_point(distances)
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
#
# Example 4
line = Line(3, 2, 5)
points = [Point(1, -1), Point(2, 3), Point(4, 4), Point(5, -1), Point(3, 2)]
woc = WeiszfeldOptimumPointCalculator(line, points, 1e-6)
result = woc.compute_optimum_point()
print(result, result.calculate_distance_sum_from_points(points))

# Example 5
line = Line(3, 1, -4)
points = [Point(1, 2), Point(4, -2), Point(5, -3), Point(7, -6)]
woc = WeiszfeldOptimumPointCalculator(line, points, 1e-6)
result = woc.compute_optimum_point()
print(line, result, result.calculate_distance_sum_from_points(points))

# Example 6
line = Line(-1, 2, -4)
points = [Point(-2, 1), Point(2, 3), Point(0, 2), Point(-4, 0)]
woc = WeiszfeldOptimumPointCalculator(line, points, 1e-6)
result = woc.compute_optimum_point()
print(line, result, result.calculate_distance_sum_from_points(points))