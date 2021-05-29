# 05 그룹 애너그램
        # 애너그램 판단은 정렬해서 하면 쉬움
        # 정렬된 애너그램을 dafault key로 사용해서 dict에 추가
        # 문자 정렬은 sorted() 가능 : sorted()는 리스트를 리턴하고, sort()은 None을 리턴한다.
        # anagrams.values() -> dict의 값만 리턴
        # ''.join() : str -> list

class Solution:            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
