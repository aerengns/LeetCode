# Day 5
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[0])
        arrow_end = points[0][1]
        arrow_count = 1
        for start, end in points[1:]:
            if arrow_end > end:
                arrow_end = end
            if arrow_end < start:
                arrow_end = end
                arrow_count += 1
        return arrow_count