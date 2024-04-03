"""
객체 생성을 위한 클래스(class) 정의하기
객체 = 속성(정보, 데이터) + 메소드(정보처리 함수)
인스턴스 = 객체. 클래스.
"""

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.아는사람 = []
        self.tmt = False
    #------------------------
    def intro(self):
        #안녕하세요, 저는 정진우이고 24세입니다.
        print("안녕하세요, 저는 {}이고 {}입니다.".format(self.name, self.age))

    def 측정한키는(self, height):
        self.height = height

        if self.tmt:
            print("제 키는 이제 {}cm입니다.".format(self.height))

    def 키는얼마니(self):
        if hasattr(self, "height"):
            print("제 키는 {}입니다.".format(self.height))
        else:
            print("저는 제 키를 몰라요;;")

    def 인사하기(self, you):
        if(you.name in self.아는사람):
            print("반갑습니다 {} 씨!".format(you.name))
        else:
            print("안녕하세요 {} 씨, 저는 {}입니다.".format(you.name, self.name))
            self.기억하기(you.name)
            you.기억하기(self.name)
        
        
    def 기억하기(self, name):
        if self.tmt:
            self.아는사람.append(name)
            print("이제 {} 씨는 아는 사람입니다.".format(name))
        
        
p1 = Person("정진우", 24, "남자")
p1.측정한키는(180)
p2 = Person("이순신", "불멸", "남자")
p2.tmt = True


"""
3번 이상 만나면 인사말 바꾸기
"""
