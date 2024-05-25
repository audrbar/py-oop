class PasswordValidator:
    def __init__(self, password):
        self.password = password
        print(f"Success. Password '*******' was created.")

    def _has_uppercase(self) -> bool:
        res = False
        for letter in self.password:
            if letter.isupper():
                res = True
                break
        return res

    def _has_lowercase(self) -> bool:
        res = False
        for letter in self.password:
            if letter.islower():
                res = True
                break
        return res

    def _has_digit(self) -> bool:
        res = False
        for letter in self.password:
            if letter.isdigit():
                res = True
                break
        return res

    def is_valid(self):
        if self._has_uppercase() and self._has_lowercase() and self._has_digit():
            return f'Password is valid.'
        else:
            return f'Password is not valid.'


psw_1 = PasswordValidator('Lithuania')
print(psw_1.is_valid())
