# 9. Sukurkite klasę „ReservationSystem“, kuri tvarko paslaugos (pvz., viešbučio kambarių, restorano stalų) rezervacijas.
# Įdiekite rezervacijų kūrimo, rezervacijų atšaukimo, prieinamumo tikrinimo ir visų rezervacijų peržiūros metodus.

class ReservationSystem:

    def __init__(self, name: str):
        self.name = name
        self.bkg_items = []
        print(f"\nSuccess: The hotel {self.name} was established.")

    def create_booking_item(self, id_: str, kind: str, *is_booked: bool):
        self.bkg_items.append({'id': id_, 'kind': kind, 'is_booked': False})
        # print(f"Success. The {kind} #{id_} was created.")

    def book_item(self):
        free_items = []
        for item in self.bkg_items:
            if not item['is_booked']:
                free_items.append(item)
        print('\nJust choose one of the our available offers by id:')
        for item in free_items:
            print(f"- {item['kind']} #{item['id']}, is booked now: {item['is_booked']}.")
        usr_choice = input('Your choice (#): ')
        for item in free_items:
            if item['id'] == usr_choice:
                item['is_booked'] = True

    def release_item(self):
        booked_items = []
        for item in self.bkg_items:
            if item['is_booked']:
                booked_items.append(item)
        print('Please release your booked item by id:')
        for item in booked_items:
            print(f"- {item['kind']} #{item['id']}, is booked now: {item['is_booked']}.")
        usr_choice = input('Your choice (#): ')
        for item in booked_items:
            if item['id'] == usr_choice:
                item['is_booked'] = False

    def get_items_by_state(self, state):
        state_items = []
        if state == 'free':
            for item in self.bkg_items:
                if not item['is_booked']:
                    state_items.append(item)
        else:
            for item in self.bkg_items:
                if item['is_booked']:
                    state_items.append(item)

        print(f'\nPlease find listed below {state} items:')
        for item in state_items:
            print(f"- {item['kind']} #{item['id']}, is booked now: {item['is_booked']}.")

    def get_all(self):
        print(f"The overall booking items available: ")
        for item in self.bkg_items:
            print(f"- {item['kind']} #{item['id']}, is booked now: {item['is_booked']}.")


hotel = ReservationSystem('Dream')
hotel.create_booking_item('1', 'room')
hotel.create_booking_item('2', 'room')
hotel.create_booking_item('3', 'table')
hotel.create_booking_item('4', 'table')
hotel.book_item()
hotel.book_item()
hotel.get_items_by_state('free')
hotel.get_items_by_state('booked')