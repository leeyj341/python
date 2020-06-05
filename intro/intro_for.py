# 반복문 종류 2개
# 1. while
# while 문은 어떤 구간이 정해져 있지 않고, 무한대로?
# n = 0
# while(n < 3) :
#     print(n)
#     n += 1

n = 0
while(n < 3) :
    n += 1
    print(n)
print(n)
# 1 2 3 3

# 2. for
number = list(range(10))
print(number)

# number = list(range(3, 10))
# print(number)

# number = list(range(3, 10, 2))
# print(number)

for num in range(30) :
    print(num)

# 2-1. list for
for num in number :
    print(num)

# 2-2. idx로 접근하고 싶어요...
number = ["삼성", "역삼", "선릉", "영등포"]
for i in range(len(number)) :
    print(i)
    print(number[i])

# 2-3. enumerate
for idx, i in enumerate(number) :
    print(idx, i)

# 3. dictionary
mask = {
    "삼성" : 100,
    "역삼" : "50개",
    "선릉" : True
}

for i in mask :
    print(i)

print("*" * 30)

# 동작은 위 코드와 동일하나, dict라는 걸 표현하기 위함
for i in mask.keys() :
    print(i)

for val in mask.values() :
    print(val)

print("*" * 30)
for key, val in mask.items() :
    print(key, val)
    print(mask[key])

for idx, i in enumerate(mask, 3) :
    print(idx, i)