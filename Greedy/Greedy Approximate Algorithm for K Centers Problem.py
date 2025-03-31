from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    @staticmethod
    def get_euclidean_distance(p: Point, q: Point):
        return ((q.x - p.x)**2 + (q.y - p.y)**2)**0.5

    @staticmethod
    def k_centers_problem(p, k: int):
        points = [Point(x, y) for x, y in p]
        centers = [points[0],]

        for _ in range(k - 1):
            farthest_point = None
            max_distance = -1
            for point in points:
                if point not in centers:
                    min_distance = min(Solution.get_euclidean_distance(point, center) for center in centers)
                    if min_distance > max_distance:
                        max_distance = min_distance
                        farthest_point = point
            centers.append(farthest_point)

        return [(p.x, p.y) for p in centers]


print(Solution.k_centers_problem([(0, 0), (2, 2), (3, 3), (5, 5), (10, 10), (12, 12)], 2))