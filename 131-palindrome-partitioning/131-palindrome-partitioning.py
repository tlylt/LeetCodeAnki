class Solution:
    def check(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        def backtrack(s, startIdx):
            if startIdx >= len(s):
                result.append(path[:])
                return
            for i in range(startIdx, len(s)):
                if self.check(s[startIdx:i+1]):
                    path.append(s[startIdx:i+1])
                    backtrack(s, i+1)
                    path.pop()
        backtrack(s, 0)
        return result