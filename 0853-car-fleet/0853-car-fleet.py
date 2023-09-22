class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        prev = 0
        ref = [(position[i], speed[i]) for i in range(len(position))]
        ref.sort(key = lambda i: -i[0])
        for p, s in ref:
            time = (target - p) / s
            if prev < time:
                ans += 1
                prev = time
        return ans