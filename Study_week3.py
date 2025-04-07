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
    print(" " * (star - i) + "*" * i)