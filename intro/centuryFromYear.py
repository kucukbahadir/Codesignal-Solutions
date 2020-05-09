def centuryFromYear(year):
    if year % 100 < 1:
        return year // 100
    else:
        return year // 100 + 1