# 완전탐색
# level 2

def solution(places):
    answer = []
    for place in places:
        flag = 1
        for row in range(5):
            for col in range(5):
                if place[row][col] == 'P':
                    if ((row < 4 and place[row+1][col] == 'P')
                    or (col < 4 and place[row][col+1] == 'P')
                    or (col < 3 and place[row][col+2] == 'P' and place[row][col+1] != 'X')
                    or (row < 4 and col > 0 and place[row+1][col-1] == 'P' and (place[row+1][col] != 'X' or place[row][col-1] != 'X'))
                    or (row < 4 and col < 4 and place[row+1][col+1] == 'P' and (place[row+1][col] != 'X' or place[row][col+1] != 'X'))
                    or (row < 3 and place[row+2][col] == 'P' and place[row+1][col] != 'X')):
                        flag = 0
                        break
            if flag == 0:
                break
        answer.append(flag)
    return answer
