print("Hello, World!")

# 저장, 조건, 반복
# ctrl + / : 주석 걸기

# 1. 저장
number = 10
string = "10"
boolean = True

print(number, string, boolean)

# 2. 리스트 저장
arr = [number, string, boolean]
arr2 = [10, "10", True, number]
print(arr2)

# 2-1. 인덱스로 접근하기
print(arr2[0], arr2[1], arr2[2])
# 2-2. 자료형 출력하기
print(type(arr2[0]), type(arr2[1]))

# 3. dictionary
mask = {
    "삼성" : 100,
    "역삼" : 50,
    "선릉" : 30,
    "영등포" : 10
}
print(mask)
print(mask["삼성"])