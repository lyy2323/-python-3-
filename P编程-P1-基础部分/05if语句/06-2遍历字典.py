language = {'dog': '狗',
            'food': '食物',
            'foot': '脚',
            'bottle':'bottle-瓶子'
            }
friends = ['dog', 'foot', 'bottle']
for name in language.keys():
    print(f'Hi {name.title()}')

    if name in friends:
        languages = language[name].title()
        print(f'\t{name.title()}, I see you love {languages}')
