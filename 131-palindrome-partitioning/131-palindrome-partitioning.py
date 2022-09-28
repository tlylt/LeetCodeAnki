class Solution:
    def check(self, s):
        return s == s[::-1]
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        def backtrack(s, idx):
            if idx >= len(s):
                result.append(path[:])
                return
            for i in range(idx, len(s)):
                if self.check(s[idx:i+1]):
                    path.append(s[idx:i+1])
                    backtrack(s, i+1)
                    path.pop()
        backtrack(s, 0)
        return result