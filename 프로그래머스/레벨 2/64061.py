board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]
moves = [1,5,3,5,1,2,1,4]

basket = []
answer = 0

for _ in moves:
    for __ in range(len(board[0])):
        va = board[__][_ - 1]
        if va == 0: continue
        if not basket:
            board[__][_ - 1] = 0
            basket.append(va)
            break
        if basket[-1] == va:
            board[__][_ - 1] = 0
            basket.pop()
            answer += 2
        else:
            board[__][_ - 1] = 0
            basket.append(va)
        break
            
        
print(basket, answer)