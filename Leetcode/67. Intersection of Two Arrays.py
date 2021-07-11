# 349 두 배열의 교집합

# brute-force 내 풀이, in 이용 60 ms	14.5 MB
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num1 in nums1:
            if num1 not in result and num1 in nums2:
                result.append(num1)
        return result
      
# brute-force 다른 풀이, set() 이용 140 ms	14.4 MB
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)
        return result



# 풀이2 이진검색, 시간 복잡도 O(nlogn) 36 ms	14.4 MB
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            # 이진 검색
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)
        return result
      
# 풀이3 투포인터 44 ms	14.5 MB
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        nums1.sort()
        i = j = 0
        # 투 포인터로 우측으로 이동하며 일치 판별
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return result
