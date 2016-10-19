from copy import deepcopy


def translate_for_output(week):
    final_draft = deepcopy(week)

    def translate_shifts():
        # Create an empty list for each time
        for day in week:
            for trans_shifts in [('8:45', '4:45'), ('8:45', '12:45'), ('9:15', '5:15'), ('9:15', '5:15'),
                                 ('11:00', '7:00'), ('11:00', '3:00'), ('1:30', '9:30'), ('5:30', '9:30'),
                                 ('9:45', '5:45'), ('9:45', '1:45'), ('12:30', '8:30'), ('4:30', '8:30'),
                                 ('10:15', '6:15'), ('10:15', '2:15')]:
                final_draft[day].shifts[trans_shifts] = []
            # Copy the contents of the old shift name to the new one
            for shift in week[day].shifts:
                try:
                    if day != 'sunday':
                        if 'open' in shift and 'cashier' in shift and week[day].shifts[shift][-1] == 8:
                            final_draft[day].shifts[('8:45', '4:45')].append(week[day].shifts[shift])
                        elif 'open' in shift and 'cashier' in shift and week[day][shift][-1] == 4:
                            final_draft[day].shifts[('8:45', '12:45')].append(week[day].shifts[shift])
                        elif 'open' in shift and 'pricer' in shift and week[day].shifts[shift][-1] == 8:
                            final_draft[day].shifts[('9:15', '5:15')].append(week[day].shifts[shift])
                        elif 'open' in shift and 'pricer' in shift and week[day][shift][-1] == 4:
                            final_draft[day].shifts[('9:15', '1:15')].append(week[day].shifts[shift])
                        elif 'mid' in shift and week[day].shifts[shift][-1] == 8:
                            final_draft[day].shifts[('11:00', '7:00')].append(week[day].shifts[shift])
                        elif 'mid' in shift and week[day].shifts[shift][-1] == 4:
                            final_draft[day].shifts[('11:00', '3:00')].append(week[day].shifts[shift])
                        elif 'close' in shift and week[day].shifts[shift][-1] == 8:
                            final_draft[day].shifts[('1:30', '9:30')].append(week[day].shifts[shift])
                        elif 'close' in shift and week[day].shifts[shift][-1] == 4:
                            final_draft[day].shifts[('5:30', '9:30')].append(week[day].shifts[shift])
                    else:
                        if 'open' in shift and 'cashier' in shift and week[day].shifts[shift][-1] == 8:
                            final_draft[day].shifts[('9:45', '5:45')].append(week[day].shifts[shift])
                        elif 'open' in shift and 'cashier' in shift and week[day][shift][-1] == 4:
                            final_draft[day].shifts[('9:45', '1:45')].append(week[day].shifts[shift])
                        elif 'open' in shift and 'pricer' in shift and week[day].shifts[shift][-1] == 8:
                            final_draft[day].shifts[('10:15', '6:15')].append(week[day].shifts[shift])
                        elif 'open' in shift and 'pricer' in shift and week[day][shift][-1] == 4:
                            final_draft[day].shifts[('10:15', '2:15')].append(week[day].shifts[shift])
                        elif 'mid' in shift and week[day].shifts[shift][-1] == 8:
                            final_draft[day].shifts[('11:00', '7:00')].append(week[day].shifts[shift])
                        elif 'mid' in shift and week[day].shifts[shift][-1] == 4:
                            final_draft[day].shifts[('11:00', '3:00')].append(week[day].shifts[shift])
                        elif 'close' in shift and week[day].shifts[shift][-1] == 8:
                            final_draft[day].shifts[('12:30', '8:30')].append(week[day].shifts[shift])
                        elif 'close' in shift and week[day].shifts[shift][-1] == 4:
                            final_draft[day].shifts[('4:30', '8:30')].append(week[day].shifts[shift])

                except IndexError:
                    pass
                finally:
                    del final_draft[day].shifts[shift]

    def translate_days():
        for day in week:
            try:
                if day == 'sunday':
                    final_draft[4] = final_draft['sunday']
                elif day == 'monday':
                    final_draft[7] = final_draft['monday']
                elif day == 'tuesday':
                    final_draft[10] = final_draft['tuesday']
                elif day == 'wednesday':
                    final_draft[13] = final_draft['wednesday']
                elif day == 'thursday':
                    final_draft[16] = final_draft['thursday']
                elif day == 'friday':
                    final_draft[19] = final_draft['friday']
                elif day == 'saturday':
                    final_draft[22] = final_draft['saturday']
            finally:
                del final_draft[day]

    translate_shifts()
    translate_days()
    return final_draft
