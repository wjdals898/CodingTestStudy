# 분수찾기
x = int(input())
n = 1
while True:
    if x > n:
        x -= n
        n += 1
    else: break
print(str(x)+"/"+str(n-x+1) if n%2==0 else str(n-x+1)+"/"+str(x))