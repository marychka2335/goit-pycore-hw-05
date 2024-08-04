from decimal import Decimal
import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"
    matches = re.findall(pattern, text)
    for match in matches:
        yield Decimal(match)

def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)
    total = sum(numbers_generator)
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")