from datetime import datetime

def get_days_from_today(date):
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = target_date - today
        return delta.days
    except ValueError:
        return "Invalid date format. Use 'YYYY-MM-DD'."

# Приклади використання функції
print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2020-10-09"))
print(get_days_from_today("invalid-date"))
