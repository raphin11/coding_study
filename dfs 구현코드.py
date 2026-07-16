#dfs 구현
def dfs(x,y):
    if x<=0 or y<=0 or x>=n or y>=n:
        return False
    if graph[x][y] == 0: #아직 방문 X라면(괴물 없는 곳이라면)
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    
    return False #방문한 곳이라면

    
