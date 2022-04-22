class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        non_overlap = 1
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                non_overlap += 1
                end = intervals[i][1]
        return len(intervals) - non_overlap