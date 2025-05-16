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

#10156번 - 과자
snack_p, snack_num, money = map(int, input().split())
total = snack_p * snack_num
if total > money:
    print(total - money)
else:
    print('0')


# 3009번 - 네 번째 점
x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
x_3, y_3 = map(int, input().split())

x_4 = max(x_1, x_2, x_3)
y_4 = max(y_1, y_2, y_3)

myList1 = [x_1, x_2, x_3]
myList2 = [y_1, y_2, y_3]

if myList1.count(x_4) >= 2:
    x_4 = min(x_1, x_2, x_3)
if myList2.count(y_4) >= 2:
    y_4 = min(y_1, y_2, y_3)
print(x_4, y_4)

# 다른 풀이
x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)


# 2476번 - 주사위 게임

# 처음 작성한 코드 ver1
N = int(input())
result = []
for n in range(N):
    dice_1, dice_2, dice_3 = map(int, input().split())
    Big = max(dice_1, dice_2, dice_3)
    
    if dice_1 == dice_2 == dice_3:
        res1 = 10000 + dice_1 * 1000
        result.append(res1)
    elif dice_1 == dice_2 or dice_1 == dice_3:
        res2 = 1000 + dice_1 * 100
        result.append(res2)
    elif dice_2 == dice_3:
        res3 = 1000 + dice_2 * 100
        result.append(res3)
    else:
        res4 = Big * 100
        result.append(res4)
print(max(result))


# 2754번 - 학점계산

grade = input()
if grade == 'A+':
    print(4.3)
elif grade == 'A0':
    print(4.0)
elif grade == 'A-':
    print(3.7)
elif grade == 'B+':
    print(3.3)
elif grade == 'B0':
    print(3.0)
elif grade == 'B-':
    print(2.7)
elif grade == 'C+':
    print(2.3)
elif grade == 'C0':
    print(2.0)
elif grade == 'C-':
    print(1.7)
elif grade == 'D+':
    print(1.3)
elif grade == 'D0':
    print(1.0)
elif grade == 'D-':
    print(0.7)
elif grade == 'F':
    print(0.0)


# 2884번 - 알람 시계

Hour, Min = map(int, input().split())
setMin = Min - 45
if setMin < 0:
    setMin = 60 - (45 - Min)
    Hour -= 1
if Hour < 0:
    Hour = 23
print(Hour, setMin)


# 7567번 - 그릇

# 내가한 ㅂㅅ짓 (실패)
height = 0
overlap = 1

case = input()
case = list(case)
case.append('c')
b = case[0]


for a in range(1, len(case)):
    if a == len(case) - 1:
        break
    if a > 1:
        if overlap == 1:
            b = case[a+1]
    if case[a] == b:
        overlap += 1
    elif case[a] != b:
        if overlap >= 2:
            height += 10 + ((overlap - 1) * 5)
        else:
            height += 20
        overlap = 1
if overlap >= 2:
    height += 10 + ((overlap - 1) * 5)
print(height)

# 하도안풀려서 검색하거나 gpt물어본거 :
dish = input()
total = 10  # 첫 번째 접시는 무조건 10

for i in range(1, len(dish)):
    if dish[i] == dish[i-1]:
        total += 5
    else:
        total += 10

print(total)


# 5063번 - TGN
N = int(input())
for i in range(N):
    r, e, c = map(int, input().split())
    if r > e - c:
        print('do not advertise')
    elif r == e - c:
        print('does not matter')
    elif r < e - c:
        print('advertise')

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


# 9506번 - 약수들의 합
# join 함수에대해.. join에서 쓸수있는건 문자열이기 때문에 map도 같이 써주었다.
# 그리고 이걸 list로 처리한다는 아이디어.. 중요 ⭐

while True:
    N = int(input())
    if N == -1:
        break
    measure = []
    for a in range(1, N):
        if N % a == 0:
            measure.append(a)

    if sum(measure) == N:
        print(f'{N} = {' + '.join(map(str, measure))}')
    else:
        print(f'{N} is NOT perfect.')


# 10162번 - 전자레인지
A = 300
B = 60
C = 10

A_attempt = 0
B_attempt = 0
C_attempt = 0

sec = int(input())


if sec < B:
    C_attempt += sec // C
    sec = sec % C

elif sec < A:
    B_attempt += sec // B
    sec = sec % B
    C_attempt += sec // C
    sec = sec % C

else:
    A_attempt += sec // A
    sec = sec % A
    B_attempt += sec // B
    sec = sec % B
    C_attempt += sec // C
    sec = sec % C

if sec % C != 0:
    print(-1)
else:
    print(f'{A_attempt} {B_attempt} {C_attempt}')

# 10103번 - 주사위 게임
N = int(input())

C_score = 100
S_score = 100
for _ in range(N):
    C, S = map(int, input().split())
    if C > S:
        S_score = S_score - C
    elif S > C:
        C_score = C_score - S
    elif C == S:
        continue
print(C_score)
print(S_score)


# 11557번 - Yangjojang of The Year
T = int(input())         # dictionary 한 번 써봄!! 근데 진짜 되네!!
dict = {}
beerPig = 0
for a in range(T):
    N = int(input())
    for b in range(N):
        univ_name, L = input().split()
        L = int(L)
        dict[univ_name] = L
        beerPig = max(dict.values())
        reverse = {k:v for v,k in dict.items()}  # 기본적으로 key > value 방향으로만 접근 가능함. value값으로 key에 접근하기 위해 key와 value가 서로 바뀐 딕셔너리를 하나 더 만들었음.
    print(reverse[beerPig])
    dict = {}
    beerPig = 0


# 10214번 - baseball
T = int(input())
yScore = 0
kScore = 0
for a in range(T):
    for b in range(9):
        y, k = map(int, input().split())
        yScore += y
        kScore += k
    if yScore > kScore:
        print('Yonsei')
    elif yScore < kScore:
        print('Korea')
    else:
        print('Draw')


# 10757번 - 큰 수 A+B
A, B = map(int, input().split())
print(A + B)

