# 1977번 - 완전제곱수
M = int(input())
N = int(input())

squares = []

for i in range(1, 101):  # 100^2 = 10000이니까 범위는 1~100까지만 보면 됨
    square = i ** 2
    if M <= square <= N:
        squares.append(square)

if squares:
    print(sum(squares))
    print(min(squares))
else:
    print(-1)


# 11098번 - 첼시를 도와줘!
n = int(input())
for a in range(n):
    playerInfo = {}
    p = int(input())
    for b in range(p):
        price, name = input().split()
        price = int(price)
        playerInfo[price] = name
    expensive = max(playerInfo.keys())
    print(playerInfo[expensive])


# 5635번 - 생일
student = int(input())
arr1 = [] # 이차원 리스트 사용
arr2 = []
for a in range(student):
    name, day, month, year = input().split()
    day = int(day)
    month = int(month)
    year = int(year)
    arr1.append([year, month, day, name])
    arr2.append([year, month, day, name])
arr1.sort()             # 이차원 리스트의 정렬 기준 - 각 리스트의 0번 요소 값을 기준으로
arr2.sort(reverse=True) # 만약 요소 값이 모두 같다면 그 다음 1번 인덱스를 비교..
print(arr2[0][3])
print(arr1[0][3])


# 2741번 - N 찍기
N = int(input())
for a in range(1, N+1):
    print(a)


# 2742번 - 기찍 N
N = int(input())
for a in range(N, 0, -1):
    print(a)


# 2440번 - 별 찍기 3
starNum = int(input())
for a in range(starNum, 0, -1):
    print('*' * a)


# 2441번 - 별 찍기 4
starNum = int(input())
blank = 0
for a in range(starNum, 0, -1):
    if a < starNum:
        print(blank * ' ' + a * '*')
        blank += 1
    else:
        print(a * '*')
        blank += 1


# 8393번 - 합
num = int(input())
total = 0
for n in range(1, num+1):
    total += n
print(total)


# 2609번 - 최대공약수와 최소공배수
def gcd(a, b):       # 최대공약수 - 유클리드 호제법
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

num1, num2 = map(int, input().split())
print(gcd(num1, num2))
print(lcm(num1, num2))


# 2748번 - 피보나치 수 2
def fibonacci(a):
    mylist = []
    for i in range(a+1):
        if i == 0:
            fibo = 0
            mylist.append(fibo)
        elif i == 1:
            fibo = 1
            mylist.append(fibo)
        else:
            fibo = mylist[i-1] + mylist[i-2]
            mylist.append(fibo)
    return mylist[a]

n = int(input())
print(fibonacci(n))


# 5565번 - 영수증
total = int(input())
b = 0
for _ in range(9):
    each = int(input())
    b = b + each
print(total - b)


# 10984번 - 내 학점을 구해줘
T = int(input())
for a in range(T):
    list1 = []
    list2 = []
    N = int(input())
    for b in range(N):
        C, G = map(float, input().split())
        C = int(C)
        list1.append(C)
        list2.append(C * G)
    print(sum(list1), end=' ')
    print(f'{(sum(list2) / sum(list1)):.1f}')


# 10833번 - 사과
total = 0
school = int(input())
for a in range(school):
    i = 1
    student, apple = map(int, input().split())
    while True:
        if i * student > apple:
            i -= 1
            break
        else:
            i += 1
    total += (apple - student * i)
print(total)


# 2442번 - 별 찍기 5
star = int(input())
for i in range(1, star+1):
    print(' ' * (star - i) + '*' * (2 * i - 1) + ' ')


# 2443번 - 별 찍기 6
star = int(input())
for i in range(star, 0, -1):
    print(' ' * (star - i) + '*' * (2 * i - 1) + ' ')


# 2444번 - 별 찍기 7
star = int(input())
for i in range(1, star+1):
    print(' ' * (star - i) + '*' * (2 * i - 1) + ' ')
for i in range(star-1, 0, -1):
    print(' ' * (star - i) + '*' * (2 * i - 1) + ' ')