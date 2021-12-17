# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

    
def change_string(s):
    main_oper, sub_oper, target = s.split(";")
    result = ""

    # 분리(split)
    if main_oper == "S":
        if sub_oper == "M" or "C" or "V":
            for i in range(len(target)):
                if target[i].isupper():
                    if i > 0:
                        result += ' '
                result += target[i]
            result = result.lower()
            result = result.replace("()", "")
        else:
            result = "Value Error: wrong operator"
    # 결합(combine)
    elif main_oper == "C":
        if sub_oper == "M":
            for i in range(len(target)):
                if target[i] == " ":
                    target[i+1] = target[i+1].upper()
                result += target[i]
            # string type 변수 result의 우측 공백을 제거해야 줄바꿈이 일어나지 않음
            result = result.rstrip() + "()\n"
            result = result.replace(" ", "")
        elif sub_oper == "C":
            target[0] = target[0].upper()
            for i in range(len(target)):
                if target[i] == " ":
                    target[i+1] = target[i+1].upper()
                result += target[i]
            result = result.replace(" ", "")
        elif sub_oper == "V":
            for i in range(len(target)):
                if target[i] == " ":
                    target[i+1] = target[i+1].upper()
                result += target[i]
            result = result.replace(" ", "")
        else:
            result = "Value Error: wrong operator"

    sys.stdout.write(result)


for line in sys.stdin:
    change_string(line)
