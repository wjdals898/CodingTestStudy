h, m = map(int, input().split())
print(-1%24)
print((h-(m<45))%24, (m-45)%60)