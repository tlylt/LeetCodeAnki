class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
        return ans
        