import time

print('Poniżej znajduje się lista jednostek, które możesz zamienić.')
list_of_choices = ['kilometry na metry', 'kilogramy na gramy', 'godziny na minuty']
print(list_of_choices)
wybrana_funkcja = str(input('Wybierz jednostki, które chcesz zamienić: '))


def kilometry_na_metry(kilometers):
    meters = kilometers * 1000
    return meters

def kilogramy_na_gramy(kilograms):
    grams = kilograms * 100
    return grams

def godziny_na_minuty(hours):
    minutes = hours * 60
    return minutes

if wybrana_funkcja == 'kilometry na metry':
    kilometers = int(input('Podaj liczbę kilometrów: '))
    meters = kilometry_na_metry(kilometers)
    print(f"{kilometers} km to {kilometry_na_metry(kilometers)} metrów")

elif wybrana_funkcja == 'kilogramy na gramy':
    kilograms = int(input('Podaj liczbę kilogramów: '))
    print(f"{kilograms} kg to {kilogramy_na_gramy(kilograms)} gramów")

elif wybrana_funkcja == 'godziny na minuty':
    hours = int(input('Podaj liczbę godzin: '))
    print(f"{hours} h to {godziny_na_minuty(hours)} minut")

else:
    raise ValueError(f"Nie wybrano poprawnej opcji. Możliwe opcje to -> {list_of_choices}")

time.sleep(30)