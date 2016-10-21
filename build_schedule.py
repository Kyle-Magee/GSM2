from random import choice
from take_input import excel_sheet


"""Scheduling algorithm"""


class Weekday:

    @staticmethod
    def load_employees(filename):
        Weekday.employees = excel_sheet(filename)
        Weekday.budget = Weekday.employees['week_budget']
        Weekday.employees.pop('week_budget')

    def __init__(self, day):
        self.budget = Weekday.budget / 7
        self.budget_used = 0
        self.pool = [staff for staff in Weekday.employees.keys() if Weekday.employees[staff].available_days[day] and
                     Weekday.employees[staff].hours_worked < Weekday.employees[staff].max_hours]
        self.shifts = {'main_open_cashier': [], 'main_mid_cashier': [], 'main_close_cashier': [],
                       'main_open_pricer': [], 'secondary_mid_pricer': [], 'main_close_pricer': [],
                       'secondary_close_pricer': [], 'secondary_mid_cashier': []}
        self.buff_schedule('main')

    def schedule_worker(self, staff, shift, hours_will_work):
        Weekday.employees[staff].give_hours(hours_will_work)
        self.shifts[shift].extend([Weekday.employees[staff].name, hours_will_work])
        self.pool.remove(staff)

    def buff_schedule(self, priority):
        for job_type in ('cashier', 'pricer'):
            for shift in [shift for shift in self.shifts.keys() if shift.endswith(job_type) and
                          shift.startswith(priority)]:
                try:
                    for position in (job_type, 'all'):
                        if self.budget_used < self.budget:
                            for time in (8, 4):
                                candidate_pool = [staff for staff in self.pool if Weekday.employees[staff].audit(position, time)]
                                if candidate_pool:
                                    self.schedule_worker(choice(candidate_pool), shift, time)
                                    self.budget_used += time
                                    raise IndexError('Employee Found')
                except IndexError:
                    continue


def make_a_schedule(filename):
    Weekday.load_employees(filename)
    week = {'monday': None, 'tuesday': None, 'wednesday': None, 'thursday': None, 'friday': None, 'saturday': None,
            'sunday': None}
    for day in week:
        week[day] = Weekday(day)
    
    for day in week:
        week[day].buff_schedule('secondary')

    return week
