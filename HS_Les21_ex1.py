# Lesson 21
"""
1. Class Exercise:
Create a Python class representing a Hospital account with methods to schedule visit
and remove schedule

"""
import datetime
import time


class HospitalTimetable:
    working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    break_hour = [13]
    current_date = datetime.datetime.now()
    start = datetime.datetime(2024, 9, 1, 9, 0)
    end = datetime.datetime(2024, 12, 30, 18, 0)
    duration = datetime.timedelta(minutes=30, hours=0)
    visits_timetable = []
    working_hours_helper = set()
    for w in working_days:
        if w == working_days[-1]:
            for i in range(start.hour, break_hour[0]):
                working_hours_helper.add(i)
        else:
            for j in range(start.hour, end.hour):
                working_hours_helper.add(j)
        work_hours = working_hours_helper - set(break_hour)

    def schedule_visit(self, visit_date, same_day=False):
        actual_date = datetime.date.today()
        visit_date_helper = datetime.datetime.strptime(visit_date, "%Y-%m-%d %H:%M")

        if visit_date_helper.year != 2024:
            return f"A visit to be scheduled for the year 2024"
        if visit_date_helper.month < actual_date.month:
            return f"A visit can be scheduled for the current month or till the end of this year."
        if actual_date.day > 10 and visit_date_helper.month == actual_date.month:
            return f"A visit can be scheduled starting next month"
        if visit_date_helper.strftime("%A") not in self.working_days:
            return f"A visit can't be scheduled on Sunday. "
        if visit_date_helper.strftime("%A") == self.working_days[-1]:
            if visit_date_helper.hour not in self.work.hours:
                return f"A visit to be scheduled until 13:00 on Saturdays"
        if visit_date_helper.minute != 0 and visit_date_helper.minute != 30:
            return f"A visit to be scheduled with duration of 30 minutes starting by 9 am."
        if visit_date_helper.month == actual_date.month and visit_date_helper.day <= 10:
            return f"A visit to be scheduled after the 10th of the month"

        if same_day is True:  # to be scheduled on the same day
            if visit_date_helper not in self.visits_timetable:
                if visit_date_helper.strftime("%A") == self.working_days[-1]:  # saturdays
                    if visit_date_helper.hour in self.work.hours:
                        self.visits_timetable.append(visivt_date_helper)
                        return self.visits_timetable
                if visit_date_helper.strftime("%A") in self.working_days[:-1]:  # except saturdays
                    if visit_date_helper.hour in self.work_hours:
                        self.visits_timetable.append(visit_date_helper)
                        return self.visits_timetable
            if visit_date_helper in self.visits_timetable:
                if visit_date_helper.strftime("%A") == self.working_days[-1]:  # saturdays
                    helper = visit_date_helper + self.duration
                    while help.hour <= self.work_hours[-1]:
                        if helper not in self.visits_timetable and helper.hour in self.work_hours:
                            visit_date_helper = helper
                            self.visits_timetable.append(helper)
                            return visit_date_helper, self.visits_timetable
                if visit_date_helper.strftime("%A") in self.working_days[:-1]:  # except saturdays
                    helper = visit_date_helper + self.duration
                    while helper.hour <= self.work_hours[-1]:
                        if helper not in self.visits_timetable and helper.hour in self.work_hours:
                            visit_date_helper = helper
                            self.visits_timetable.append(helper)
                            return visit_date_helper, self.visits_timetable
        else:  # may be scheduled on available time
            if visit_date_helper in self.visits_timetable:
                self.visits_timetable.sort()
                n = 0
                for v in self.visits_timetable:
                    if v.day >= actual_date:
                        helper_actual = self.visits_timetable[v:]
                        n += 1
                        if n < len(helper_actual) and helper_actual[n] - v > self.duration:
                            visit_date_helper = v + self.duration
                            self.visits_timetable.append(visit_date_helper)
                            return self.visits_timetable, visit_date_helper


visit1 = HospitalTimetable()
print(visit1.schedule_visit("2024-09-16 14:30", True))

