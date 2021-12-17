# 메모리 : 29200 KB
# 시간 : 272 ms
def buy_card(n, p_list):
    table = [0 for _ in range(n + 1)]

    for c in range(n + 1):
        for i in range(len(p_list)):
            if c >= i + 1:
                table[c] = max(table[c], p_list[i] + table[c - i - 1])

    return table[n]


N = int(input())
P_list = list(map(int, input().split()))

print(buy_card(N, P_list))
