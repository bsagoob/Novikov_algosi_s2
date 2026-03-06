n = int(input())
starts = list(map(int, input().split()))
ends = list(map(int, input().split()))

meetings = sorted(zip(ends, starts))

count = 0
last_end = -1

for end, start in meetings:
    if start > last_end:
        count += 1
        last_end = end

print(count)
