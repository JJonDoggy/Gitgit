# 클래스 상속

class Rabbit:
    def __init__(self, color, x=0, y=0):
        self.color = color
        self.xPos = x
        self.yPos = y
        print('rabbit 생성자 호출')

    def goto(self, x, y):
        print('rabbit의 goto 메소드 실행..')
        self.xPos = x
        self.yPos = y

    def __str__(self):         # 출력값 설정 (print 썼을 때 어떻게 출력 되는 지 설정)
        return f'색상 - {self.color}, 위치 - ({self.xPos}, {self.yPos})'


class HouseRabbit(Rabbit):
    def __init__(self, color, owner, x=0, y=0):
        # 부모 클래스의 생성자를 이용해서 부모로부터 상속받는 속성을 초기화
        super().__init__(color, x, y)
        self.owner = owner
        print('houserabbit 생성자 호출')

    def eat_feed(self):
        print(f'집토끼가 먹이를 먹습니다')

    def goto(self, x, y):
        print('houserabbit의 goto 메소드 실행..') # 자식클래스에서 부모클래스에 정의된 메서드와 같은 이름의 메서드를 재정의하는 것
        self.xPos = x + 100                    # ==> 메서드 오버라이딩(overriding)
        self.yPos = y + 100

    def __str__(self):         # 출력값 설정 (print 썼을 때 어떻게 출력 되는 지 설정)
        return f'색상 - {self.color}, 위치 - ({self.xPos}, {self.yPos}, 소유자 - {self.owner})'

r2 = HouseRabbit('빨강', 30, 70)
r2.owner = '컴공'
r2.eat_feed()
print(f'r2 - {r2}')
print(r2.owner)


# 중요한 것
# super - 부모클래스에 정의되있는 것을 사용할때..
# 메소드 오버라이딩 - 자식 클래스만의 메소드
