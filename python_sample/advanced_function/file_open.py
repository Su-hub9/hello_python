# 파일을 엽니다.
file = open("./basic.txt", "w")

# 파일을 텍스트를 씁니다.
file.write("Hello Python Programming...!")

# 파일을 닫습니다.
file.close()

# with 키워드 사용
# 파일을 엽니다.
with open("basic2.txt", "w") as file:
    # 파일에 텍스트를 씁니다.
    file.write("Hello Python Programming...!2")