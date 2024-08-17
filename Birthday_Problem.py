import datetime, random

# Generate given number of random Birthdays 
def getBirthdays(numBdays):
    
    collectBdays = []

    for i in range(numBdays):
        # Add random number of days to Start date to get a random Bdays
        randomBdays = datetime.date(2001, 1, 1) + datetime.timedelta(random.randint(0, 365))
        collectBdays.append(randomBdays)

    return collectBdays


# Find a Birthday match
def getMatch(birthdays):

    # Set eliminates duplication
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for holdIndex, birthdayA in enumerate(birthdays):
        for birthdayB in birthdays[holdIndex + 1 : ]:
            if birthdayA == birthdayB:
                return birthdayA
            

# ------------------------------------------------------------------------------------

Months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# while user do not give valid input
while True: 
    print('\nHow many Birthdays do you want? (Max. 100)')
    response = input('> ')
    # accept only decimals and within limit
    if response.isdecimal() and (0 < (int(response)) <= 100):
        numBdays = int(response)
        break

print()

birthdays = getBirthdays(numBdays)

for index, bdayAt in enumerate(birthdays):
    # put coma inbetween
    if index != 0:
        print(', ', end='')

    getMonth = Months[bdayAt.month - 1]
    dateText = f'{getMonth} {bdayAt.day}'
    print(dateText, end='')

matchBday = getMatch(birthdays)

if matchBday != None:
    print(f'\nIn this simulation, {Months[matchBday.month - 1]} {matchBday.day} is not a unique Birthday.\n')
else:
    print('\nAll birthdays are unique.\n')

print('Let\'s do simulation 100_000 times, to get percent of people having Birthday on the same day.')
input('Press Enter to initiate 100_000 simulation.')

simMatch = 0

for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulatons have done.')
    birthdays = getBirthdays(numBdays)
    matchBday = getMatch(birthdays)
    if matchBday != None:
        simMatch += 1

print(f'Result : There is {round((simMatch / 100_000 * 100), 2)} percent people with Birthday on the same day.' )