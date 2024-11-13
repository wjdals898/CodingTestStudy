# 카드 게임
card = [list(input().split()) for _ in range(5)]
colors = [c[0] for c in card]
numbers = [int(c[1]) for c in card]
cnt_num = [0] * 11
for i in range(5):
    num = numbers[i]
    cnt_num[num] += 1

numbers.sort()  # 숫자 오름차순 정렬
result = 0
# 1번 규칙
if len(set(colors)) == 1 and numbers[0]+4 == numbers[1]+3 == numbers[2]+2 == numbers[3]+1 == numbers[4]:
    result = numbers[-1] + 900
# 2번 규칙
elif 4 in cnt_num:
    result = cnt_num.index(4) + 800
# 3번 규칙
elif 3 in cnt_num and 2 in cnt_num:
    result = cnt_num.index(3) * 10 + cnt_num.index(2) + 700
# 4번 규칙
elif len(set(colors)) == 1:
    result = max(numbers) + 600
# 5번 규칙
elif numbers[0]+4 == numbers[1]+3 == numbers[2]+2 == numbers[3]+1 == numbers[4]:
    result = numbers[-1] + 500
# 6번 규칙
elif 3 in cnt_num:
    result = cnt_num.index(3) + 400
# 7, 8번 규칙
elif 2 in cnt_num:
    first = cnt_num.index(2)
    if 2 in cnt_num[first+1:]:
        second = first + 1 + cnt_num[first+1:].index(2)
        result = second * 10 + first + 300
    else:
        result = first + 200
# 9번 규칙
else:
    result = max(numbers) + 100

print(result)
