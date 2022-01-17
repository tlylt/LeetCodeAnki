class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == '{':
                st.append('}')
            elif i == '(':
                st.append(')')
            elif i == '[':
                st.append(']')
            elif st == []:
                return False
            elif st[-1] != i:
                return False
            else:
                st.pop()
        return st == []