# 내가 맡은 2주차 문제
# 성택이의 은밀한 비밀번호 (https://www.acmicpc.net/problem/25372)

for i in range(int(input())):    # i는 _(언더바)로 해도 댐
    num = len(input())
    if 6 <= num <= 9:
        print('yes')
    else:
        print('no')

# len 함수 : len() 은 리스트나 문자열과 같은 시퀀스 자료형의 길이를 반환해줌. 
# 이 len() 을 활용하면 길이 값을 활용하여 리스트나 문자열 등의 요소에 접근할 수 있게 되는 것.
# 출처 : 코드잇 (사랑해요! 😍)

# 해결못한 것 : input 받을 변수를 지정하는 방식으로 코드를 실행하면 런타임 에러가 생김.(백준에서)
