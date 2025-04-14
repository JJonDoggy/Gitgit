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

