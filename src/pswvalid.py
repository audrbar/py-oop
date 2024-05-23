class PasswordValidator:
    def __init__(self, password):
        self.password = password

    def _has_uppercase(self):
        res = False
        for letter in self.password:
            if letter.isupper():
                res = True
                break
        return res

    def _has_lowercase(self):
        res = False
        for letter in self.password:
            if letter.islower():
                res = True
                break
        return res

    def _has_digit(self):
        res = False
        for letter in self.password:
            if letter.isdigit():
                res = True
                break
        return res

    def is_valid(self):
        res = False
        if self._has_uppercase() and self._has_lowercase() and self._has_digit():
            res = True
        return res

psw_1 = PasswordValidator('Lietuva')
print(f'Ar geras slaptazodis: {psw_1.is_valid()}')