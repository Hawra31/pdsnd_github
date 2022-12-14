import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = {
        1:'january',
        2:'february',
        3:'march',
        4:'april',
        5:'may',
        6:'june',
        7:'july',
        8:'august',
        9:'september',
        10:'october',
        11:'november',
        12:'december'}

days = {
        1:'sunday',
        2:'monday',
        3:'tuesday',
        4:'wednesday',
        5:'thursday',
        6:'friday',
        7:'saturday'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    cities = ['chicago','new york city','washington']
    months = ['january','february','march','april','may','june','july','august','september','october','november','december','all']
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']

    print('\nHello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        city = input('Which city do you want to explore (chicago, new york city, washington)? ')
        city = city.lower()
        if city not in cities:
            continue
        else:
            month = input('For which month do you want to explore the data (january, february, ..., all)? ')
            month = month.lower()
            if month not in months:
                continue
            else:
                day = input('For which day do you want to explore the dataset (sunday, monday, ..., all)? ')
                day = day.lower()
                if day not in days:
                    continue
                else:
                    break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    for key, value in CITY_DATA.items():
        if key == city:
            df = pd.read_csv(value, index_col = 0)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month != 'all':
        for key, value in months.items():
            if value == month:
                df = df[df['Start Time'].dt.month == key]

    if day != 'all':
        for key, value in days.items():
            if value == day:
                df = df[df['Start Time'].dt.dayofweek == key]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    print('the most common month:', df['Start Time'].dt.month.mode()[0])

    # display the most common day of week
    common_day = df['Start Time'].dt.dayofweek.mode()[0]
    for key, value in days.items():
        if key == common_day:
            print('the most common day of week:', value)

    # display the most common start hour
    print('the most common start hour:', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[61]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('the most common used start station:', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('the most common used end station:', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('the most frequent combination of start station and end station trip:\n\n', df[['Start Station', 'End Station']].mode()[:1],'\n')
    # x[['Start Station', 'End Station']].mode().iloc[:,1][0]

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('the total time travel: ', df['Trip Duration'].sum())

    # display mean travel time
    print('the average time travel: ', df['Trip Duration'].mean(), '\n')

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('the counts of user types:')
    print(df.groupby(['User Type'])['User Type'].count())

    # Display counts of gender
    print('\nthe counts of gender:')
    if 'Gender' in df:
        print(df.groupby(['Gender'])['Gender'].count())
    else:
        print('no data available')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('\nthe earliest birth year: {}\nthe most recent birth year: {}\nthe most common birth year: {}\n'.format(min(df['Birth Year']), max(df['Birth Year']), df['Birth Year'].mode()))
    else:
        print('the earliest birth year:\nno data available\n')

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():

    '''the while loop allows the user to use the piece of code over
       and over without having to run the code again'''

    while True:

        city, month, day = get_filters()
        df1 = load_data(city, month, day)

        time_stats(df1)
        station_stats(df1)
        trip_duration_stats(df1)
        user_stats(df1)

        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() == 'no':
            break
        elif restart.lower() == 'yes':
            continue
        else:
            restart = input('\nWould you like to restart? Enter yes or no.\n')


if __name__ == "__main__":
    main()
