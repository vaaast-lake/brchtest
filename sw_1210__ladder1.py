import sys

sys.stdin = open('./sw_1210__ladder1__input.txt', 'r')

for ts in range(10):
    case_num = int(input())

    path_table = []
    for _ in range(100):
        path_table.append(list(map(int, input().split())))

    cur_pos = [99, -1]
    for i in range(100):
        if path_table[99][i] == 2:
            cur_pos[1] = i
            break

    remote_ctr = [[0, 1], [0, -1], [-1, 0]]
    visited = [99, -1]
    while cur_pos[0] > 0:
        cur_pos_x, cur_pos_y = cur_pos[0], cur_pos[1]
        visited_x, visited_y = visited[0], visited[1]
        for i in range(3):
            move_x, move_y = remote_ctr[i]
            next_pos_x, next_pos_y = cur_pos_x + move_x, cur_pos_y + move_y
            if next_pos_y > 99 or next_pos_y < 0 or (next_pos_x == visited_x and next_pos_y == visited_y):
                continue
            if path_table[next_pos_x][next_pos_y] == 1:
                visited[0] = cur_pos_x
                visited[1] = cur_pos_y
                cur_pos[0] = next_pos_x
                cur_pos[1] = next_pos_y
                if cur_pos[0] == 0:
                    cur_pos[1] = next_pos_y
                break

    print(f'#{ts+1} {cur_pos[1]}')

sys.stdin.close()