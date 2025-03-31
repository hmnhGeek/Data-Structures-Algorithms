# Problem link - https://www.geeksforgeeks.org/optimum-location-point-minimize-total-distance/


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
        """
            The update equation for calculating the nearest point to a set of points in Weiszfeld Algorithm is:

            x_(k+1) = \frac{\sum_{i = 1}^{i = n} \frac{x_i}{d_i} } {\sum_{i = 1}^{i = n}(1/d_i)}
            y_(k+1) = \frac{\sum_{i = 1}^{i = n} \frac{y_i}{d_i} } {\sum_{i = 1}^{i = n}(1/d_i)}

            After getting the updated nearest point, the point must be projected back on the line. Thus, the updated
            reference point for further iterations in the Weiszfeld Algorithm would be the projection of the nearest
            point calculated in this step.
        """
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

    def _populate_distances(self, reference_point: Point, distances: dict):
        """Populates the referenced distances dictionary with distance of each point from reference point."""
        for point in self.points:
            distances.update({point: reference_point.distance_from(point.x, point.y)})

    def _within_threshold(self, prev_reference_point: Point, reference_point: Point) -> bool:
        return abs(reference_point.x - prev_reference_point.x) < self.threshold and abs(reference_point.y - prev_reference_point.y) < self.threshold

    def compute_optimum_point(self) -> Point:
        # The starting point can be any point on the line. Here, x-intercept of the line has been taken. This also
        # proves the fact that if the x-intercept lies far away from the cluster of points, then also this algorithm
        # would yield the correct result.
        x_intercept = self.line.get_x_intercept()
        reference_point = Point(x_intercept, 0)

        # a variable to stop infinite loop in case the result never reaches within threshold.
        iterations = 0

        while iterations < self.max_iterations:
            # populate the distance of each point in the points list from the reference point.
            distances = {}
            self._populate_distances(reference_point, distances)

            # hold the current value of the reference point
            prev_reference_point = reference_point

            # update the reference point using the update mathematical function from Weiszfeld Algorithm.
            reference_point = self._update_reference_point(distances)

            # if the new reference point and old reference point lie within threshold, we've got the correct
            # nearest point on the line to all the points in the list such that the distance is minimized. Return
            # this point.
            if self._within_threshold(prev_reference_point, reference_point):
                return reference_point

            # increment the iteration count.
            iterations += 1

        # if the max allowed iterations are crossed and still the threshold is breached, return whatever reference
        # point has been calculated till now.
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