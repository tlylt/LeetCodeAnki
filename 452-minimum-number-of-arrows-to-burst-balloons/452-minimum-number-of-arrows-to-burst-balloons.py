class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ans = [points[0]]
        for i in range(1, len(points)):
            if ans[-1][1] < points[i][0]:
                ans.append(points[i])
        return len(ans)