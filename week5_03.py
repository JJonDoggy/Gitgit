# 7. 안전한 비밀번호 만들기


while True:
    password = input('비밀번호 입력 ==> ')
    if len(password) < 8 :
        print('비밀번호 길이를 8자 이상으로 입력해주세요.')
    elif not any(char.isdigit() for char in password):
            print('비밀번호에 숫자(0~9)를 최소 하나 포함해주세요.')
    elif not any(char.isalpha() for char in password):
            print('비밀번호에 영문자를 최소 하나 포함해주세요.')
    if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
            print(f'안전한 비밀번호가 설정되었습니다 : {password}')
            break


is_long_enough = len(password) >= 8
is_having_digit = any(i.isdigit() for i in password)
is_having_alpha = any(i.isalpha() for i in password)

while True:
    password = input("비밀번호를 입력해주세요 : ")
    if not is_long_enough:
        print('8자리 이상으로 입력해주세요')
    elif not is_having_digit:
        print('숫자(0~9)를 최소 하나 포함해주세요')
    elif not is_having_alpha:
        print('알파벳(a~z)을 최소 하나 포함해주세요')
    if is_long_enough and is_having_digit and is_having_alpha:
        print(f'안전한 비밀번호가 설정 되었습니다 : {password}')
        break

# 9. 가방 용량 검사

C = int(input('무게 제한을 입력하세요 ==> '))
N = int(input('아이템 개수를 입력하세요 ==> '))
totalWeight = 0

for i in range(1, N+1):
    eachWeight = int(input('각 아이템의 무게를 입력하세요 ==> '))
    totalWeight += eachWeight

    if totalWeight > C:
        totalWeight -= eachWeight
        break

print(f'가방에 {i-1}개의 아이템을 담았으며' , end = "")
print(f'남은 용량은 {C - totalWeight}입니다.')


# 10. 구구단 퀴즈

import random

N = int(input('풀 문제의 개수를 입력하세요 ==> '))
count = 0


for i in range(1, N+1):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    answer = int(input(f' {i}번 문제 : {a} * {b} = '))
    if answer == (a * b):
        print('정답!')
        count += 1
    else:
        print('오답!')

print(f'최종적으로 맞힌 문제의 개수는 {count}개 입니다.')


# 14. 보물 지도와 소수

N = int(input('범위 : 2 ~ '))
for num in range(2,N+1):
    for i in range(2, int(num**0.5 + 1)):          # 소수 판별 코드 부분은 GPT내용 확인
        if num % i == 0:
            break
    else:
        print(num, end="")


# 11. 별 피라미드 출력

N = int(input('높이를 입력하세요 ==> '))

for star in range(1, N+1):
    stars = '*' * (2 * star - 1)                # 걍 ㅈㄴ 어렵네
    spaces = '' * (N - star)
    print(spaces + stars)                 # 공백이 출력되고 *이 출력되는데 이게 중앙정렬처럼 보임