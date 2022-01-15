# FU BOFENG
# TP066667


def question1():
    # Calculate how many cups of each ingredient are needed for one cookie
    cups_sugar_per_cookie = 1.5 / 48
    cups_butter_per_cookie = 1 / 48
    cups_flour_per_cookie = 2.75 / 48

    # Ask the user how many cookies he/she wants to make
    cookie_num = input('Dear Sir/Miss, how many cookies do you want to make?\n')
    # Convert String to Float
    cookie_num = float(cookie_num)

    # Calculate how many cups of each ingredient are needed for given number of cookies
    sugar_needed = cookie_num * cups_sugar_per_cookie
    butter_needed = cookie_num * cups_butter_per_cookie
    flour_needed = cookie_num * cups_flour_per_cookie

    # Print results
    print('To make ' + str(cookie_num) + ' cookies, we need:')
    print(str(sugar_needed) + ' cups of sugar.')
    print(str(butter_needed) + ' cups of butter.')
    print(str(flour_needed) + ' cups of flour.')


def question2():
    # Ask the user for following values
    start_num = input('Starting number of organisms: ')
    daily_increase = input('Average daily increase: ')
    days = input('Number of days to multiply: ')

    # Convert String to int
    start_num = int(start_num)
    daily_increase = int(daily_increase[:-1])
    days = int(days)

    # For loop for printing results
    print('Day Approximate Population:')
    for i in range(days):
        print(str(i + 1) + ' {:g}'.format(start_num))

        # Calculate the approximate size of a population of organisms for each day
        start_num = start_num * (1 + daily_increase / 100)


def question3():
    # Ask the user for the total rainfall for each of 12 months
    rainfall = input('Enter rainfall for each month separated by comma:\n')
    rainfall_list = rainfall.split(',')

    # Initialize values
    total_rainfall = 0
    highest_month = []
    highest_amount = 0
    lowest_month = []
    lowest_amount = 1000000

    # For loop
    for i in range(len(rainfall_list)):

        # Covert String to Float
        rainfall_month = float(rainfall_list[i])

        # Calculate total rainfall by adding every month's rainfall together
        total_rainfall += rainfall_month

        # Find the month of highest rainfall
        if rainfall_month > highest_amount:
            highest_amount = rainfall_month
            highest_month.clear()
            highest_month.append(i)
        elif rainfall_month == highest_amount:
            highest_month.append(i)

        # Find the month of lowest rainfall
        if rainfall_month < lowest_amount:
            lowest_amount = rainfall_month
            lowest_month.clear()
            lowest_month.append(i)
        elif rainfall_month == lowest_amount:
            lowest_month.append(i)

    # Calculate average monthly rainfall
    ave_rainfall = total_rainfall / len(rainfall_list)

    # Print results
    print('Total rainfall for the year: ', total_rainfall)
    print('Average monthly rainfall: ', ave_rainfall)
    print('months with the highest amounts: ', [i + 1 for i in highest_month])
    print('months with the lowest amounts: ', [i + 1 for i in lowest_month])


def question4():
    # Constant value for gravity
    g = 9.8

    # Make list
    fall_time_list = [i + 1 for i in range(10)]

    # Call the function in for loop
    for i in range(len(fall_time_list)):
        dist = falling_distance(fall_time_list[i], g)
        print('The objects has fallen {:g}'.format(dist) + ' meters in ' + str(i + 1) + ' second(s).')


def falling_distance(fall_time: int, g: float) -> float:
    return 0.5 * g * fall_time * fall_time


if __name__ == '__main__':
    choice = int(input('Which question do you want to answer?'))

    if choice == 1:
        question1()
    elif choice == 2:
        question2()
    elif choice == 3:
        question3()
    elif choice == 4:
        question4()
    else:
        print('Wrong input!')
