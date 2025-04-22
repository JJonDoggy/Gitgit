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


# 갑자기 생각난 ver2