# [프로그래머스] 개인정보 수집 유효기간

def change(date,term_month):
    year,month,day = date.split(".")
    year = int(year)
    month = int(month) + int(term_month)
    while month > 12:
        year += 1
        month -= 12
    if month == 0:
        month = 12

    return [int(year),int(month),int(day)]

def solution(today, terms, privacies):
    result = []
    hash_map = dict()
    today_year,today_month,today_day = today.split(".")
    today_year = int(today_year)
    today_month = int(today_month)
    today_day = int(today_day)
    print(today_year,today_month,today_day)
    for term in terms:
        a,b = term.split(" ")
        hash_map[a] = b
    for i in range(len(privacies)):
        date,term = privacies[i].split(" ")
        validation_date = change(date,hash_map[term])
        print(validation_date)
        if validation_date[0] < today_year:
            result.append(i+1)
        elif today_year == validation_date[0]and validation_date[1] < today_month:
            result.append(i+1)
        elif today_year == validation_date[0]and validation_date[1] == today_month and validation_date[2] <= today_day:
            result.append(i+1)
    return result




print(solution("2019.01.01"  , ["B 12"],   ["2017.12.21 B"]))