class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack [73, 74, 75] decreasing towards the top
        # compare stack top vs curr
        # if curr is bigger than top, pop top and update
        stack = [0]
        ans = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans
        
        