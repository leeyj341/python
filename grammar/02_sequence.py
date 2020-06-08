# ctrl + 1 현재 편집 중인 코드파일
# ctrl + ` 현재 떠있는 터미널 창

# 02_sequence.py
# 데이터가 순차적으로 나열이 되어있다. 정렬 되어있다는 뜻은 아님.
# list, tuple, range, string
# 1. list
list_a = []
list_b = list()
list_a = ["삼성", 23, True]
# 1-1. idx로 접근하기
print(list_a[0])
print(list_a[-1])

# 2. tuple
tuple_a = ()
tuple_a = (1, 2) # tuple()로는 생성이 불가
print(tuple_a)
# 값을 하나만 넣고자 한다면
tuple_b = (1,) # list와 달리 ,를 꼭 넣어야 한다.
tuple_c = (1)
print(type(tuple_b))
print(type(tuple_c))

# 3. range
print(range(10))
print(type(range(10)))
print(list(range(10)))
print(list(range(3, 10, 2)))