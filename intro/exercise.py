# 1. 로또번호 추첨하는데 5번 한 번에
import random

for i in range(5) :
    lotto = sorted(random.sample(range(1, 46), 6))
    print(lotto)

# comprehension
lotto = [sorted(random.sample(range(1, 46), 6)) for i in range(5)]
print(lotto)

# 2. 음식점 이름, 전화번호인 딕셔너리
# 2-1. 그중에서 무작위 음식점 하나 뽑아서
# 2-2. 가게이름이랑 전화번호 출력

dic = {
    "엽기 떡볶이" : "02-111-1111",
    "반장 떡볶이" : "02-222-2222",
    "신전 떡볶이" : "02-333-3333",
    "국대 떡볶이" : "02-444-4444"
}
# 그냥 keys()를 사용하면 반환하는 형태가 list가 아니기 때문에 형변환이 필요하다.
pick = random.choice(list(dic.keys()))
print(pick, dic[pick])

# pick = random.choice(list(dic.items()))
# print(pick)

# f-string (formatting)
print(f"가게이름은 {pick}, 전화번호는 {dic[pick]}")
