# 5주차는 문제 풀이 위주로 진행됨 
# 문제는 LMS에 업로드된 quiz-2 파일을 확인하길 바람


# 1. 일주일 용돈 관리

daily = int(input('하루 용돈을 입력 : '))
over_day = 0

for i in range(1,8):
    paid = int(input(f'{i}일차 지출 금액 : '))
    if paid > daily:
        over_day += 1

print(f'예산을 초과한 날은 {over_day}일 입니다.')


# 2. 용에게 먹이 주기

M = int(input('매일 용에게 줘야하는 먹이의 양 : '))
N = int(input('먹이를 준 일 수 : '))

deadline = 0
hungryday = 0

for i in range(1, N+1):
    irl = int(input(f'{i}일차에 준 먹이 양 ==> '))
    if irl < M:
        deadline += 1
        hungryday += 1
    elif irl >= M:
        deadline = 0
    if deadline == 2:
        break

if deadline == 2:
    print('먹이를 이틀 연속 제대로 주지 않아 용이 떠났습니다!')
else:
    print(f'{i}일 동안 먹이를 제대로 먹지 못한 날은 {hungryday}일 입니다.')

# 3. 보물 상자 암호 맞추기

import random
password = random.randint(1,100) # 1~100 까지의 무작위 수 지정 (range랑 쓰는 법 다름 ㅋ)
try_num = 0

while True:
    guess = int(input('비밀번호는 뭘까요? ==> '))
    if guess > password:
        print(f'{guess}보다 작아요.')
        try_num += 1
    elif guess < password:
        print(f'{guess}보다 커요.')
        try_num += 1
    else:
        print('정답!')
        try_num += 1
        break

print(f'{try_num}회 시도끝에 맞추셨네요.')

