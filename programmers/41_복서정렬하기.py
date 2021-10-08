# level 2
# 단순구현
# sort함수 key사용

# My answer
def solution(weights, head2head):
    n = len(weights)
    data = [[i+1] for i in range(n)]
    # data = [[번호, 승률, 무거운복서를이긴횟수, 자신의몸무게], ...]
    
    for i, NWL in enumerate(head2head):
        # 승률
        total_game = 0
        win_game = 0
        win_heavy = 0
        for j, result in enumerate(NWL):
            if result == 'W' or result == 'L':
                total_game += 1
            if result == 'W':
                win_game += 1
            if result == 'W' and weights[j] > weights[i]:
                win_heavy += 1
        win_rate = win_game / total_game if total_game > 0 else 0
        data[i].extend([win_rate, win_heavy, weights[i]])
    data.sort(reverse = True, key = lambda x : (x[1], x[2], x[3], -x[0]))
    return [x[0] for x in data]
