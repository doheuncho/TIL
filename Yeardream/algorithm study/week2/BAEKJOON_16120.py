# 메모리 : 36496 KB
# 시간 : 344 ms
def check_ppap(string):
    stack = []
    for c in string:
        stack.append(c)
        # "PPAP"가 반복되면 pop()을 이용해 "PAP"를 제거해 "P"로 만듬.
        if stack[-4:] == ["P", "P", "A", "P"]:
            stack.pop()
            stack.pop()
            stack.pop()

    if stack == ["P"]:
        return "PPAP"
    else:
        return "NP"


unknown_ap = input()
print(check_ppap(unknown_ap))
