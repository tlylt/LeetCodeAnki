class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if ans[-1][1] > intervals[i][0]:
                continue
            else:
                ans.append(intervals[i])
        return len(intervals) - len(ans)
            