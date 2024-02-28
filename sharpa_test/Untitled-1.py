def back(x,s):
    global result
    if x == n:
        result = min(result,s)
        return
    if result < s:
        return
    for y in range(n):
        if visited[y]:
            continue
        if lst[x][y] == 0:
            continue
        
        visited[y] = True
        back(x+1,s+lst[x][y])
        visited[y] = False

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(n)]
    
    visited = [False] * n
    result = 10001
    back(0,0)
    
    print(f'#{tc}',result)