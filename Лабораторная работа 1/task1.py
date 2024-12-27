# TODO Написать 3 класса с документацией и аннотацией типов

import doctest

class Cat:
    def __init__(self, name: str, age: int, owner: str):
        '''Создаем кота с именем, возрастом и хозяином'''

        if not isinstance(name, str):
            raise TypeError('Дайте коту нормальное имя!')
        self.name = name
        if not isinstance(age, int):
            raise TypeError('Возраст кота должен иметь целочисленное значение')
        if age <= 0:
            raise ValueError('Возраст кота должен быть положительным!')
        self.age = age
        if not isinstance(owner, str):
            raise TypeError('Введите корректно имя хозяина')
        self.owner = owner

        def change_owner(self, new_owner):
            '''Меняем имя владельца кота

            Пример:
            >>> barsik = Cat(Barsik, 3, Max)
            >>> barsik.change_owner(Julia)

            :return: Поменяли владельца кота - Юлия вместо Макса'''

            if not isinstance(new_owner, str):
                raise TypeError('Введите корректно имя хозяина')
            self.owner = new_owner

        def increase_age(self):
            '''Делаем кота на год старше
            Пример:
            >>> barsik = Cat(Barsik, 3, Max)
            >>> barsik.increase_age()

            :return: Теперь Барсику 4 года'''

            self.age += 1


class VolleyballPlayer:
    '''Создаем профиль игрока, содержащий имя, возраст, кназвание команды, номер и амплуа'''

    def __init__(self, name: str, age: int, team: str, number: int, position: str):
        if not isinstance(name, str):
            raise TypeError('Введите корректно имя игрока')
        self.name = name
        if not isinstance(age, int):
            raise TypeError('Возраст игрока должен быть целым числом')
        if age <= 0:
            raise ValueError('Введите корректный возраст игрока')
        self.age = age
        if not isinstance(team, str):
            raise TypeError('Название команды должно иметь тип данных "строка"')
        self.team = team
        if not isinstance(number, int):
            raise TypeError ('Введите корректно номер игрока')
        if number <= 0:
            raise ValueError('Введите корректно номер игрока')
        self.number = number
        if not isinstance(position, str):
            raise TypeError('Амплуа игрока должно иметь тип данных "строка"')
        self.position = position

        def change_position(self, new_position):
            '''Меняем амплуа игрока
            Пример:
            >>> egonu = VolleyballPlayer(Paola Egonu, 26, Italy, 18, diagonal)
            >>> egonu.change_position(outside hitter)

            :return: Поменяли амплуа - доигровщик вместо диагонального'''

            if not isinstance(new_position, str):
                raise TypeError('Амплуа игрока должно иметь тип данных "строка"')
            self.position = new_position

        def change_number(self, new_number):
            '''Меняем номер игрока
            Пример:
            >>> egonu = VolleyballPlayer(Paola Egonu, 26, Italy, 18, diagonal)
            >>> egonu.change_number(20)

            :return: Поменяли номер игрока с 18 на 20'''

            if not isinstance(new_number, int):
                raise TypeError('Введите корректно номер игрока')
            if new_number <= 0:
                raise ValueError('Введите корректно номер игрока')
            self.number = new_number

        def change_team(self, new_team):
            '''Меняем команду игрока
            Пример:
            >>> egonu = VolleyballPlayer(Paola Egonu, 26, Italy, 18, diagonal)
            >>> egonu.change_team(USA))

            :return: Перевели из сборной Италии в сборную США'''

            if not isinstance(new_team, str):
                raise TypeError('Название команды должно иметь тип данных "строка"')
            self.team = new_team

        def increase_age(self):
            '''Увеличиваем на год возраст игрока'''
            self.age += 1

class Holiday:
    '''Создаем праздник, который хранит своё название в строке и дату в кортеже'''
    def __init__(self, name: str, month: str, day: int):
        if not isinstance(name, str):
            raise TypeError('Название праздника должно иметь тип данных "строка"')
        self.name = name
        if not isinstance(day, int):
            raise TypeError ('Введите корректно дату')
        if not isinstance(month, str):
            raise TypeError ('Введите название месяца строкой')
        if day < 1 or day > 31:
            raise ValueError('Введите корректно день')
        self.date = (month, day)
        # Мне лень проверять по отдельности количество дней в каждом месяце...
        # Так что теоретически я допускаю 31 февраля.

        def celebrate(self):
            '''Желаем счастливого праздника. Пример: Happy Easter!
            Работает только в английском эквиваленте, так как в
            английском при склонении существительные не изменяются.
            По-хорошему, можно доработать, добавив Merry для случая Christmas
            и подумать о других исключениях

            Пример:
            >>> easter = (Easter,April,20)
            >>> easter.celebrate()

            :return: Happy Easter!

            '''
            print(f"Happy {self.name}!")

        def change_name(self, new_name):
            '''Меняем имя праздника
             Пример:
            >>> easter = (Easter,April,20)
            >>> easter.change_name(EggDay)

            :return: Поменяли имя Пасха на День Яиц'''

            if not isinstance(new_name, str):
                raise TypeError('Название праздника должно иметь тип данных "строка"')
            self.name = new_name

#В документации методов я не описываю, за что отвечают аргументы, потому
# что там всё кристалльно ясно.

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

