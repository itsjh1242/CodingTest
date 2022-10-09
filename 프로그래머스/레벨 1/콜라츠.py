n = 6
answer = 0
def test(n, answer):
    i = 0
    while n != 1:
        if i == 500: return -1
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        i += 1
        answer += 1
    return answer

print(test(n, answer))