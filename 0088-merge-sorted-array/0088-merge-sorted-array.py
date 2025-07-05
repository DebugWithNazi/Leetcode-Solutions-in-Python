class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left = 0
        right = 0
        if not nums1:
            return nums2
        if not nums2:
            return nums1
       

        while left < m:
            if nums1[left] >= nums2[right]:
                nums1[left],nums2[right]= nums2[right],nums1[left]
                nums2.sort()
            left += 1
        
        while right < n:
            nums1[left] = nums2[right]
            left += 1
            right += 1
        
        return nums1

                
            
            
        