# 1816. Truncate Sentence

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        word_list = s.split(' ')
        return ' '.join(word_list[:k])
