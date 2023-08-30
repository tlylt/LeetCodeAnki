class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        ptr1, ptr2 = 0, 0
        last_char = None

            # last_char = "e"
            # "aalex"
            #      ^ 
            # "aaaleex"  
            #        ^

        while ptr1 < len(name) and ptr2 < len(typed):
            if name[ptr1] == typed[ptr2]:
                last_char = name[ptr1]
                ptr1 += 1
                ptr2 += 1
            elif last_char and typed[ptr2] == last_char:
                while ptr2 < len(typed) and typed[ptr2] == last_char:
                    ptr2 += 1
            else:
                return False
        while ptr2 < len(typed) and typed[ptr2] == last_char:
            ptr2 += 1
        if ptr1 != len(name) or ptr2 != len(typed):
            return False
        return True