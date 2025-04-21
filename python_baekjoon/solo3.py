#10156번 - 과자
snack_p, snack_num, money = map(int, input().split())
total = snack_p * snack_num
if total > money:
    print(total - money)
else:
    print('0')