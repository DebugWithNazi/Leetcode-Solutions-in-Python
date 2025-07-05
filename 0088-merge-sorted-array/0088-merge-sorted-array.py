class Solution(object):
    def merge(self, nums1, m, nums2, n):
        last = m + n - 1
     

        while m>0 and n >0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                last -= 1
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                last -= 1
                n -= 1
        
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
            

        # left = 0
        # right = 0
        # if not nums1:
        #     return nums2
        # if not nums2:
        #     return nums1
       

        # while left < m:
        #     if nums1[left] >= nums2[right]:
        #         nums1[left],nums2[right]= nums2[right],nums1[left]
        #         nums2.sort()
        #     left += 1
        
        # while right < n:
        #     nums1[left] = nums2[right]
        #     left += 1
        #     right += 1
        
        # return nums1

                
            
            
        