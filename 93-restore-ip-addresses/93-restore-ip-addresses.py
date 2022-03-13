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
        path = []
        def backtrack(s, startIdx, points):
            if points == 3 and self.check(s, startIdx, len(s)-1):
                path.append(s[startIdx:])
                result.append("".join(path))
                path.pop()
                return
            if points >= 3:
                return
            for i in range(startIdx, len(s)):
                if self.check(s, startIdx, i):
                    path.append(s[startIdx:i+1] + '.')
                    s = s[:i+1] + '.' + s[i+1:]
                    backtrack(s, i+2, points+1)
                    s = s[:i+1] + s[i+2:]
                    path.pop()
        backtrack(s, 0, 0)
        return result