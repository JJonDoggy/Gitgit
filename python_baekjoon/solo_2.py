# 10699번 - 오늘 날짜

print('2025-04-14')

# 이렇게 해도 되지만 datetime 모듈을 사용할 수 있다.

from datetime import date 

today = date.today()
print(today)


# 7287번 - 등록

print('24')
print('jjondoggy') # 데이터를 받아와서 하는 문제인줄... 뭐냐

# 2530번 - 인공지능 시계
# 2525번 오븐시계 문제를 참고함.

Hour, Min, Sec = map(int, input().split())
D = int(input())

Min += D // 60
Sec += D % 60

while Sec >= 60:
    Min += 1
    Sec -= 60


while Min >= 60:
    Hour += 1
    Min -= 60


while Hour >= 24:
    Hour -= 24


print(Hour, Min, Sec)


# 2914번 - 저작권

A, I = map(int, input().split())
melody = A * (I - 1)
print(melody + 1)


# 5355번 - 화성 수학

T = int(input())

for a in range(T):
    values = input().split()
    result = float(values[0])

    for value in values[1:]:
        if value == '@':
            result = result * 3
        elif value == '%':
            result = result + 5
        elif value == '#':
            result = result - 7
    print(f'{result:.2f}')


# 2675번 - 문자열 반복

T = 0
times = int(input())
for i in range(times):
    attempt, string = input().split()
    attempt = int(attempt)
    T = len(string)
    list(string)
    for a in range(T):
        print(f'{string[a] * attempt}', end='')
    print()


# 2935번 - 소음
A = int(input())
how = input()
B = int(input())
if how == '*':
    print(A*B)
elif how == '+':
    print(A+B)


# 9498번 - 시험 성적

score = int(input())
if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
else:
    print('F')


# 10817번 - 세 수

# 내가 생각한 풀이
a, b, c = map(int, input().split())
total = a + b + c
maximum = max(a, b, c)
minimum = min(a, b, c)
mid = total - maximum - minimum
print(mid)

# gpt가 알려준 풀이
nums = list(map(int, input().split()))
nums.sort()
print(nums[1])

# sort()를 쓰면 큰 순서대로 정렬
# 
# 또는 if문을 사용한 풀이도 가능
a, b, c = map(int, input().split())

if (a >= b and a <= c) or (a <= b and a >= c):
    print(a)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print(b)
else:
    print(c) 


# 11653번 - 소인수분해
Num = int(input())
divide = 2
while True:
    if (Num % divide) == 0:
        print(divide)
        Num /= divide
    else:
        divide += 1
    
    if Num <= 1:
        break


# 1789번 - 수들의 합
n_num = int(input())
count = 0
i = 1
total = 0

while (total + i) <= n_num:
    total += i
    i += 1
    count += 1

print(count)


# 2753번 - 윤년
year = int(input())
if (year % 4) == 0 and (year % 100) != 0:
    print('1')
elif (year % 4 ) == 0 and (year % 400) == 0:
    print('1')
else:
    print('0')


# 10039번 - 평균 점수

score = []
for a in range(5):
    score.append(int(input()))
    if score[a] < 40: 
        score[a] = 40
    
print(int(sum(score) / 5))


# 1934번 - 최소공배수
import math

T = int(input())
for i in range(T):
    A, B = map(int, input().split())     # 최대공배수 공식 = 두수의 곱 / 최대공약수수
    lcm = A * B // math.gcd(A, B)   # LCM(A, B) = A × B / GCD(A, B)
    print(lcm)