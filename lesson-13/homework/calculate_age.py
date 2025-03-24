from datetime import date
import calendar

def calculate_age(birth_date):
    today = date.today()
  years = today.year - birth_date.year
    has_birthday_occurred = (today.month, today.day) >= (birth_date.month, birth_date.day)
    if not has_birthday_occurred:
        years -= 1
    last_birth_year = today.year if has_birthday_occurred else today.year - 1
    
    if birth_date.month == 2 and birth_date.day == 29:
        if not calendar.isleap(last_birth_year):
            last_birthday = date(last_birth_year, 2, 28)
        else:
            last_birthday = date(last_birth_year, 2, 29)
    else:
        try:
            last_birthday = date(last_birth_year, birth_date.month, birth_date.day)
        except ValueError:
          
            last_birthday = date(last_birth_year, birth_date.month + 1, 1) - date.resolution
            if last_birthday < date(last_birth_year, birth_date.month, 1):
                last_birthday = date(last_birth_year, birth_date.month, 1)
    
  
    months = (today.year - last_birthday.year) * 12 + (today.month - last_birthday.month)
    if today.day < last_birthday.day:
        months -= 1
       
        if today.month == 1:
            prev_month, prev_year = 12, today.year - 1
        else:
            prev_month, prev_year = today.month - 1, today.year
        days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
        days = (today.day + days_in_prev_month) - last_birthday.day
    else:
        days = today.day - last_birthday.day
    
    return years, months, days


birth_date = date(2000, 5, 20)  
years, months, days = calculate_age(birth_date)
print(f"You are {years} years, {months} months, {days} days old")
