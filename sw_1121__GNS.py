import sys

sys.stdin = open('./sw_1121__GNS__input.txt', 'r')

nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
nums_table = {}
for i in range(10):
    nums_table[nums[i]] = i


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low = merge_sort(arr[:mid])
    high = merge_sort(arr[mid:])

    return merge(low, high)


def merge(low, high):
    merged_arr = []
    l = h = 0
    while l < len(low) and h < len(high):
        if nums_table[low[l]] <= nums_table[high[h]]:
            merged_arr.append(low[l])
            l += 1
        else:
            merged_arr.append(high[h])
            h += 1
    merged_arr += low[l:]
    merged_arr += high[h:]

    return merged_arr

for _ in range(int(input())):
    ts, length = input().split()
    strings = input().split()

    sorted_strings = merge_sort(strings)

    print(f'{ts}\n', *sorted_strings)




sys.stdin.close()