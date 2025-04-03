# 4. ATM 현금 인출
# 이 ATM은 1000원 단위로만 돈을 인출할 수 있으며, 
# 50,000원, 10,000원, 5,000원, 1,000원 지폐로만 지급됩니다. 
# 사용자가 인출 금액을 입력하면 각 지폐를 몇 장씩 받을지 계산해줍니다. 
# 만약 1000원 단위가 아닌 금액을 입력하면 ATM은 올바른 값이 입력될 때까지 다시 요청합니다. 
# 인출 할 금액이 유효하면 최소 개수의 지폐조합을 계산하여 출력하는 프로그램을 작성하세요.

while True:
    req_money = int(input('인출할 금액을 입력해주세요 : '))
    if req_money % 1000 != 0:
        print(f'1000원 단위로 금액을 입력해주셈')
    else:
        break

sinsaimdang = req_money // 50000
req_money = req_money % 50000   # req_money %= 50000 으로 가능할 듯

sejong = req_money // 10000
req_money = req_money % 10000

ee = req_money // 5000
req_money = req_money % 5000

ehwang = req_money // 1000
req_money = req_money % 1000

print('받을 지폐는')
if sinsaimdang > 0:
    print(f'50000원 권 {sinsaimdang}장')
if sejong > 0:
    print(f'10000원 권 {sejong}장')
if ee > 0:
    print(f'5000원 권 {ee}장')
if ehwang > 0:
    print(f'1000원 권 {ehwang}장')
print('입니다.')


# 5. 상점 할인 계산

total = 0
each_price = 0
rate = 0
f_price = 0

N = int(input('물건 몇개 구매 하셨나요? '))

for i in range(1,N+1):
    each_price = int(input(f'{i}번째로 구매한 물건의 가격을 입력해주세여 : '))
    total += each_price

if total >= 100000:
    f_price = total - (total * (1/10))
    rate = 10
elif total >= 50000:
    f_price = total - (total * (1/20))
    rate = 5
else:
    f_price = total

print(f'{rate}% 할인을 받아 결제 금액은 {int(f_price)}원 입니다.')

# 6. 성적 등급 계산

student = int(input('학생 수를 입력해주세요 ==> '))
grade = 0

for n in range(1,student+1):
    score = int(input(f'{n}번째 학생의 점수 ==> '))
    if 90 <= score <= 100:
        grade = 'A'
    elif 80 <= score <= 89:
        grade = 'B'
    elif 70 <= score <= 79:
        grade = 'C'
    elif 60 <= score <= 69:
        grade = 'D'
    else:
        grade = 'F'
    print(f'{n}번째 학생의 등급은 {grade}입니다.')
