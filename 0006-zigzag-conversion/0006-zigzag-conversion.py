class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or len(s) < numRows:
            return s
        rows = [''] * numRows
        flag = False
        index = 0
        for i in range(len(s)):
            rows[index] += s[i]

            if index == 0 or index == numRows-1:
                flag = not flag
            
            if flag:
                index += 1
            else:
                index -= 1
        result = ''.join(rows)
        return result


  
            
            

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
      

        