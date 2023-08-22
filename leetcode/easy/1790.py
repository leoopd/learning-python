# 1790. Check if One String Swap Can Make Strings Equal

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = []
        if s1 == s2:
            return True
        for i in range(len(s1)):
            if len(diffs) > 2:
                return False
            if s1[i] != s2[i]:
                diffs.append([s1[i], i])
        if len(diffs) == 1:
            return False
        res = s1[:diffs[0][1]] + diffs[1][0] + s1[diffs[0][1]+1:diffs[1][1]] + diffs[0][0] + s1[diffs[1][1]+1:]
        print(res)
        if res == s2:
            return True
        return False
