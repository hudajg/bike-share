import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday',
    'wednesday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Hello everyone, this code is written, you must write exactly like your data, if you add a space or comma, your request will not be answered')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    the_city = ''
    while the_city.lower() not in CITY_DATA:
        the_city = input(
        "\n enter the name of city data? (chicago, new york city, washington)?\n")
        if the_city.lower() in CITY_DATA:
            city = CITY_DATA[the_city.lower()]
        else:
            print("missmatch. tryagain\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    the_month = ''
    while the_month.lower() not in MONTH_DATA:
        the_month = input(
        "\nenter the month of month data?(all,january, february, ... , june)\n")
        if the_month.lower() in MONTH_DATA:
            month = the_month.lower()
        else:
            print("missmatch. tryagain")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    the_day = ''
    while the_day.lower() not in DAY_DATA:
        the_day = input(
            "\nenter the day of day data? (all, monday, tuesday, ... sunday)\n")
        if the_day.lower() not in DAY_DATA:
            print("missmatch . tryagain\n")

        else:
           day = the_day.lower()
    
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
   # here I copy the code of practice 3 to can open the data (dataFrame) :
    # load data file into a dataframe
    #df = pd.read_csv(CITY_DATA[city]) # but i change it to can have a output (line 27 to 31 i didn't but it on CITY_DATA just on city .....)
    df = pd.read_csv(city)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    # f on print to can write {}
    print(f'The most common month : {months[month-1]}')

    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0]
    # f on print to can write {}
    print(f'The most common month : {day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    populr_hour = df['hour'].mode()[0]
    print(f'The most common start hour is : {populr_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f'most commonly used start station: {start_station} ')

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f'most commonly used end station: {end_station} ')

    # TO DO: display most frequent combination of start station and end station trip
    station_trip = df['Start Station'] + '+' + df['End Station']
    print(f'most frequent combination of start station and end station trip :{station_trip}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   # TO DO: display total travel time
    #total_travel_Time = sum(df['Trip Duration'])
    total_travel_Time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_Time/86400, "days")
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time/3600, "seconds")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time=time.time()

    # TO DO: Display counts of user types
    usertypes=df['User Type'].value_counts()
    print('User Types:\n', usertypes)


    # TO DO: Display counts of gender
      
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("No info available, sorry!")


    # earliest/most recent/most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(recent)
        common_birth = df['Birth Year'].mode()[0]
        print(common_birth)
    else:
        print("No info available, sorry!")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def raws(df):
    """Displays raw data .
    """
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        
        
def main():
    while True:
        city, month, day=get_filters()
        df=load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart=input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()