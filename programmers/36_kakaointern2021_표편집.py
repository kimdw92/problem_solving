# level 3
# 처음에 list로 풀려했지만 삭제 구현에서 O(n2)이 걸려 효율성테스트 통과못함

# 연결리스트는 삽입, 삭제 O(n)으로 구현 가능
# dict로 연결리스트 구현하기 !!
# 참고: https://ckd2806.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91
def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    OX = ["O"] * n
    stack = []

    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c[2:])):
                k = linked_list[k][1]
        elif c[0] == 'U':
            for _ in range(int(c[2:])):
                k = linked_list[k][0]
        elif c[0] == 'C':
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            OX[k] = 'X'
            if next == n: # k가 마지막 노드이면
                k = linked_list[k][0] # 위로 이동
            else:
                k = linked_list[k][1]
            
            if prev == -1:
                linked_list[next][0] = prev
            elif next == n:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev
        
        elif c[0] == 'Z':
            prev, next, now = stack.pop()
            OX[now] = 'O'
            if prev == -1:
                linked_list[next][0] = now
            elif next == n:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now
    return ''.join(OX)
