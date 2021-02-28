class Date:
    @classmethod
    def int_date(cls, date):
        date = date.replace('-', '')
        return f'{int(date[:2]):02}.{int(date[2:4]):02}.{int(date[4:])}'

    @staticmethod
    def validating(date):
        try:
            date = date.replace('-', '')
            if int(date[:2]) not in range(1, 32) or int(date[2:4]) not in range(1, 13):
                raise ValueError('ValueError')
            else:
                return f'Допустимый формат даты'
        except ValueError as error:
            print(f'Ошибка {error}: не верно ввели формат даты, где то ошиблись')


print(Date.validating('27-02-2021'))
print(Date.int_date('27-02-2021'))