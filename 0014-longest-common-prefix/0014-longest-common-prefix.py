class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        first = strs[0]
        last = strs[len(strs)-1]
        i,j = 0,0
        final = ""

        while i < len(first) and j < len(last):
              if first[i] == last[j]:
                 final += first[i]
              else:
                return final
              i += 1
              j += 1

        return final if final else ""

                 



        