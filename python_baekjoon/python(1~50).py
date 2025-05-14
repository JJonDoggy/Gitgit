# 2588번 = 곱셈
num1 = int(input())
num2 = int(input())

print(num1 * (num2%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2//100))
print(num1 * num2)

# 3046번 - R2

R1, S = map(int, input().split())
print((2 * S) - R1)           # R2 출력

# 2163번 - 초콜릿 자르기

N, M = map(int, input().split())
print((N - 1) + (M - 1) * (N))

# 11021번 - A + B - 7
T = int(input())
list = []
for a in range(1, T+1):
    A, B = map(int, input().split())
    list.append(A + B)
for i in range(len(list)):
    print(f'Case #{i + 1}: {list[i]}')

# 근데 사실 list에 저장하지 말고 걍 반복문 하나에 print까지 다 넣어도 정답.

# 11022번 - A + B - 8

T = int(input())
numList = []
for a in range(T):
    A, B = map(int, input().split())
    numList.append(A + B)
    print(f'Case #{a + 1}: {A} + {B} = {numList[a]}')






