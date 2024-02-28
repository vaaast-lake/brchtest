def dfs(r, c):
    global total
    total += 1
    visited[r][c] = 1
    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + di, c + dj
        if 0 <= nr < N and 0 <= nc < N:
            if rooms[nr][nc] == (rooms[r][c]+1):
                dfs(nr, nc)

for tc in range(int(input())):
    N = int(input())
    rooms = [list(map(int ,input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]     # 탐색 수(실행시간)을 줄여주기 위한 변수로 넣어준다.
    result = 0
    room_number = 0xfffff
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:      # 만약 방문했다면, 탐색을 안해도 된다. 1이 찍혀있으면 무조건 그 전에 돈 total보다 낮다.
                total = 0               # total은 최대 이동 가능 횟수
                dfs(i, j)
                if total > result:      # 최대 이동 횟수를 계속 비교하여 넣어주고
                    result = total
                    room_number = rooms[i][j]   # 방의 번호 또한 넣어준다.
                # 같은 최대 이동 횟수가 나오는 경우가 있다.
                elif total == result:           # 이 때는 방 번호 중 가장 작은 번호로 한다.
                    room_number = min(room_number, rooms[i][j])

    print(f'#{tc+1}', room_number, result)