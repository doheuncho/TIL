# 메모리 : 29200 KB
# 시간 : 72 ms
def combination(n, k):
    nums = list(range(k)) + [n]
    result, j = [], 0
    while j < k:
        result.append(nums[:k])
        j = 0
        while j < k and nums[j + 1] == nums[j] + 1:
            nums[j] = j
            j += 1
        nums[j] += 1

    return result


L, C = map(int, input().split())
C_list = list(map(str, input().split()))
C_list.sort()

vowels = set(['a', 'e', 'i', 'o', 'u'])
consonants = set([x for x in C_list if x not in vowels])

comb = combination(C, L)

answer = []

for line in comb:
    c = 0
    for i in range(L):
        line[i] = C_list[line[i]]
        if line[i] in consonants:
            c += 1
    if L > c >= 2:
        answer.append(line)

answer.sort()

for line in answer:
    print("".join(line))
