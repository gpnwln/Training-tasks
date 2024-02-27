n = int(input())
attacked_quarters = [tuple(map(int, input().split())) for _ in range(n)]
attacked_quarters_set = set(attacked_quarters)

l = 0
for r, c in attacked_quarters:
    if (r + 1, c) not in attacked_quarters_set:
        l += 1
    if (r - 1, c) not in attacked_quarters_set:
        l += 1
    if (r, c + 1) not in attacked_quarters_set:
        l += 1
    if (r, c - 1) not in attacked_quarters_set:
        l += 1
print(l)
