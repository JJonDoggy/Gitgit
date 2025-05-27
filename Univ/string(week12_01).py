# **문자열**

# a = [1, 2, 3, 4, 5]
# b = '파이썬'
# a[2:3] = [44, 55] # 가능

# b[2] = '하이' # 불가능
# b = b[:2] + '하이' b[3:] # 가능

# 각 문자뒤에 $ 붙이기
# ss='파이썬짱'
# for i in ss:
#    print(i + '$', end='')


# 문자열 거꾸로 하기
# ss='파이썬짱'
# for i in reversed(ss):
#   print(i, end='')

# list 내장함수 sort : 원본을 정렬함, 반환값 None
# 파이썬 sorted : 그냥 정렬한 다른 정보를 반환

# 문자열 함수 - (메소드)
# upper(): 모두 대문자로
# lower(): 모두 소문자로
# swapcase(): 대문자 소문자 서로 바꾸기
# title(): 각 단어의 첫글자를 대문자로

# 문자열 찾기
# count(): string에서 sub-string이 몇번 등장하는지
# find(): sub-string이 몇번 인덱스부터 시작하는지 찾아줌
    # find('공부', 5) - 5번인덱스 부터 찾음
    # rfind(): 뒤에서 부터 (오른쪽)
    # 찾을 수 없는 경우 -1을 출력

# index(): find랑 비슷하지만 없는 단어를 찾으려고 할 경우 코드가 터짐
# startswith(): 이 문장이  ()에 넣은 단어로 시작하느냐? 맞으면 True
    # startswith('시작', 10) - 10번인덱스가 시작이라는 걸로 시작하냐?
# endswith(): 마지막 단어가 ~~

# 문자열 공백 삭제/변경
# strip(): 좌우 공백 삭제
# rstrip(): 오른쪽 공백 삭제
# lstrip(): 왼쪽 공백 삭제
# ()에 값을 넣어서 특정 문자를 삭제 가능

# ss = ' 파 이 썬 '
# strip -> '파 이 썬'
# rstrip -> '파 이 썬 '

# replace(): 특정 문자열을 다른 문자열으로 바꿈
# replace('파이썬', 'python') - 파이썬을 python으로

# split(): list의 형태로 나눠줌
# splitlines():
# ''.join():

# msg = '파이썬을 공부중'
# my_list = list(msg) --> ['파', '이', '썬', ...]
# msg2 = str(my_list) --> ['파', '이', '썬', ...] 이런 문자열을 만들어버림
# msg2 = ''.join(my_list) --> 파이썬을 공부중


# 문자열 정렬, 채우기
# center(칸 수)
# ljust()
# rjust()
# zfill()

# 문자열 구성 파악하기 - True 또는 False 반환
# isdigit()
# isalpha()
# isalnum()
# islower()
# issuper()
# isspace()