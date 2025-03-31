# Problem link - https://www.geeksforgeeks.org/greedy-approximate-algorithm-for-k-centers-problem/
# Solution - https://www.youtube.com/watch?v=dpYZojRuJEI


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    @staticmethod
    def get_euclidean_distance(p: Point, q: Point):
        return ((q.x - p.x) ** 2 + (q.y - p.y) ** 2) ** 0.5

    @staticmethod
    def k_centers_problem(weights, k: int):
        n = len(weights)  # Number of cities

        # Step 1: Pick the first center arbitrarily (let’s pick city 0)
        centers = [0]

        # Step 2: Select (k-1) additional centers
        for _ in range(k - 1):
            farthest_city = None
            max_distance = -1

            # Find the city that is farthest from any of the current centers
            for city in range(n):
                if city not in centers:  # Ensure it's not already a center
                    # Compute the minimum distance to any selected center
                    min_distance = min(weights[city][c] for c in centers)

                    # Update if we find a farther city
                    if min_distance > max_distance:
                        max_distance = min_distance
                        farthest_city = city

            # Add the farthest city to the centers
            centers.append(farthest_city)

        return centers


print(Solution.k_centers_problem([[0, 4, 8, 5],
                                  [4, 0, 10, 7],
                                  [8, 10, 0, 9],
                                  [5, 7, 9, 0]], 2))
