# 1. Sukurkite stateless klasę StringUtils su statiniais metodais įprastoms eilutės
# operacijoms atlikti: to_uppercase, to_lowercase ir reverse_string.

class StringUtils:
    @staticmethod
    def to_uppercase(a: str):
        return a.upper()

    @staticmethod
    def to_lowercase(a: str):
        return a.lower()

    @staticmethod
    def reverse_string(a: str):
        return a[::-1]


print(StringUtils.to_uppercase('Zodis'))
print(StringUtils.to_lowercase('Zodis'))
print(StringUtils.reverse_string('Zodis'))


# 2. Sukurkite statefull klasę Skaitiklis, kuri saugoja skaičių. Joje turėtų būti metodai,
# skirti skaičiui padidinti, sumažinti, atstatyti ir dabartiniam skaičiui gauti.

class Skaitiklis:
    def __init__(self, numb: int):
        self.numb = numb
        self.initial = numb

    def increase(self, amount):
        return self.numb + amount

    def decrease(self, amount):
        return self.numb - amount

    def reverse(self):
        return self.initial

    def get_numb(self):
        return f"{self.numb}"


num = Skaitiklis(3)
print(num.increase(3))
print(num.decrease(3))
print(num.reverse())
print(num.get_numb())

# 3. Sukurkite klasę Timer, kuri gali paleisti, sustabdyti ir iš naujo nustatyti laikmatį bei
# nurodyti praėjusį laiką sekundėmis. Naudokite time python paketą.
import time


class Timeri:

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        print(f"\n\nTotal elapsed time: {(self.end_time - self.start_time):.3f} seconds\n")
        exit(0)

    def end(self):
        self.end_time = time.time()

    def get_duration(self):
        return self.end - self.start


timer_1 = Timeri()
print(timer_1.start())
print(timer_1.end())


class Timer:
    def __init__(self) -> None:
        self.deltatime = 0
        self.current_time = 0

    def start_time(self):
        self.current_time = time.time()

    def stop_time(self):
        self.deltatime = time.time() - self.current_time

    def resume_time(self):
        self.start_time()

    def results(self):
        return self.deltatime


#timeriux = Timer()
#timeriux.start_time()
#time.sleep(2)
#timeriux.stop_time()
#timeriux.resume_time()
#time.sleep(5)
#print(timeriux.results())

# 4. Sukurkite klasę DateUtils su statiniais metodais, kad apskaičiuotumėte dienų skaičių tarp dviejų datų ir
# patikrintumėte, ar tam tikri metai yra keliamieji metai. Naudokite python paketą datetime.
from datetime import datetime


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


# 5. Sukurkite klasę ShoppingCart, kuriame būtų prekių sąrašas. Joje turėtų būti metodai:
# pridėti prekes, pašalinti prekes, peržiūrėti krepšelį ir apskaičiuoti bendrą kainą.

class ShoppingCart:
    def __init__(self, id_: str, _items: dict):
        self.id = id_
        self.items = _items

    def _calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item
        return total

    def add_item(self, name, amount):
        self.items.update({name: amount})
        print(f"The Cart #{self.id} was updated: {name} added.")
        self.get_total_items()

    def remove_item(self, name):
        self.items.pop(name)
        print(f"The Cart #{self.id} was updated: {name} removed.")
        self.get_total_items()

    def get_total_items(self):
        print(f"The Cart #{self.id}  Total: {self._calculate_total()}")


cart = ShoppingCart('1', {})
cart.add_item('banana', 5)
cart.add_item('berry', 7)
cart.add_item('apple', 9)
print(cart.items)
cart.get_total_items()
cart.remove_item('berry')
print(cart.items)

# 6. Sukurkite klasę UserSession, kuri valdo vartotojo prisijungimo būseną.
# Joje turėtų būti būdai prisijungti, atsijungti, patikrinti,
# ar vartotojas yra prisijungęs, ir gauti prisijungusio vartotojo duomenis.
import uuid


class UserSession:

    def __init__(self):
        self.session_id = None
        self.is_logged = False

    def login(self):
        self.is_logged = True
        self.session_id = uuid.uuid4()
        print(f"Success. You are logged in with session id: {self.session_id}")

    def logoff(self):
        self.is_logged = False
        self.session_id = None
        print(f"Success. You are logged off. Your session id expired.")

    def is_logged(self):
        if not self.is_logged:
            print(f"You are logged off.")
        else:
            print(f"You are logged in with session id: {self.session_id}")

    def get_user_data(self):
        return f"User session id: {self.session_id}, login status: {self.is_logged}."


session = UserSession()
print(session.get_user_data())
session.login()
print(session.is_logged)
session.logoff()
print(session.is_logged)
print(session.get_user_data())


# 7. Sukurkite klasę Order (užsakymas), kuriame būtų saugoma užsakymo informacija (prekės, kiekiai, kainos).
# Įdiekite prekių pridėjimo, pašalinimo, bendros kainos apskaičiavimo ir nuolaidų taikymo metodus.

class Order:
    def __init__(self, id_: str):
        self.id = id_
        self.items = []
        print(f"The Order item #{self.id} was created.")

    def add_item(self, name: str, price: int, amount: int):
        self.items.append({'name': name, 'price': price, 'amount': amount})
        print(f"The {amount} pieces of '{name}' for {price}$ each where added to the Order #{self.id}.")

    def total_price(self) -> float:
        total: float = 0.0
        for item in order.items:
            total += item['price'] * item['amount']
        print(f"The Order #{self.id} total price is {total}$.")
        return round(total)

    def checkout(self):
        if self.total_price() >= 100:
            total = round(self._calculate_discount(self.total_price()))
            print(f"The Order #{self.id} checkout {total}$, 10% discount was applied.")
        else:
            print(f"The Order #{self.id} checkout {self.total_price()}$, no discount applied.")

    @staticmethod
    def _calculate_discount(total):
        return total * 0.9

    def get_order_content(self):
        print(f"The Order #{self.id} consist of:")
        for item in order.items:
            print(f"- {item['amount']} pieces of '{item['name']}' for {item['price']}$ each.")


order = Order('1')
order.add_item('bread', 2, 5)
order.add_item('milk', 5, 2)
order.add_item('nuts', 10, 2)
order.get_order_content()
order.total_price()
order.checkout()

# 8. Sukurkite klasę DataTransformer su statiniais metodais, kad atliktumėte duomenų transformavimo operacijas:
# skaičių sąrašo normalizavimą, eilučių kodavimą/dekodavimą ir duomenų filtravimą pagal kriterijus.

class DataTransformer:
    def __init__(self):
        pass