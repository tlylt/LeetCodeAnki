class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        if not s:
            return ""
        for i in s:
            if st and st[-1] == i:
                st.pop()
            else:
                st.append(i)
        return "".join(st)