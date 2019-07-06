# allergy_values = ['Y', 'N','YES','NO']
# allergy = input('Do you have a food allergy? (Y/N)')

# while allergy.upper() not in allergy_values:
#     print("Please enter Y or N")
#     allergy = input('Do you have a food allergy? (Y/N) ')

# if allergy.upper() == "N":
#     print('Welcome to the tour, as you have no food allergies you can enjoy all of the food on offer')
# else:
#     specific_allergy = input("What sort of allergy do you have? ")
#     print(f'We see that you have an allergy called: {specific_allergy}, we\'ll make sure that you\'re catered for')

from app import get_greeting

def test_get_greeting():
    greeting = get_greeting('test_name')
    expected = 'Hello' + 'test_name' + ', Welcome to the Tour'
    assert greeting == expected

from app import day_break

def test_day_break():
    in_month = day_break(35)
    expected = False
    assert in_month == expected

def test_day_notbreak():
    in_month = day_break(30)
    expected = True
    assert in_month == expected