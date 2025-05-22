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
