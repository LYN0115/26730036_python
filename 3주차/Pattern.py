import random

def printPattern(rows, cols, char):
    for _ in range(rows):
        for _ in range(cols):  
            print(char, end="")
        print()  



rows = int(input("행 개수를 입력하세요: "))
cols = int(input("열 개수를 입력하세요: "))
char = input("출력할 문자를 입력하세요: ")

print("\n--- 입력 결과 ---")
printPattern(rows, cols, char)
