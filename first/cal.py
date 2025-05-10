import random

class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 1:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage: object) -> None:
        if self.car.fuel < 1:
            manage = 'fuel'
        else:
            self.to_repair()
            return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 50
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food')
            self.money -= 20
            self.home.food += 50
        elif manage == 'delicious':
            print('Mmmm... It is delicious!')
            self.gladness += 20
            self.satiety += 5
            self.money -= 15

    def chill(self):
        self.gladness += 50
        self.home.mess += 10

    def clean_home(self):
        self.gladness -= 10
        self.home.mess = 0

    def to_repair(self):
        self.money -= 35
        self.car.strength += 100

    def days_indexes(self, day):
        day = f' Today is {day} of {self.name} life'
        print(f'{day:=^50}', '\n')
        human_indexes = self.name + ' index'
        print(f'{human_indexes:=^50}', '\n')
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print(f'Gladness - {self.gladness}')
        home_indexes = 'Home index'
        print(f'{home_indexes:=^50}', '\n')
        print(f'Food - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        car_indexes = f'{self.car.brand} car index'
        print(f'{car_indexes:=^50}', '\n')
        print(f'Fuel - {self.car.fuel}')
        print(f'Strength - {self.car.strength}')

    def is_alive(self):
        if self.gladness < 0:
            print('Depression...')
        if self.satiety < 0:
            print('Hungry')
        if self.money < -100:
            print('Poor')
            return False
        return None

    # noinspection PyUnresolvedReferences
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Settled in the house')
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f'I bought a car {self.car.brand}')
        if self.job is None:
            self.get_job()
            print(f'I have a job {self.job.job} with salary {self.job.salary}')
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print('I go eat')
            self.eat()
            return None
        elif self.gladness < 20:
            if self.home.mess > 15:
                print('I will clean the home')
                self.clean_home()
                return None
            else:
                print('Let chill')
                self.chill()
                return None
        elif self.money < 0:
            print('Start working')
            self.work()
            return None
        elif self.car.strength < 15:
            print('I need to repair the car')
            self.to_repair()
            return None
        elif dice == 1:
            print('Let chill')
            self.chill()
            return None
        elif dice == 2:
            print('Start working')
            self.work()
            return None
        elif dice == 3:
            print('Let clean the home')
            self.clean_home()
            return None
        elif dice == 4:
            print('Let shopping')
            self.shopping(manage='delicious')
            return None
        return None


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumtion = brand_list[self.brand]['consumtion']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumtion:
            self.fuel -= self.consumtion
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


job_list = {
    'AutoMechanic': {'salary': 200, 'gladness_less': 30},
    'McDonald': {'salary': 50, 'gladness_less': 50},
    'Taxi': {'salary': 200, 'gladness_less': 35},
    'Chef': {'salary': 300, 'gladness_less': 10},
    'Office': {'salary': 500, 'gladness_less': 60},
    'Teacher': {'salary': 150, 'gladness_less': 40},
}

brands_of_car = {
    'Mazda': {'fuel': 2, 'strength': 260, 'consumtion': 1},
    'BMW': {'fuel': 5, 'strength': 320, 'consumtion': 4},
    'Toyota': {'fuel': 5, 'strength': 480, 'consumtion': 6},
    'Mersedes': {'fuel': 3, 'strength': 286, 'consumtion': 3},
    'Zhiguli': {'fuel': 10, 'strength': 86, 'consumtion': 15},
}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

Jim = Human(name='Nick')
for day in range(1, 8):
    if not Jim.live(day):
        break
