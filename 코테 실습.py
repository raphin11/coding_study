#구현 문제 1(걍 빼낌...)
n=int(input())
moves=input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for move in moves:
    for i in range(4):
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if 1<=nx<=n and 1<=ny<=n:
        x, y = nx, ny

print(x,y)
        
