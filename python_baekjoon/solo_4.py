# 5086번 - 배수와 약수

while True:
    num1, num2 = map(int, input().split())
    if num1 == num2 == 0:
        break

    if num2 % num1 == 0:
        print("factor")
    if num1 % num2 == 0:
        print("multiple")
    if num2 % num1 != 0 and num1 % num2 != 0:
        print("neither")


# 5171번 - 상근이의 친구들
