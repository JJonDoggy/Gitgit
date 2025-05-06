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
while True:
    bf, gf = map(int, input().split())
    if bf == 0 and gf == 0:
        break
    print(f'{bf + gf}')


# 9610번 - 사분면
N = int(input())

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0

for a in range(1, N+1):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        Q1 += 1
    elif x > 0 and y < 0:
        Q4 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    else:
        AXIS += 1

print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AXIS: {AXIS}')


# 8958번 - OX퀴즈
testCase = int(input())          # sum에 sequence를 더하는 타이밍을 잘 생각하기

for _ in range(testCase):
    a = input()
    sequence = 0
    sum = 0
    for j in a:
        if j == 'O':
            sequence += 1
            sum += sequence
        else:
            sequence = 0
    print(sum)