class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                ans += 1
            else:
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
        return len(intervals) - ans