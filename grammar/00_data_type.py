import sys
max_num = sys.maxsize
print(max_num)
super_max = max_num * max_num
print(super_max)
print(type(super_max))

# 프로그래밍 언어의 기본 3가지
# 1. 변수 저장
number = 10
string = '10'
boolean = False
# 파이썬에는 값이 없다는 뜻인 None 타입이 존재
nothing = None
print(number, string, boolean, nothing)
print(type(nothing))

# 1-1. 정수형
number = 10
float_num = 1.3
complex_num = (3 + 3j)
print(type(number), type(float_num), type(complex_num))


# 2. bool
print(type(True))
print(type(False))
# 0, 0.0, [], {}
print(False == 0)

# 3. 문자형
# '', ""
# ''로 작성했으면 끝까지 ''로
greeting = 'hi'
name = "kim"
print(greeting, name) 

# 문자열 입력 받기
# input()
# age = input("나이를 입력해 주세요. : ")
# print(type(age))
# print(type(int(age)))

# string interpolation
name = "kim"
print("안녕하세요, ", name)
print("{}, {}".format(greeting, name))
print(f"{greeting}, {name}")

# 연산과 출력 형태 지정
pi = 3.141592
print(f"원주율은 {pi:.4}, 반지름 = 2 원의 넓이는 {pi * 2 * 2}")