# 리스트 값 변경하기
    # 첨자를 이용
    # 리스트이름[인덱스] = 값

    # 슬라이싱으로도 변경 가능

        # myList = [1, 2, 3]
        # myList[2:3] = [10, 20]
        # print(myList)
        # >> [1, 2, 10, 20]

    # 근데 슬라이싱만 쓰는거 보다 슬라이싱과 더하기를 같이 쓰는걸 추천한다
        # myList = myList[:-1] + [10, 20]


# 리스트 값 삽입
    # append(값) : 맨 뒤에 값 추가하기
    # insert(위치, 값) : 정해진 위치에 값 삽입하기

# 리스트 값 삭제
    # del() : 괄호 안 삭제(메모리 반납)        ** 파이썬 내장함수임!

        # myList = [10, 20, 30]
        # del(myList[1])
        # >> [10, 30]

    # remove(지울 값) : 리스트에서 특정 값 삭제    ** list에 들어있는 함수

        # myList = [10, 20, 30]
        # myList.remove(20)
        # >> [10, 30]

        # myList = [10, 20, 30, 20, 20]
        # myList.remove(20)
        # >> [10, 30, 20, 20]

    # del과 remove에는 작성하는 형식이 다른 점도 있지만
    # remove는 없는 값을 넣었을 때 넘어가는 게 아니라 코드가 종료되서 if문에 넣곤 함.

    # 만약 중첩되있는 수를 지우려면?
        # myList = [10, 20, 20, 30]
        # while 20 in myList:
        #    myList.remove(20)

        # for i in range(myList.count(20)):
        #   myList.remove(20)


# 리스트의 값 추출하기
    # pop() : 제일 뒤의 값을 뽑아내서 값을 알려준 뒤 삭제 (값을 알려주는 건 python idle에서만)
    # 때낸 값을 반환하기 때문에 변수에 저장 가능
    # 괄호안에 인덱스를 넣으면 그에 맞게 추출 가능         del() 왜 쓰냐..


# 리스트 정렬하기
    # sort() : 리스트의 값을 오름차순 정렬
    # sort(reverse = True) : 내림차순 정렬

    # 문자열도 지원
        # myList = ['사과', '바나나', '가지']
        # myList.sort()
        # >> ['가지', '바나나', '사과']

    # 문자열과 숫자가 같이 있으면 터진다.

    # 만약 리스트의 값을 변경하는 게 아닌
    # 단지 결과값만 보고 싶었던 거라면

    # sorted()와 reversed()
    # 그냥 출력해도 되고 변수에 저장해도 되고 ~
    # 단, reversed()는 값을 하나씩 때는거라 다시 List로 만들어 줘야함

# 리스트 복사하기
    # copy() - 깊은 복사

        # numList = [1, 2, 3]
        # numList2 = numList1.copy()

# 2차원 리스트
    # 1차원 리스트를 여러개 연결한 리스트
    # 접근 : 리스트이름[행][열]

        # numList = [[1, 2, 3, 4], [5, 6, 7]]
        # print(numList[0][0])
        # >> 1

#------------------------------------------------------------

# N x N 크기의 정사각형 행렬 리스트를 입력받아 만들고
# 대각선의 합을 구한다 (N은 홀수라고 가정)

import random

N = int(input('N : '))
numList = []
for i in range(N):
    tmp = []
    for a in range(N):
        tmp.append(random.randint(-100, 100))
    numList.append(tmp)

for b in range(N):
    print(numList[b])

# 왼쪽위에서 오른쪽 아래 합
lt_rb = 0
for c in range(N):
    lt_rb += numList[c][c]

# 왼쪽 아래에서 오른쪽 위 합
lb_rt = 0
for d in range(N):
    lb_rt += numList[N - 1 - d][d]

print(f'왼쪽위에서 오른쪽아래 => {lt_rb}')
print(f'왼쪽아래에서 오른쪽위 => {lb_rt}')


# List Comprehension     리스트를 만드는 방식 중 하나
# 채우는 값들에 규칙이 있다면 쓴다.

    # my_list = []
    # for i in range(1, 10):
    #   my_list.append(i * i)

# 제곱을 추가하는 규칙이 있음.

    # my_list = [i * i for i in range(1, 10)]

# 조건도 추가 가능

    # my_list = [i * i for i in range(1, 10) if i % 2 == 0]
    # 짝수 제곱만 출력