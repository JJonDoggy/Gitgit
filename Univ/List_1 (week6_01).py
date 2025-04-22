# sum()함수 - 순서가 있는 문자열을 괄호안에 넣으면 그거 다 더한 값을 반환해줌.

# list = [1, 2, 3, 4]
# sum(list)
# ==> 10


# 인덱스(첨자, index)
# 순서가 있는 데이터에서 특정 순서의 데이터를 참조하기 위한 숫자
# **0부터 시작**

# 음수 인덱스는 뒤에서부터 순서를 셈

# my_list = [1, 2, '텍스트']
# print(my_list[-2])
# ==> 2


# 슬라이스(slice)
# 사용 : 순서가 있는 데이터에서 [시작인덱스 : 끝인덱스]
# 그럼 시작 인덱스 부터 끝 인덱스 전 까지 가져옴
# my_list[2:3]
# my_list[0:5:2]    이건 2칸 씩 띄워서 가져옴
# [:]이렇게 쓴다면 그 전체를 복제해서 가져옴.


# 리스트를 하나씩 추가하기
# - 리스트이름.append(값)         append : 뒤에 값을 추가함

# myList = []

# myList.append(10)
# myList.append(20)
# myList.append(30)

# print(mylist)
# --> [10, 20, 30]

# Q. 그냥 어느 변수에 입력받아서 인덱스로 값을 변경하면 되는거 아닌가요?
# - 그럼 입력받을 길이를 미리 알거나 설정해야 함.
# append를 사용한다면 list를 비워놓고 원하는 길이만큼 값을 추가할 수 있다.


# 리스트의 메모리 경로
# my_list1 = [1, 2, 3, 4, 5]
# my_list2 = my_list1                   - 얕은 복사
# my_list3 = my_list1[:]                - 깊은 복사

# my_list2[2] = 1
# print(my_list1[2])
# --> 1

# print(my_list3[2])
# --> 3

# 리스트, 튜플, 딕셔너리에 대입 연산자를 사용하는 건 단순히 대입이 아니라
# 같은 경로로 이어주는 것이다.
# my_list3 은 my_list1과 같은 리스트가 복제되어 다른 메모리공간에 리스트가 또 생긴 것이다.


# 리스트의 덧셈, 곱셈
# --> 문자열과 비?슷?

score_list = [0] * 5
for i in range(len(score_list)):
    socre_list.append(int(input('평가 점수 ==> ')))
print(f'심사위원 평균 점수 : {sum(score_list) / len(score_list):.2f}')