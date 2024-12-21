players = ['one', 'tow', '333', '444', '555']
print(players[1:3])
print(players[:3])
print(players[-3:])
print(players[:-3])
print(players[1:5:2]) # 其中2是步长，注意切片之间是冒号，不仅位置，也包括步长之间
# 通过for循环使用切片，显示位置名称：
for number in players[1:3]:
    print(number.title())
