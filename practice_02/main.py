#вариант 20
def km_per_day(km , days):
    if days == 0:
        return 'На ноль делить нельзя'
    return km / days

assert(km_per_day(210, 7)) == 30
assert(km_per_day(86, 0)) == 'На ноль делить нельзя'
assert(km_per_day(50, 2)) == 25
words = [ 'путь' , 'маршрут' , 'путешествие']
print(sorted(words, key=lambda word: len(word)))