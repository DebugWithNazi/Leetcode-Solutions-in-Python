class Solution(object):
    def reverseWords(self, s):
        first = 0 
        last = len(s)-1

        words = s.strip().split()
        words.reverse()
        string = ""

        for i in range(len(words)):
            string += words[i]
            if i != len(words)-1:
                string += " "
        return string 
        


        # words = s.strip().split()

        # left = 0 
        # right = len(words)-1

        # while left < right:
        #     words[left],words[right] = words[right],words[left]
        #     left += 1
        #     right -= 1
                    
        # return ' '.join(words)

        

        