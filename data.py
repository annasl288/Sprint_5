from random import randint

class Person:
    NAME = 'Анна'
    EMAIL = 'annaslobodyanyuk14a111@ya.ru'
    PASSWORD = 'qwerty'

class RandomPerson:
    NAME = 'Анна_тест'
    EMAIL = f'annaslobodyanyuk14a{randint(0, 999)}@ya.ru'
    PASSWORD = str(randint(100000, 999999))