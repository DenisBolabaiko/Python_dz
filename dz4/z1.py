list_ = [x ** 2 for x in range(1, 11)]
print(f'пункт 1 :{list_}')
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
dictionary = {day: i + 1 for i, day in enumerate(days)}
print(f'пункт 2 :{dictionary}')
tags = ['Django', 'FastAPI', 'Numpy', 'PYTHON', 'Pandas', 'FASTAPI', 'Python', 'random']
tags_set = {tag.lower() for tag in tags}
print(f'пункт 3 :{tags_set}')
