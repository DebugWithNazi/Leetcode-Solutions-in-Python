class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start filling nums1 from the end
            i = m - 1        # pointer for nums1's real elements
            j = n - 1        # pointer for nums2
            k = m + n - 1    # pointer for final position in nums1

            # Merge from back to front
            while i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
                k -= 1

            # If any elements left in nums2, copy them
            while j >= 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1








        