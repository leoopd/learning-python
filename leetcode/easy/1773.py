# 1773. Count Items Matching a Rule

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ctr = 0
        for item in items:
            if ruleKey == "type":
                if item[0] == ruleValue:
                    ctr += 1
            elif ruleKey == "color":
                if item[1] == ruleValue:
                    ctr += 1
            elif ruleKey == "name":
                if item[2] == ruleValue:
                    ctr += 1
        return ctr
