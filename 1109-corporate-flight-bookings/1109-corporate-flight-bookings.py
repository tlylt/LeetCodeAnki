class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in bookings:
            ans[i[0] - 1] += i[2]
            ans[i[1]] -= i[2]
        ans.pop()
        for i in range(1, n):
            ans[i] += ans[i-1]
        return ans