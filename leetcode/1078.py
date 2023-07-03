# 1078. Occurrences After Bigram

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text_list = text.split(' ')
        res = []
        for i in range(1, len(text_list)):
            if text_list[i] == second and text_list[i-1] == first and i < len(text_list)-1:
                res.append(text_list[i+1])
        return res
