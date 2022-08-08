white = list(input().split())
black = [1,1,2,2,2,8]
for i in range(6):
    print(black[i] - int(white[i]), end=" ")
