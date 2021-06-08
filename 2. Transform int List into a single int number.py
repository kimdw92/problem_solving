a = [1, 2, 3, 4, 5]

# 1: 문자형으로 바꿧다가 다시 숫자형으로, 가독성이 떨어짐
answer = ''.join(str(e) for e in a) # '12345'

# 2: 임시변수 e 없이 가능
answer = ''.join(map(str, a)) # '12345'

# 3: 숫자형으로 바로 변환
answer = functools.reduce(lambda x, y: 10 * x + y, a, 0)
