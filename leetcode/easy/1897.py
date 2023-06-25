# 1897. Redistribute Characters to Make All Strings Equal

class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        chars = dict()
        word_count = len(words)
        for element in words:
            for digit in element:
                if digit in chars:
                    chars[digit] += 1
                else:
                    chars[digit] = 1
        for key in chars.keys():
            if chars[key] % word_count != 0:
                return False
        return True
