class Solution:
    def fib(self, n: int) -> int:
        ref = [0, 1]
        if n <= 1:
            return ref[n]
        for i in range(2, n+1):
            temp = ref[0] + ref[1]
            ref[0], ref[1] = ref[1], temp
        return ref[-1]