class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_list = []
print('Введите поочереди числовые элементы списка. Для завершения ввода введите stop.')
while True:
    inp = input()
    if inp == 'stop':
        break
    try:
        el = int(inp)
    except ValueError:
        print('Зачем ввели буквы. Элементы списка должны быть числами')
    else:
        inp_list.append(el)

print(f'Сформированный список: {inp_list}')