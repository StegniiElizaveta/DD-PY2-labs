if __name__ == "__main__":
    # Write your solution here
    class Human:
        def __init__(self, name: str, age: int, height: float, weight: float):
            self.name = name
            self.age = age
            self.height = height
            self.weight = weight

        def __str__(self):
            return f"Человек по имени {self.name}, возраст:{self.age} , рост: {self.height} см, вес: {self.weight} кг. "

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}), height={self.height!r}, weight={self.weight!r})"

    class Man(Human):
        def __init__(self, name: str, age: int, height: float, weight: float):
            super().__init__()
            self._sex_chromosomes = "ХY"

        @property
        def sex_chromosomes(self):
            return self._sex_chromosomes
        '''Если человек отнесен к определенному классу мужчина/женщина, нельзя редактировать атрибут, отвечающий за половые хромосомы'''

        def __str__(self):
            return f"Мужчина по имени {self.name}, возраст:{self.age} , рост: {self.height} см, вес: {self.weight} кг. "

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}), height={self.height!r}, weight={self.weight!r})"


    class Woman(Human):
        def __init__(self, name: str, age: int, height: float, weight: float):
            super().__init__()
            self._sex_chromosomes = "ХX"

        @property
        def sex_chromosomes(self):
            return self._sex_chromosomes
        '''Если человек отнесен к определенному классу мужчина/женщина, нельзя редактировать атрибут, отвечающий за половые хромосомы'''

        def __str__(self):
            return f"Женщина по имени {self.name}, возраст:{self.age} , рост: {self.height} см, вес: {self.weight} кг. "

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}), height={self.height!r}, weight={self.weight!r})"



    class Building:
        def __init__(self, height: float, length: float, width: float):
            self.height = height
            self.length = length
            self.width = width

        def __str__(self):
            return f"Здание высотой {self.height} м, длина в плане {self.length} м, ширина в плане {self.width} м. "

        def __repr__(self):
            return f"{self.__class__.__name__}(height={self.height!r}, length={self.length!r}), width={self.width!r})"



    class IndustrialBuilding (Building):

        def __init__(self, height: float, length: float, width: float, industry: str, equipment: str):
            super().__init__()
            self.industry = industry
            self.equipment = equipment

        def __str__(self):
            return f"Промышленное здание высотой {self.height} м, длина в плане {self.length} м, ширина в плане {self.width} м. "

        def __repr__(self):
            return f"{self.__class__.__name__}(height={self.height!r}, length={self.length!r}), width={self.width!r})"


    class CivilBuilding(Building):
        def __init__(self, height: float, length: float, width: float, class_of_building: str):
            super().__init__()
            self.class_of_building = class_of_building

        def __str__(self):
            return f"Гражданское здание высотой {self.height} м, длина в плане {self.length} м, ширина в плане {self.width} м. "

        def __repr__(self):
            return f"{self.__class__.__name__}(height={self.height!r}, length={self.length!r}), width={self.width!r})"





    class VolleyballPlayer:
        def __init__(self, name: str,  gender: str, age: int, height: float, weight: float, country: str, team: str, awards: list, serving_points: int):
            self.name = name
            self.age = age
            self.height = height
            self.weight = weight
            self.country = country
            self.gender = gender
            self.team = team
            self.awards = awards
            self.serving_points = serving_points

        def __str__(self):
            return f"Игрок по имени {self.name}, пол: {self.gender},  возраст:{self.age}, рост: {self.height} см, вес: {self.weight} кг, страна: {self.country}."

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}), height={self.height!r}, weight={self.weight!r}, gender={self.gender!r}, country={self.country!r})"

        def give_an_award(self, award_name: str):
            '''Метод, позволяющий расширить список присужденных игроку номинаций и наград'''
            self.awards = self.awards + list(award_name)


        def change_team(self, team_name):
            '''Метод для замены команды игрока'''
            self.team = team_name

        def add_serving_points(self, gained_points):
            '''Метод, позволяющий добавить очки, заработанные на подаче'''
            self.serving_points += gained_points

    class OutsideHitter(VolleyballPlayer):
        def __init__(self, name: str, age: float, height: float, weight: float, points_from_attacking: int, errors: int, attempts: int):
            self.points_from_attacking = points_from_attacking
            self.errors = errors
            self.attempts = attempts

        def add_points_from_attacking(self, gained_points):
            '''Метод, позволяющий добавить очки, заработанные в нападении'''
            self.points_from_attacking += gained_points

        def add_errors(self, gained_errors):
            '''Метод, позволяющий добавить ошибки'''
            self.errors += gained_errors

        super().__str__()

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}), height={self.height!r}, weight={self.weight!r})"


    class MiddleBlocker(VolleyballPlayer):
        def __init__(self, name: str, age: float, height: float, weight: float, blocks: int, errors: int, rebounds: int):
            self.blocks = blocks
            self.errors = errors
            self.rebounds = rebounds

        def add_blocks(self, gained_points):
            '''Метод, позволяющий добавить очки, заработанные на блоке'''
            self.blocks += gained_points

        def add_errors(self, gained_errors):
            '''Метод, позволяющий добавить ошибки'''
            self.errors += gained_errors

        def add_rebounds(self, gained_rebounds):
            '''Метод, позволяющий увеличить количество блоков, не забивших очко, но оставивших мяч на стороне соперника'''
            self.rebounds += gained_rebounds

        super().__str__()

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}), height={self.height!r}, weight={self.weight!r})"

        class OppositeHitter(VolleyballPlayer):
            def __init__(self, name: str, age: float, height: float, weight: float, points_from_attacking: int, errors: int, attempts: int):
                self.points_from_attacking = points_from_attacking
                self.errors = errors
                self.attempts = attempts

        def add_points_from_attacking(self, gained_points):
            '''Метод, позволяющий добавить очки, заработанные в нападении'''
            self.points_from_attacking += gained_points

        def add_errors(self, gained_errors):
            '''Метод, позволяющий добавить ошибки'''
            self.errors += gained_errors

        super().__str__()

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}), height={self.height!r}, weight={self.weight!r})"

        class Setter(VolleyballPlayer):
            def __init__(self, name: str, age: float, height: float, weight: float, successfull_settings: int, errors: int, attempts: int)
                self.successfull_settings = successfull_settings
                self.errors = errors
                self.attempts = attempts

            def add_successfull_settings(self, new_settings):
                '''Метод, позволяющий увеличить число успешных передач'''
                self.successfull_settings += new_settings

            def add_errors(self, gained_errors):
                '''Метод, позволяющий добавить ошибки'''
                self.errors += gained_errors

            super().__str__()

            def __repr__(self):
                return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}), height={self.height!r}, weight={self.weight!r})"

        class Libero(VolleyballPlayer):
            def __init__(self, name: str, age: float, height: float, weight: float, digs: int, successful_receives: int, errors: int, attempts: int):
                self.digs = digs
                self.successful_receives = successful_receives
                self.errors = errors
                self.attempts = attempts

            def add_successfull_receives(self, new_receives):
                '''Метод, позволяющий увеличить число результативных приемов'''
                self.successfull_settings += new_settings

            def add_errors(self, gained_errors):
                '''Метод, позволяющий добавить ошибки'''
                self.errors += gained_errors

            def add_successfull_digs(self, new_receives):
                '''Метод, позволяющий увеличить число результативных действий в защите'''
                self.successfull_digs += new_digs

            super().__str__()

            def __repr__(self):
                return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r}), height={self.height!r}, weight={self.weight!r})"

