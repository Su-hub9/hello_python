# 마무리 확인문제 4
list_of_list = [
    [1, 2, 3], 
    [4, 5, 6, 7], 
    [8, 9]
]

for list in list_of_list:
    for number in list:
        print(number)

# 마무리 확인문제 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number - 1) % 3].append(number)

print(output)