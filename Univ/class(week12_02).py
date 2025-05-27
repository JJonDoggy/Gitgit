# 객체 지향 프로그래밍 (class)
# 객체 - 어떤 속성과 행동을 가지고 있는 데이터         - 인스턴스(Instance)라고 하기도 한다
# 클래스 - 객체를 만들기 위한 설계도 또는 찍어내는 틀

# Rabbit 클래스 정의
class Rabbit:
    def __init__(self, shape, x=0, y=0):  # 생성자
        print('생성자 호출됨!!')
        self.shape = shape  # 상태
        self.xPos = x
        self.yPos = y # self.goto(x, y)

    def goto(self, x, y):  # 행동
        self.xPos = x
        self.yPos = y

    def __add__(self, other):       # ex : rabbit1 + rabbit2 를 할시 출력되는 값 설정하기
        print(f'{self.shape} 토끼와 {other.shape} 토끼가 친구가 되었습니다')

    # getter, setter : 속성값을 설정하거나 가져오기 위한 용도의 함수
    def set_shape(self, shape):
        self.shape = shape

    def get_shape(self):
        return self.shape

    def __del__(self):
        print(f'{self.shape} 토끼는..')

rabbitA = Rabbit('빨강')          # rabbitA는 class Rabbit의 객체다
rabbitA.goto(10, 20)
print(f'rabbitA - 모양 : {rabbitA.get_shape()}, x 위치 : {rabbitA.xPos}, y 위치 : {rabbitA.yPos}')

rabbitB = Rabbit('노랑', 50 ,25)
rabbitB.goto(5, 20)
print(f'rabbitB - 모양 : {rabbitB.shape}, x 위치 : {rabbitB.xPos}, y 위치 : {rabbitB.yPos}')


# 생성자 - 객체를 생성하면 무조건 호출되는 메소드. | 메모리에 클래스 위치 할당, 생성자로 fix, 객체의 이름 설정
    #  - 초기 상태 값을 결정하는 용도
    # - def __init__():

# 객체 지향 프로그래밍에서 클래스에 관한 코드를 작성할 때
# 1. 객체의 속성(변수)값을 클래스의 외부에서 변경하는 것을 안좋아함(은닉성)
# 2.




## ppt 예제 - Line 이라는 클래스 만들어보기 


class Line:
    def __init__(self, length):
        self.length = length
        print(f'{self.length} 길이의 선이 생성되었습니다.')

    def __add__(self, other): # 두 선 길이의 합
        return self.length + other.length

    def compare(self, other): # 짧은 선을 삭제
        if self.length > other.length:
            print(f'길이가 {other.length}인 선이 작다.')
        elif self.length == other.length:
            print('두 선의 길이가 같습니다.')
        else:
            print(f'길이가 {self.length}인 선이 작다.')

    def __del__(self):
        print(f'{self.length} 길이의 선이 제거되었습니다.')


line_a = Line(10)
line_b = Line(5)
print(f'line_a + line_b = {line_a + line_b}')
line_a.compare(line_b)