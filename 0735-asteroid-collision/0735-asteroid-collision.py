class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        stack = []
        pt = 0
        while pt < len(arr):
            curr = arr[pt]
            if not stack:
                stack.append(curr)
                pt += 1
            else:
                if stack[-1] > 0 and curr < 0:
                    if stack[-1] + curr == 0: # same size
                        stack.pop()
                        pt += 1
                    else:
                        bigger = stack[-1] if stack[-1] > abs(curr) else curr
                        if bigger != stack[-1]:
                            stack.pop()
                        else:
                            pt += 1
                else:
                    stack.append(curr)
                    pt += 1
        return stack