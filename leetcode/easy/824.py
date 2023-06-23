# 824. Goat Latin

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence_list = sentence.split(' ')
        res = []
        counter = 1
        vowels = ['a','e','i','o','u']
        for word in sentence_list:
            if word[0].lower() in vowels:
                word += 'ma'
            else:
                tmp1 = word[0]
                tmp2 = word[1:]
                word = tmp2 + tmp1 + 'ma'
            word += counter * 'a'
            res.append(word)
            counter += 1
        return ' '.join(res)
