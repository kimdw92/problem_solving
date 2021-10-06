# level2
# 단순구현
# 2D 리스트 TRANSPOSE

# MY ANSWER
def solution(scores):
    n = len(scores)
    means = []
    for i in range(n):
        score = [x[i] for x in scores]
        my = score[i]
        score.sort()
        if (my == score[0] and my != score[1]) \
        or (my == score[n-1] and my != score[n-2]):
            mean = (sum(score) - my) / (n-1)
        else:
            mean = sum(score) / n
        if mean >= 90:
            means.append('A')
        elif 90 > mean >= 80:
            means.append('B')
        elif 80 > mean >= 70:
            means.append('C')
        elif 70 > mean >= 50:
            means.append('D')
        else:
            means.append('F')
    return ''.join(means)
  
# OTHER ANSWER
def solution(scores):
    answer = ''

    for i, score in enumerate(zip(*scores)):
        avg = (sum(score) - score[i]) / (len(score) - 1) if score[i] in (min(score), max(score)) and score.count(score[i]) == 1 else sum(score) / len(score)
        answer += "%s" % (
            "A" if 90 <= avg else
            "B" if 80 <= avg else
            "C" if 70 <= avg else
            "D" if 50 <= avg else
            "F"
        )

    return answer
