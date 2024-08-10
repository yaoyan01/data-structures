# steps towards creating a weather app 

# 1. need to be able to get in requests from the user
    # this means the location of the weather, and the date 

#2. once we get the request, we must send it to the API or whichever backend to retreive the correct data

#3. display the data to the user 

def fetchWeatherData(location, date):
    '''
    receiving user's wanted location and data, and then accessing the api in order to fetch the data

    Args:
        1. location (string) - desired location for filtering 
        2. date (string) - desired time for filtering 

    Return:
        1. data (arr) - weather data from the api 
    
    Errors:
        1. no data fetched
            - raise error 
        2. no location or date 
            - raise error for specified missing parameter 
    '''

    # fetch based on these criteria
    return 

def displayData(arr):
    # display the data in a formatted way
    return 

def main():
    location = input('Enter the location you want to find: ')
    date = input('Enter the date: ')

    weatherData = fetchWeatherData(location, date)
    displayData(weatherData)

main()

