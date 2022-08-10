# 더하기 사이클
n = int(input())
s,c = n,0
while True:
    s = s%10*10+(s//10 + s%10)%10
    c += 1
    if s == n: break
print(c)