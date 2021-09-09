# My answer
# dict 이용
from itertools import combinations
import collections

def solution(orders, course):
    count = collections.defaultdict(int)
    
    for order in orders:
        m = len(order)
        for comb in course:
            if comb > m:
                break
            for c in list(combinations(list(order), comb)): 
                count[''.join(sorted(c))] += 1
                
    menu_cnt = collections.defaultdict(int)
    menu_list = collections.defaultdict(list)
    print(count)
    for key, value in count.items():
        many = len(key) # 메뉴 구성의 수
        if value >= 2 and value > menu_cnt[many]:
            menu_cnt[many] = value
            menu_list[many] = [key]
        elif value >= 2 and value == menu_cnt[many]:
            menu_list[many].append(key)
    print(menu_list)
    result = []
    for key, value in menu_list.items():
        result.extend(value)
    return sorted(result)
  
# Counter를 이용한 간결한 풀이
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]
