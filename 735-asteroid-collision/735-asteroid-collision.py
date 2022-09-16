class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        s = []
        i = 0
        while i < len(arr):
            if not s:
                s.append(arr[i])
                i += 1
            elif s[-1] > 0 and arr[i] < 0:
                if s[-1] == abs(arr[i]): # same
                    s.pop()
                    i += 1
                else: # diff
                    val = s.pop() # 2
                    if abs(val) > abs(arr[i]):
                        arr[i] = val
                    else:
                        arr[i] = arr[i]
            else:
                s.append(arr[i])
                i += 1
        return s
