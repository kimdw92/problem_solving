# 3687 성냥개비
# 네이버 공채 문제와 유사한 DP 유형
# 50%에서 오답... 뭐가 틀렸는지 모르겠다?? 테스트 케이스도 안나오고 어떻게 디버그 하라는건지

# 최소값 -> 1과 7로만 이루어지는 규칙
# 최대값 -> n개로 만드는 최소값은 ... dp[n] = min(dp[2] + dp[n-2], dp[3] + dp[n-3], ...)
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

n = len(data)
min_list = [0, 0, 1, 7, 4, 2, 6, 8]
dp = dict()
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 0
dp[7] = 8
for num in data:
    # 가장 큰 수 구하기
    # Greedy, 1로 채워나가며 자릿수를 최대화 한다. 가장 앞자리는 7 혹은 1
    num_copy = num
    max = ''
    while num_copy >= 2:
        if num_copy == 3:
            max = '7' + max
            break
        num_copy -= 2
        max = '1' + max
    max = int(max)

    # 가장 작은 수 구하기
    # Dp
    for i in range(2, num+1):
        if i <= 7:
            continue

        sub_list = []
        for j in range(2, 8):
            if i-j < 2:
                break
            left = str(min_list[j])
            right = str(dp[i-j])
            if len(right) > 1 and right[0] == '6':
                right = '0' + right[1:]
            sub_list.append(int(left + right))

        dp[i] = min(sub_list)

    if num == 6:
        _min = 6
    else:
        _min = dp[num]
    print(_min, max)
