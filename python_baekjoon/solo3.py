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