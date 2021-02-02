import datetime

class Person:
    def __init__(self, first_name: str, last_name: str, birthdate: datetime.date):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if self.validate_name(value):
            self._first_name = self.format_name(value)
        else:
            raise ValueError("Invalid name. Name cannot be empty, None or contain any numbers.")
            
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if self.validate_name(value):
            self._last_name = self.format_name(value)
        else:
            raise ValueError("Invalid name. Name cannot be empty, None or contain any numbers.")

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, date):
        if self.validate_birthdate(date):
            self._birthdate = date
        else:
            raise ValueError("InvalidBirthdate must be of datetime.date type and the date must be from 1/01/1900 to current day.")

    def __str__(self):
        return f"{self._first_name} {self._last_name}, born in {self._birthdate.strftime('%d %B %Y')}."

    @staticmethod
    def validate_name(name):
        if len(name.strip()) == 0 or name is None:
            return False
        for ch in name:
            if not ch.isalpha() and ch not in ["-", "'", " "]:
                return False
        return True

    @staticmethod
    def format_name(name):
        names = name.split()
        formated_names = []
        for name in names:
            formated_name = ""
            for i in range(len(name)):
                if i == 0:
                    formated_name += name[i].upper()
                elif name[i].isalpha() and not name[i-1].isalpha():
                    formated_name += name[i].upper()
                else:
                    formated_name += name[i].lower()
            formated_names.append(formated_name)
        return ' '.join(formated_names)

    @staticmethod
    def validate_birthdate(birthdate):
        if not isinstance(birthdate, datetime.date):
            return False
        if not datetime.date(1900, 1, 1) < birthdate <= datetime.date.today():
            return False
        return True
