import random
from selectors import SelectSelector


class Human:
    def __init__(self, name='human', job=None,home= None, car=None):
        self.name = name
        self.money = 10
        self.gladness_less = 50
        self.car = car
        self.satiety = 50
        self.job = job
        self.home = home

def get_home(self):
    self.home = House()

def get_car(self):
    self.car= Auto(brands_of_car)



def get_job(self):
    if self.car.drive():
        pass
    else:
        self.to_repair()
        return
    self.job = Job(job_list)

def eat(self):
    if self.home.food <=0:
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
        if self.car.fuel < 20:
           self.shopping('fuel')
        return
        else:
           self.to_repair()
           return
     self.money += self.job.salary
     self.gladness -= self.job.gladness_less
     self satiety-=4

def shopping(self,manage):
    if self.car.drive():
      pass
    else:
        if self.car.fuel<20:
            manage = 'fuel'
        else:
            self.to.repair()
            return
    if manage == 'fuel':
        print('I bought fuel')
        self.money -= 100
        self.car.fuel = 100
    elif manage == 'food':
        print('I bought food')
        self.money -=50
        self.home.food +=50
    elif manage == 'delicasies':
        self.gladness += 30
        self.satiety +=2
        self.money -= 15

def chill(self):
    self.gladness += 50
    self.home.mess += 15

def clean_home(self):
    self.gladness -=10
    self.home.mess = 0

def to_repair(self):
    self.car.strenght += 100
    self.money -= 50

def day_indexes(self,day):
    day = f'Today is the{day} of {self.name} life'
    print(f'{day:=¬50}','\n')
    human_indexes = self.name = 'indexes'
    print(f'{human_indexes:=¬50}','\n')
    print(f'money - {self.money}')
    print(f'Gladness - {self.satiety}')
    print(f'Satiety - {self.satiety}')
    car_indexes = f'{self.car.brand}car indexes'
    print(f' {car_indexes:==¬50}')

def is_alive(self):
    pass

def live(self,day):
    pass

class Auto:
   def __init__(self,brand_list):
    self.brand= random.choice(list(brand_list))
    self.fuel= brand_list[self.brand]['fuel']
    self.strength = brand_list[self.brand]['strength']
    self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        pass

    class House:
        def __init__(self):
            self.mess = 0
            self.food=0



brands_of_car = {
       'kama3':{'fuel':50,'strength':300,'consumption':2},
       'Me':{'fuel':180,'strength':270,'consumption':5},
      'lol':{'fuel':5,'strength':300,'consumption':3},
     'Lamburger':{'fuel':35,'strength':90,'consumption':6},
      'Mercedes':{'fuel':35,'strength':90,'consumption':6}}

job_list = {
    'Farmer':{'salary':30 ,'gladness_less': 25},
    'Freelancer':{'salary':35 ,'gladness_less': 15},
    'Python dev':{'salary':50, 'gladness_less': 20},
    'driver':{'salary':32,'gladness_less': 25},
    'Delivery man ':{'salary':40,'gladness_less': 20}}

class Job:
     def __init__(self,job_list):
            self.job = random.choice(list(job_list))
            self.salary= job_list[self.job]['salary']
            self.gladness_less= job_list[self.job]['gladness_less']

