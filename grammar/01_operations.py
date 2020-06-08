# 논리 연산자
# and, or, not
print("___and___")
print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("___or___")
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print("___not___")
print(not True)
print(not [])

# in, not in
print("___in___")
print("a" in "apple")
print(1 not in [1, 2, 3])

# 단축 평가
# ""가 False "Text"가 True이기 때문에 or문이 끝나서 그 다음은 연산하지 않는다.
print("" or "Text" or "Text_2")
# ""가 False "Text"가 True이기 때문에 and문을 만족하지 못하고 다음 or문을 검사해 "Text_2"가 출력된다.
print("Text" and "" or "Text_2")