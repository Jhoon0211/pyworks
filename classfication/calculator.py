# Calculator 클래스

class Calculator:
    def __init__(self):
        self.x = 0  # 멤버변수 x에 0을 할당

    # 매개변수 y값 더하기
    def add(self, y):
        self.x = self.x + y
        return self.x

    # 매개변수 y값 빼기
    def sub(self, y):
        self.x = self.x - y
        return self.x

    # 매개변수 y값 빼기
    def sub(self, z):
        self.x = self.x - z
        return self.x

cal1 = Calculator()
print('더한 값 :', cal1.add(10))
print('뺀 값 :', cal1.sub(4))

cal2 = Calculator()
print('더한 값 :', cal2.add(10.1))
print('뺀 값 :', cal2.sub(2.5))

