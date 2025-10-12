class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key = lambda x : x[0])
        result = 1
        position = points[0][1]

        for start, end in points[1:]:
            if start > position:
                result += 1
                position = end
            else:
                # update the overlapping end limit
                position = min(position, end)

        return result