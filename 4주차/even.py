numbers = []

while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

even = numbers[1::2]
print(*even)
