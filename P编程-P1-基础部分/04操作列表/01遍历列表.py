magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"goog!{magician.title()},very good!\n")
print('thinks!')

foods = ['board', 'cake', 'rice', 'dumpling']
for food in foods:
    print(food.upper())
    print(f'I like {food.title}!\n')
print('haha')

for number in range(5):
    print(number)
# 通过list()函数将数字转换为列表：
numbers = list(range(5))
print(numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)