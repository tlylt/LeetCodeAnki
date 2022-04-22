class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], intervals[i][1])]
            else:
                ans.append(intervals[i])
        return ans
            