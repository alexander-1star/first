import random.

class Human:
    def __init__(self, name='human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

brands_of_car = {
    'kama3': {'fuel': 50, 'strength': 300, 'consumption': 2},
    'Me': {'fuel': 180, 'strength': 270, 'consumption': 5},
    'lol': {'fuel': 5, 'strength': 300, 'consumption': 3},
    'Lamburger': {'fuel': 35, 'strength': 90, 'consumption': 6},
    'Mercedes': {'fuel': 35, 'strength': 90, 'consumption': 6}
}

job_list = {
    'Farmer': {'salary': 30, 'gladness_less': 25},
    'Freelancer': {'salary': 35, 'gladness_less': 15},
    'Python dev': {'salary': 50, 'gladness_less': 20},
    'Driver': {'salary': 32, 'gladness_less': 25},
    'Delivery man': {'salary': 40, 'gladness_less': 20}
}


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            return False


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']




    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            self.satiety = min(self.satiety + 5, 100)
            self.home.food -= 5

    def work(self):
        if not self.car.drive():
            if self.car.fuel < 20:
                self.shopping('fuel')
            else:
                self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if not self.car.drive():
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel = 100
        elif manage == 'food':
            print('I bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print("I bought delicacies")
            self.gladness += 30
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 50
        self.home.mess += 15

    def clean_home(self):
        self.gladness -= 10
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def day_indexes(self, day):
        print(f"\n{'=' * 20} Day {day} of {self.name}'s life {'=' * 20}")
        print(f"Money: {self.money}")
        print(f"Gladness: {self.gladness}")
        print(f"Satiety: {self.satiety}")
        if self.car:
            print(f"{self.car.brand} - Fuel: {self.car.fuel}, Strength: {self.car.strength}")
        print(f"House mess: {self.home.mess if self.home else 'N/A'}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression")
            return False
        if self.satiety < 0:
            print("Dead")
            return False
        if self.money < -500:
            print("Bankrupt...")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False

        if self.home is None:
            print("Settling into a house...")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car: {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I got a job as a {self.job.job} with salary {self.job.salary}")

        self.day_indexes(day)
        dice = random.randint(1, 4)

        if self.satiety < 20:
            print("I'm going to eat.")
            self.eat()
            return None
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("Need to clean the house before chilling.")
                self.clean_home()
                return None
            else:
                print("Let's chill.")
                self.chill()
                return None
        elif self.money < 0:
            print("Time to work.")
            self.work()
            return None
        elif self.car.strength < 15:
            print("Need to repair the car.")
            self.to_repair()
            return None
        elif dice == 1:
            print("Let's chill.")
            self.chill()
            return None
        elif dice == 2:
            print("Time to clean the house.")
            self.clean_home()
            return None
        elif dice == 3:
            print("Let's buy some delicacies.")
            self.shopping('delicasies')
            return None
        return None

jim = Human(name='Jim')
for day in range (1,8):
    if jim.live(day) == False :
        break