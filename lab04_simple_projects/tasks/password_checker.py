class PasswordChecker:
    """Задача: password_checker"""
    def __init__(self, pwd: str):
        self.pwd = pwd

    def is_strong(self) -> bool:
        """Длина >= 8 и есть цифра"""
        if len(self.pwd)>=8 and (('0') in self.pwd or ('1') in self.pwd or ('2') in self.pwd or ('3') in self.pwd or ('4') in self.pwd or ('5') in self.pwd or ('6') in self.pwd or ('7') in self.pwd or ('8') in self.pwd or ('9') in self.pwd):
            return True
        else:
            return False
