class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        carry = 0
        a = a[::-1]
        b = b[::-1]
        for i in range(max(len(a), len(b))):
            val_a = int(a[i]) if i < len(a) else 0
            val_b = int(b[i]) if i < len(b) else 0
            total = val_a + val_b + carry
            ans.append(str(total % 2))
            carry = total // 2
        if carry == 1:
            ans.append("1")
        return "".join(ans[::-1])