# 4. Median of Two Sorted Arrays

# My answer 시간복잡도: SORT의 시간복잡도(O(NlogN)) 로 인해 총 O((m+n)log(m+n))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        merged = nums1 + nums2
        merged.sort()
        return merged[(m+n)//2] if (m+n) % 2 > 0 else (merged[(m+n)//2] + merged[(m+n)//2-1]) / 2
