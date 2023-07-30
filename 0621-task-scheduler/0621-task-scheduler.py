class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_f = 0
        num_max = 0
        ref = {}
        for i in tasks:
            ref[i] = ref.get(i, 0) + 1
        for k, v in ref.items():
            if v ==  max_f:
                num_max += 1
            elif v > max_f:
                max_f = v
                num_max = 1
        return max((n+1) * (max_f - 1) + num_max, len(tasks))