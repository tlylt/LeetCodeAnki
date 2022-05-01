class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= ans[-1][1]:
                ans.append(intervals[i])
        return len(intervals) - len(ans)