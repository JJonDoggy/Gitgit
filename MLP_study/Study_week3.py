# 구구단 계산기

dan = int(input())
for i in range(1,10):
    print(f'{dan} * {i} = {dan * i}')

# 별 찍기 - 1        # 첫째줄에는 별 1개, 둘째줄에 별 2개, ...

star = int(input())
for i in range(1, star+1):
    print('*' * i)

#  별 찍기 - 2           # 이번에는 오른쪽에서 출력

star=int(input())
for i in range(1,star+1):
    print(" " * (star - i) + "*" * i)        # f-string 사용시 불 필요한 공백이 생기는 것 주의!! 


# A + B - 3 (10950번)

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print(A + B)

# 코딩은 체육과목 입니다 (25314번)

N = int(input())

multiply_num = N // 4 

print('long ' * multiply_num + 'int')

