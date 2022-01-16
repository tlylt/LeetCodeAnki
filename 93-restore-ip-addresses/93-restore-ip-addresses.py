class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def backtrack(s, startIdx, points):
            if points == 3:
                if self.isValid(s, startIdx, len(s)-1):
                    result.append(s)
                return
            for i in range(startIdx, len(s)):
                if self.isValid(s, startIdx, i):
                    s = s[:i+1] + '.' + s[i+1:]
                    points+=1
                    backtrack(s, i+2, points)
                    points-=1
                    s = s[:i+1]+ s[i+2:]
        backtrack(s, 0, 0)
        return result
    def isValid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:
            return False
        if not 0<= int(s[start:end+1]) <= 255:
            return False
        return True
