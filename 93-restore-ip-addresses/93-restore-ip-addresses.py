class Solution:
    def check(self, s, start, end): # both inclusive
        if start > end:
            return False
        if s[start] == '0' and start != end:
            return False
        if not (0 <= int(s[start:end+1]) <= 255):
            return False
        return True
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def backtrack(s, points, startIdx):
            if points > 3:
                return
            if points == 3 and self.check(s, startIdx, len(s)-1):
                result.append(s)
                return
            for i in range(startIdx, len(s)):
                if self.check(s, startIdx, i):
                    s = s[:i+1] + '.' + s[i+1:]
                    backtrack(s, points+1, i+2)
                    s = s[:i+1] + s[i+2:]
        backtrack(s, 0, 0)
        return result