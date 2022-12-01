import random


class person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'({self.name!r},{self.surname})'


persons = [person('JAn', 'Kowalski'),
         person('Wojciech', 'Długosz'),
         person('Wacław', 'King'),
         person('Ali','Halib-Dar'),
         ]

def add_data(a: float,b: float,h: float):
    '''obliczamy pole trapezu'''
    '''parametr wyłapujący bład'''
    try:
        pole = ((a + b) * h) / 2
    except Exception as e:
        print("zostały wprowadzone niprawidłowe wartości:", e.args)
        return 0
    else:
        return pole

def wielkosc(pole):
    if pole <=10:
        wymiar = 'A'
    elif pole >10 and pole <=30:
        wymiar = 'B'
    elif pole >30 and pole <=50:
        wymiar = 'C'
    else:
        wymiar = 'D'
    return wymiar

persons.sort(key=lambda x: x.surname)
pole_trapezu = add_data(3.15,20,12)
wymiar = wielkosc(pole_trapezu)
random_person = random.choice(persons)
print("Lista kandydatów do działki:  ", repr(persons))
print("Zwyciezcą konkursu na działkę o powieżchni: " + str(pole_trapezu) + ' i symbolu wielkości: ' + str(wymiar) + " Zostaje...: " + str(random_person))
