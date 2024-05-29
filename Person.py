"""
객체 생성을 위한 클래스(class) 정의하기
객체 = 속성(정보, 데이터) + 메소드(정보처리 함수)

인스턴스 = 객체. 클래스.
"""

#===================================================
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.아는사람 = []
        self.tmt = False
    #--------------------------
    def intro(self):
        # 안녕하세요, 저는 홍길동이고 20세입니다.
        print("안녕하세요, 저는 {}이고 {}세입니다.".format(self.name, self.age))

    #--------------------------
    def 측정한키는(self, height):
        self.height = height

        if self.tmt:
            print("제 키는 이제 {}cm이군요.^^".format(self.height))
    #--------------------------
    def 키는얼마니(self):
        if hasattr(self, "height"):
            print("제 키는 {}입니다.".format(self.height))
        else:
            print("저는 모릅니다.")
        
    #--------------------------
    def 인사하기(self, you):
        if you.name in self.아는사람:
            print("또 만나 반갑습니다 {}씨!!".format(you.name))
        else:
            print("안녕하세요 {}씨, 저는 {}입니다.".format(you.name, self.name))
            self.기억하기(you.name)
            you.기억하기(self.name)

    #--------------------------
    def 기억하기(self, name):
        self.아는사람.append(name)

        if self.tmt:
            print("이제 {}는 아는 사람입니다.".format(name))
#===================================================
p1 = Person("홍길동", 20, "남자")
p1.측정한키는(180)
p2 = Person("이순신", 25, "남자")
p2.tmt = True


        
        
