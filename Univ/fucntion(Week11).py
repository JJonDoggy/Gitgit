# 함수의 정의
    # def 함수이름(매개변수1, 매개변수2, ...):
        # ......

# 함수의 사용 (호출, call)
    # 반환값이 있는 경우 - 변수 = 함수이름(인자1, 인자2, ...)
    # 없는 경우 - 함수이름(인자1, 인자2, ...)

# 매개변수 (parameters, params)
# -> 함수의 정의에서 함수의 실행을 위해 전달받아야 하는
#   정보를 담기위한 변수들

# 인자 (또는 인수 arguments, args)
# -> 함수를 호출할 때 실제로 전달되는 정보(값, 변수 등...)

# 함수를 처리할 때 할당되는 메모리 공간은 끝나면 정보와 같이 사라진다.

# 함수의 유형

    # 1. 매개변수 x, 반환값x
    # 완전 수동적인 역할, 거의 안씀..
    # 코드의 절약 보다는 복잡한 처리의 모듈화에 사용

def func1():
    print('깡통')

func1()   # 호출

    # 2. 매개변수 1개, 반환값x
def func2(a):
    res = a + 10
    print(f'{a} + 10 = {res}')

func2(10)

    # 3. 매개변수 3개, 반환값x
def func3(a, b, c):
    res1 = a + b
    res2 = a - c
    print(f'{a} + {b} = {res1}')
    print(f'{a} - {c} = {res2}')

func3(15, 3, 8)

    # 4. 매개변수x, 반환값o
    # 반환값은 return을 이용해서 지정
def func4():
    return 3.141592
mypi = func4()
print(f'mypi = {mypi}')

    # 반환값이 없는 함수의 결과를 변수에 저장한다면 함수가 종료되지는 않지만
    # None이 들어간다.

    # 5. 매개변수o, 반환값o
def func5(r): # 반지름 r이 주어졌을 때 원의 넓이를 반환
    return r ** 2 * func4()
r = 7
area = func5(r)

    # 부록1. 매개변수의 기본값(default values)
    # 매개변수에는 기본값을 설정할 수 있다~
    # 인자가 설정되지 않았다면 기본값을 사용한다.

def func99(a, b, c=99):  # c의 기본값 : 99
    res1 = a + b
    res2 = a - c
    print(f'{a} + {b} = {res1}')
    print(f'{a} - {c} = {res2}')

func99(10, 3) # 이래도 실행이 된다.

def func100(a=100, b, c):  # 근데 이건 안된다.
def func1001(b, c, a=100):  # *기본값이 있는 매개변수는 기본값이 없는 매개변수보다 뒤에 있어아 한다

# 그냥 이렇게 쓰면된다.
func99(a=100, b=200, c=300) # 인자를 어느 파라미터에 넣을지 명시적으로 지정 가능하다.

    # 부록2. return에 대해서..
    # 2-1 : 모든 프로그래밍 언어에서 함수는 하나의 정보만 반환 가능
    # 파이썬은 튜플의 잠재적 문법으로 인해 여러 개의 반환값을 지원하는 것 처럼 보일 수 있다 (아님)
def func3q421(a, b, c):
    res1 = a + b
    res2 = a - c
    return res1 # 근데 python은 return res1, res2해도 됨ㅋㅋㅋㅋㅋㅋㅋ (튜플로 처리해서)

func3q421_res1 = func3q421(10, 5, 2)
print(f'어쩌고의 res1 : {func3q421_res1}')

    # 여러 정보를 반환하고 싶다면?
    res = [res1, res2] # 기본적으로 list를 사용할 수 있다.
    return res


    # 2-2 : return이 실행되면 함수는 즉시 종료
def funcInstant(c):
    if c == 'A':
        print('대문자 A입력')
        return
    print(f'입력된 문자 : {c}')

funcInstant('A')

# 전역변수(Global Variables)
# 지역변수(Local Variables)

# 과제 : 함수 내에서 b값을 수정했는데 왜 호출이후에 값이 5로 되돌아왔을까------
b = 5 # 파이썬 기준 들여쓰기 없이 선언된 변수 --> 전역변수

def func11(a):
    c = 10 # 지역변수
    b = 99
    print(f'func11 - b : {b}')
    return a + b + c

print(func11(8))
print(f'global - b : {b}')
print(c)
