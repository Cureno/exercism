def is_leap_year(year):
    divisible_by_4 = year % 4 == 0
    divisible_by_100_not_by_400 = year % 100 == 0 and not year % 400 == 0
    
    return divisible_by_4 and not divisible_by_100_not_by_400
