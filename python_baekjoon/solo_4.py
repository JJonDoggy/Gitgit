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