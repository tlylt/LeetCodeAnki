class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x: x[1])
        ans = [intervals[0]]
        count = 1
        for i in range(1, len(intervals)):
            if ans[-1][1] <= intervals[i][0]:
                count += 1
                ans.append(intervals[i])
        return len(intervals) - count