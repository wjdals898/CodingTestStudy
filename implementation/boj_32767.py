# 계산기가 필요해

def print_calculator(result):
    print("=================\n|SASA CALCULATOR|")
    print(f'|{"{0:15.3f}".format(result)}|')
    print("-----------------")
    print("|               |")
    print("| AC         /  |")
    print("| 7  8  9    *  |")
    print("| 4  5  6    -  |")
    print("| 1  2  3    +  |")
    print("|    0  .    =  |")
    print("=================")


arr = list(input().split())
for i in range(0, 5, 2):
    arr[i] = float(arr[i])

answer = arr[0]
for j in range(1, 5, 2):
    if arr[j] == "+":
        answer += arr[j+1]
    elif arr[j] == "-":
        answer -= arr[j+1]
    elif arr[j] == "*":
        answer *= arr[j+1]
    elif arr[j] == "/":
        answer /= arr[j+1]


print_calculator(round(answer, 3))
