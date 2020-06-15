class Person :      # 클래스 객체 생성(클래스 정의)
    name = "이름이란, 사람이 공통적으로 가지는 속성"
    age = "나이란, 내가 태어나서 죽을때까지 기간"

    def greeting(self) :
        return f"{self.name}이(가) 인사합니다. 안녕하세요!"

    def aging(self) :
        return f"{self.name}은(는) {self.age}살 입니다."

    @classmethod    # 자바에서 static method와 같은 역할
    def age_means(cls) :
        return f"{cls.name}은 나라마다 다르다."

p1 = Person()
print(p1.name)
print(p1.age)
p1.name = "이영주"
p1.age = "28"
print(p1.greeting())
print(p1.aging())
print(Person.age_means())
print(p1.age_means())
