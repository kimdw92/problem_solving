# level 3
# dp
# 직접 손으로 쓰면서 패턴을 찾아라
# https://gurumee92.tistory.com/164
def solution(N, number):
    s = [ set() for _ in range(9) ]
    for _n in range(1, 9):        
        s[_n].add(int(str(N) * _n))
        for i in range(1, _n):
            left = s[i]
            right = s[_n-i]
            for l in left:
                for r in right:
                    s[_n].add(l + r)
                    s[_n].add(l - r)
                    s[_n].add(l * r)
                    if r != 0:
                        s[_n].add(l // r)
        if number in s[_n]:
            return _n
    return -1
