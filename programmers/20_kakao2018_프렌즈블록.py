# 구현

# My answer
def check_two_by_two(m, n, board):
    check = False # 사라질 블록이 없다
    check_list = []
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j].isalpha():
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    check = True
                    check_list.append([i, j])
                    
    return check, check_list
    

def solution(m, n, board):
    # 문자열을 하나씩 쪼개서 리스트로 변환
    list_board = [list(x) for x in board]
    
    answer = 0
    
    dx = [0, 1, 0, 1]
    dy = [0, 0, 1, 1]
    
    while True:
        # 2x2 형태가 있는가?
        check, xys = check_two_by_two(m, n, list_board)
        # 없으면 루프 종료
        if check == False:
            return answer
        
        # 있으면 해당 위치를 0으로 바꾼다
        for x, y in xys:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if list_board[nx][ny].isalpha():
                    answer += 1
                    list_board[nx][ny] = '0'
            
        # 위에 있는 블록을 떨어트린다
        for j in range(n):
            for i in range(m-1, 1, -1): # row index는 m-1에서 2까지 역순으로 탐색
                # 빈공간을 발견하면
                if list_board[i][j] == '0':
                    find_alpha = i - 2
                    # 프렌즈를 찾아서 떨어트리기
                    while find_alpha >= 0:
                        if list_board[find_alpha][j].isalpha():
                            list_board[i][j], list_board[find_alpha][j] = \
                            list_board[find_alpha][j], '0'   
                            break
                        find_alpha -= 1   

    return answer
  
  
  # 다른 풀이
  def solution(m, n, board):
    # 문자열을 하나씩 쪼개서 리스트로 변환
    board = [list(x) for x in board]
    
    matched = True    
    while matched:
        # 1) 일치 여부 판별
        matched = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] !=  '#':
                    matched.append([i, j])
                    
        # 2) 일치한 위치 삭제
        for i, j in matched:
            board[i][j] = board[i+1][j] = board[i][j+1] = board[i+1][j+1] = '#'
            
        # 3) 빈공간 블럭 처리
        for _ in range(m):
            for i in range(m-1):
                for j in range(n):
                    if board[i + 1][j] == '#':
                        board[i + 1][j], board[i][j] = board[i][j], '#'
                        
    return sum(x.count('#') for x in board)
