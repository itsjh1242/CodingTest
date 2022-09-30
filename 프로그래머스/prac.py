n = 216
       
for _ in range(1, n + 1):
    if _ + sum(map(int, [__ for __ in str(_)])) == n:
        print(_)
        break
else:
    print(0)
