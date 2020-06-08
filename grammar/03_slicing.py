sample_list = list(range(31))
print(sample_list)
print(sample_list[3])
print(sample_list[3:24])
print(sample_list[5:-1])
print(sample_list[5:])
# 3부터 sample_list의 길이만큼, 2단계씩 뛰어서 출력하겠다
print(sample_list[3:len(sample_list):2])

# 생략하기
# 비워두면 끝까지 출력하겠다는 의미
print(sample_list[:13:2])
# 뒤에서부터 전체 다 출력
print(sample_list[::-1])
