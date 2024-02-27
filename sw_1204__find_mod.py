# f = open('./sw_1204__find_mode__input.txt', 'r')
#
# data = f.read().rstrip().split('\n')
#
# print(data)
#
# f.close()

for i in range(int(input())):
    case_num = int(input())
    scores = list(map(int, input().split()))

    score_table = [0 for _ in range(101)]
    for score in scores:
        score_table[score] += 1

    max_mod = 0
    max_mod_num = 0
    for num, mod in enumerate(score_table):
        if max_mod <= mod:
            max_mod = mod
            max_mod_num = num

    print(f'#{case_num} {max_mod_num}')


