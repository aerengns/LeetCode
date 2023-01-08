# Day 8
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return n

        max_points = 0
        for i in range(n):
            point1 = points[i]
            same_point_count = 1
            same_slope_count = 0
            slopes = {}
            for j in range(i+1, n):
                point2 = points[j]
                # Check if the points have the same coordinates
                if point1[0] == point2[0] and point1[1] == point2[1]:
                    same_point_count += 1
                    continue
                # Calculate the slope of the line defined by the two points
                slope = None
                if point1[0] == point2[0]:
                    slope = float('inf')
                else:
                    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
                # Check if we have seen this slope before
                if slope in slopes:
                    slopes[slope] += 1
                else:
                    slopes[slope] = 1
            slopes['default'] = 0
            # Find the maximum number of points with the same slope
            same_slope_count = max(slopes.values())
            # Add the number of points with the same coordinates
            same_slope_count += same_point_count
            # Update the maximum number of points on a line
            max_points = max(max_points, same_slope_count)
        return max_points
