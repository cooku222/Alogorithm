def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        for b in str(num):
            if b == str(k):
                answer += 1
    return answer