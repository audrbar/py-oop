# 3. Sukurkite klasę Timer, kuri gali paleisti, sustabdyti ir iš naujo nustatyti laikmatį bei
# nurodyti praėjusį laiką sekundėmis. Naudokite time python paketą.
from datetime import datetime
import time


class Timer:
    def __init__(self) -> None:
        self.delta = 0
        self.current_time = 0

    def start_time(self):
        self.current_time = time.time()

    def stop_time(self):
        self.delta = time.time() - self.current_time

    def resume_time(self):
        self.start_time()

    def results(self):
        return self.delta


class DateUtils:
    @staticmethod
    def days_between_dates(date1, date2):
        delta = abs(date2 - date1)
        return delta.days

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)

print("Dienų skaičius tarp", date1.strftime("%Y-%m-%d"), "ir", date2.strftime("%Y-%m-%d"), ":",
      DateUtils.days_between_dates(date1, date2))

year = 2024
print(year, "metai yra keliamieji:", DateUtils.is_leap_year(year))

timer_2 = Timer()
timer_2.start_time()
time.sleep(2)
timer_2.stop_time()
timer_2.resume_time()
time.sleep(5)
print(timer_2.results())
