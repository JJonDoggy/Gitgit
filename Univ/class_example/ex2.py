class Device:
    def __init__(self, name, status=False):
        self.name = name
        self.status = status

    def change_status(self, status):
        self.status = status




class Sensor:
    def __init__(self, name, value=0, status=False):
        self.name = name
        self.value = value
        self.status = status

    def change_status(self, status):
        self.status = status

    def change_value(self, value):
        self.value = value





    # 장치목록과 센서목록은 딕셔너리로
class SmartHome:
    def __init__(self, name, devices={}, sensors={}):
        self.name = name
        self.devices = devices
        self.sensors = sensors

        self.add_device('장치 1')
        self.add_device('장치 2')
        self.add_sensor('센서 1')
        self.add_sensor('센서 2')

    def add_device(self, name):
        d = Device(name)
        self.devices[name] = d
        print(f'장치 [{name}] 이 추가됨.')

    def remove_device(self, name):
        self.devices.pop(name)
        print(f'장치 [{name}]이 제거됨.')

    def add_sensor(self, name):
        s = Sensor(name)
        self.sensors[name] = s
        print(f'센서 [{name}] 추가됨.')

    def remove_sensor(self, name):
        self.sensors.pop(name)
        print(f'센서 [{name}] 제거됨.')

    # 특정 조건에 따라 장치를 자동으로 제어하는 메서드 만들기
    # updateSystem() -> 센서1이 활성 상태이고 값이 50 이상이면 장치 1 켜짐
    # 센서2가 활성 상태이고 값이 30 이하면 장치 2 켜짐

    def updateSystem(self):
        if self.sensors['센서 1'].status and self.sensors['센서 1'].value >= 50:
            self.devices['장치 1'].change_status(True)
        else:
            self.devices['장치 1'].change_status(False)

        if self.sensors['센서 2'].status and self.sensors['센서 2'].value <= 30:
            self.devices['장치 2'].change_status(True)
        else:
            self.devices['장치 2'].change_status(False)


    def display_info(self):
        print(f'센서 1 : 값 - {self.sensors['센서 1'].value}, 활성 상태 - {self.sensors['센서 1'].status}')
        print(f'센서 2 : 값 - {self.sensors['센서 2'].value}, 활성 상태 - {self.sensors['센서 2'].status}')
        print(f'장치 1 : 활성 상태 - {self.devices['장치 1'].status}')
        print(f'장치 2 : 활성 상태 - {self.devices['장치 2'].status}')


sh = SmartHome('우리집')
sh.display_info()

sh.sensors['센서 1'].change_value(60)
sh.sensors['센서 2'].change_value(40)
sh.sensors['센서 1'].change_status(True)
sh.sensors['센서 2'].change_status(True)

print('====================')
sh.display_info()
print('====================')
sh.updateSystem()
sh.display_info()