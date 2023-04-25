#Person 클래스 (맨 앞글자 대문자)
class Person:
    def __init__(self, name, age):  # 생성자 (함수)
        self.name = name
        self.age = age

    # 멤버의 정보
    def __str__(self):
        return f'이름: {self.name}, 나이: {self.age}'

# 상속 - 클래스 이름(부모 클래스) = Employee(Person)
class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age) # 부모 클래스의 멤버 상속
        self.id = id    # 자식 클래스 사번 초기화

    # 메서드 재정의(오버라이딩)
    def __str__(self):
        #return f'이름: {self.name}, 나이: {self.age}, 사번: {self.id}'
        return f' {super().__str__()}, 사번: {self.id}'

    def work(self):
        print("회사에 다닌다.")

e1 = Employee("이하나", 25, "a1001")
print(e1)
e1.work()

e2 = Employee

# 클래스 사용 - 객체 생성(메모리 실행)
# p1 - 인스턴스, 오브젝트
p1 = Person("김산", 21)
# print(p1.name)
# print(p1.age)
# __str__(self)함수 사용 시
print(p1)

p2 = Person("이강", 30)
# print(p2.name)
# print(p2.age)
# __str__(self)함수 사용 시
print(p2)