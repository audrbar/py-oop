# 3. Sukurkite bazinę klasę Instrument su metodu play, kuris atspausdina pranešimą kad
# instrumentas groja. Sukurkite dvi išvestines klases Guitar ir Drum, ir taip pat
# implementuokite metodą play() ir atspausdina info kuris butent instrumentas groja.
# Parašykite funkciją play_instrument, kuri priima objektą Instrument ir iškviečia jo metodą play.

class Instrument:
    def __init__(self, name: str):
        self.plays = name

    def play(self):
        print(f"Unknown Instrument plays.")


class Guitar(Instrument):
    def __init__(self, name: str, sound: str):
        self.sound = sound
        super().__init__(name)

    def play(self):
        print(f"Instrument {self.plays} plays {self.sound}.")


class Drum(Instrument):
    def __init__(self, name: str, sound: str):
        self.sound = sound
        super().__init__(name)

    def play(self):
        print(f"Instrument {self.plays} plays {self.sound}.")


git = Guitar('Guitar', 'lala')
dru = Drum('Drum', 'blabla')
git.play()
dru.play()
Instrument.play(git)
