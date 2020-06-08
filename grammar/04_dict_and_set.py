# 1. dictionary
# key, value로 이루어져 있음
dict_a = {}
dict_b = dict()
# key 중복은 불가능
dict_a = {
    "삼성" : 100,
    "역삼" : 50,
    "삼성" : 30,
}
# 같은 키가 두개면 오류는 나지 않지만 마지막에 사용한 키의 value만 호출이 된다.
print(dict_a)

print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

print(dict_a["삼성"])
print(dict_a.get("삼성"))

# .get과 [] 접근 차이점
dict_a = { "삼성" : 100, "역삼" : 50 }
# 해당 키가 없으면 None을 리턴한다.
print(dict_a.get("선릉"))
# 해당 키가 없으면 오류가 발생한다.
# print(dict_a["선릉"])

# 2. set
# set는 순서가 없이 저장된다.
# key값이 없고 중복이 없다.
set_a = {1, 2, 3}
set_b = {} # 이렇게 만들 경우 빈 dictionary가 생성된다.
set_b = set() # 이렇게 생성해야 함.
set_b = {3, 6, 8}
print(set_a - set_b) # 집합처럼 사용 가능
print(set_a | set_b) # 합집합
print(set_a & set_b) # 교집합

list_a = [1, 1, 1, 1]
print(list(set(list_a))[0])

string = "immutable"
list_a = ["immutable?", "real?"]

print(string[0])
print(list_a[0])
# 한 번 정해진 string 값은 변환할 수 없다.
# string[0] = "a" 
list_a[0] = "mutable"
print(list_a)

# mutable
list_a = ["immutable?", "real?"]
list_b = list_a
print(list_a, list_b)
list_b[0] = "mutable"
print(list_a, list_b)

# immutable
string_a = "a"
string_b = string_a
string_b = "b"
print(string_a, string_b)