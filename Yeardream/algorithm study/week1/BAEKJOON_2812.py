# 메모리 32184 KB
# 시간 176 ms
def remove_k_digits(num, k):
    num_stack = []

    for digit in num:
        while k and num_stack and num_stack[-1] < digit:
            num_stack.pop()
            k -= 1

        num_stack.append(digit)

    if k > 0:
        return "".join(num_stack[:-k])
    else:
        if num_stack:
            return "".join(num_stack)
        else:
            return "0"


N, K = map(int, input().split())
number = input()

print(remove_k_digits(number, K))
