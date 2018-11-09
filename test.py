days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months_of_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "Nobember", "December"]

date_template = ".*{day_holder}, {month_holder} \d?\d\s"

date_pattern = ""
for month in months_of_year:
    for day in days_of_week:
        date_pattern += date_template.format(day_holder = day, month_holder = month) + "|"

date_pattern = date_pattern[:-1]
print(date_pattern)
