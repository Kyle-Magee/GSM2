from datetime import timedelta
# Working on setting max hours for Part time workers


class Employee:
    """De-facto employee characteristic tree. Contains the basic info
    for a fulltime employee regardless of position."""

    fulltime_count = 0
    max_hours = 40

    def __init__(self, name, position='all', **kwargs):
        if self.__class__ == Employee or self.__class__ == Pricer or self.__class__ == Cashier:
            Employee.fulltime_count += 1
        else:
            Parttime.parttime_count += 1
        self.name = name
        self.position = position
        self.hours_worked = 0
        self.available_days = {}
        for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            self.available_days[day] = kwargs.get(day, 'True')

    def give_hours(self, hours):
        if hours == 8:
            hours = 7.5
        self.hours_worked += hours

    def audit(self, position, hours):
        if self.position == position and hours == 8 and self.hours_worked + hours <= self.max_hours:
            return True
        else:
            return False


class Parttime(Employee):

    parttime_count = 0
    max_hours = 24

    def __init__(self, name, position='all', **kwargs):
        Employee.__init__(self, name, position=position, **kwargs)

    def audit(self, position, hours):
        if self.position == position and self.hours_worked + hours <= self.max_hours:
            return True
        else:
            return False

    def set_max_hours(self, budget):
        new_parttime_hours = (budget - (Employee.fulltime_count * Employee.max_hours)) / Parttime.parttime_count
        if new_parttime_hours > 22.5:
            new_parttime_hours = 22.5
        elif new_parttime_hours > 19:
            new_parttime_hours = 19
        elif new_parttime_hours > 15.5:
            new_parttime_hours = 15.5
        else:
            new_parttime_hours = 12
        Parttime.max_hours = new_parttime_hours


class Cashier(Employee):

    def __init__(self, name, **kwargs):
        Employee.__init__(self, name, position='cashier', **kwargs)


class Pricer(Employee):

    def __init__(self, name, **kwargs):
        Employee.__init__(self, name, position='pricer', **kwargs)


class ParttimePricer(Parttime, Pricer):

    def __init__(self, name, **kwargs):
        Parttime.__init__(self, name, position='pricer', **kwargs)


class ParttimeCashier(Parttime, Cashier):

    def __init__(self, name, **kwargs):
        Parttime.__init__(self, name, position='cashier', **kwargs)


class Manager(Cashier, Employee):

    def __init__(self, name, **kwargs):
        Employee.__init__(self, name, position='manager', **kwargs)



if '__name__' == 'x':
    from random import choice
    maria = Employee('Maria')
    dory = Employee('Dory')
    myra = Employee('Myra')
    lily = Employee('Lily')
    juan = Parttime('Juan')
    armando = Parttime('Armando')
    chelsea = ParttimeCashier('Chelsea')
    tina = ParttimeCashier('Tina')
    kyle = Parttime('Kyle')
    luis = Parttime('Luis')
    employees = [maria, dory, myra, lily, juan, armando, chelsea, tina, kyle, luis]
'''
    x = [f for f in employees if f.available_days['monday']]
    y = [f for f in x if timedelta(hours=8, minutes=45) in f.available_shifts['opening']]
    for i in range(20):
        k = choice(y)
        k.give_hours()
    j = sorted(y, key=lambda hours: hours.hours_worked - hours.max_hours)
    print([(x.name, x.hours_worked, x.max_hours, x.max_hours - x.hours_worked ) for x in j])
    #print(y)
    monday = []
    tuesday = []
    wednesday = []
    week = [monday, tuesday, wednesday]
    for day in week:
        pool = list(employees)
        for i in range(2):
            for shift in stacy.available_shifts:
                victim = choice(pool)
                day.append(victim)
                pool.remove(victim)

    for day in week:
        print(day)
        '''

'''
    print('May ',)

    for x in may.available_shifts:
        for i in may.available_shifts[x]:
            print(x, str(i))
    print('Joe ', )
    for x in joe.available_shifts:
        for i in joe.available_shifts[x]:
            print(x, str(i))
    print('Kyle')
    for x in kyle.available_shifts:
        for i in kyle.available_shifts[x]:
            print(x, str(i))

    print('Jane', )
    for x in jane.available_shifts:
        for i in jane.available_shifts[x]:
            print(x, str(i))
    '''