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


print(StringUtils.to_uppercase('Zodiacs'))
print(StringUtils.to_lowercase('Zodiacs'))
print(StringUtils.reverse_string('Zodiacs'))
