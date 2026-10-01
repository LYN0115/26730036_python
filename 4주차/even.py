num = []

while True:
    n = int(input())
    if n == 0:
        break
    num.append(n)

print(*num[1::2])
