# 조건문
# 내장함수 -> built-in function
# 형변환 str -> int
number = int(input())
# print(number + 3)

# 스트링으로 변환하려면?
# number = str(number)

# 1. if
if number > 3 :
    print("3초과")
print("????")

# 1-2. 조건 여러개 쓰고 싶어요.
if number > 10:
    print("10초과")
    # 그게 아니라, number가 10 이하, 5초과 일때는 ?
elif 10 >= number > 5 :
    print("애매")
else
    print("5이하")