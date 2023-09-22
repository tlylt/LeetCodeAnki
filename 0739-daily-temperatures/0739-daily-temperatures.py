class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        ans = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                    ans[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return ans
                
                