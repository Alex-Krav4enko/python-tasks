from datetime import datetime
from accounting.application import salary, people

print(f'today: {datetime.today()}')

if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()
