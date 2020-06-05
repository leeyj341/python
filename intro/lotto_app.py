from lt import lottos

pick = lottos.lotto(1000) 
print(pick)

# 1. 만약 4등 한 적이 있으면
# 2. 4등 "몇 번" 했습니다.
result = pick["4th"]
if result > 0 :
    print(f"4등 {result} 번 했습니다.")

strResult = lottos.lotto("100000")
print(strResult)

