
from datetime import datetime


class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = int(age)
        self.gender = gender
        self.total_income = float(total_income)
        self.expenses = expenses
        self.created_at = datetime.utcnow()

    def to_dict(self):
        return {
            "age": self.age,
            "gender": self.gender,
            "total_income": self.total_income,
            "expenses": self.expenses,
            "created_at": self.created_at
        }
