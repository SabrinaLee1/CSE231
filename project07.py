#######################################################
# Programming Project 07
#
# function to open all files
# function to read files
# function to get the data in range
# function to get the min
# function to get the max
# function to get the average
# function to get the modes
# function to get high and low avgs
# function to display statistics
# main function to go through inputs
# call open and read file, and ask for option
# while loop for option selection
#   if/elif/else statements for options
#     display selected option results
# closing message
# close the files
# main function required code
#
######################################################

import csv
from datetime import datetime
from operator import itemgetter

COLUMNS = ["date",  "average temp", "high temp", "low temp", "precipitation", \
           "snow", "snow depth"]

TOL = 0.02

BANNER = 'This program will take in csv files with weather data and compare \
the sets.\nThe data is available for high, low, and average temperatures,\
\nprecipitation, and snow and snow depth.'    

MENU = '''
        Menu Options:
        1. Highest value for a specific column for all cities
        2. Lowest value for a specific column for all cities
        3. Average value for a specific column for all cities
        4. Modes for a specific column for all cities
        5. Summary Statistics for a specific column for a specific city
        6. High and low averages for each category across all data
        7. Quit
        Menu Choice: '''

# function to open all files             
def open_files():
    ''' 
    Opens entered files only if files exist
    Returns: file pointers of citys (list), cities (list)
    '''
    cities = input("Enter cities names: ")
    cities_list = cities.split(',')
    #make list of cities and city csvs
    fp_list =[]
    fps = []
    for city in cities_list:
        try:
            fp = open(city +'.csv', 'r')
            fp_list.append(city)
            fps.append(fp)
        except FileNotFoundError:
            print('\nError: File {:s} is not found'.format(city + '.csv'))
    return fp_list, fps

# function to read files            
def read_files(cities_fp):
    ''' 
    Reads a csv file using a file pointer and returns
    a list of lists of tuples
    cities_fp: list of city file pointers(file object)
    Returns: list of lists of tuples of city information (list)
    '''
    biggest_list = []
    for city in cities_fp:
        inner_list = []
        #skip header lines
        file_csv = csv.reader(city)
        next(file_csv)
        next(file_csv)
        #go thru each line, assign vlaues
        #if the index is empty make it none
        for line in file_csv:
            if line[0] != '':
                date = line[0]
            else:
                TAVG = None
            if line[1] != '':
                TAVG = float(line[1])
            else:
                TAVG = None
            if line[2] != '':
                TMAX = float(line[2])
            else: 
                TMAX = None
            if line[3] != '':
                TMIN = float(line[3])
            else:
                TMIN = None
            if line[4] != '':
                PRCP = float(line[4])
            else:
                PRCP = None
            if line[5] != '':
                SNOW = float(line[5])
            else:
                SNOW = None
            if line[6] != '':
                SNWD = float(line[6])
            else:
                SNWD = None
            inner_list.append((date,TAVG,TMAX,TMIN,PRCP,SNOW,SNWD))
        biggest_list.append(inner_list)
    return biggest_list

# function to get the data in range
def get_data_in_range(master_list, start_str, end_str):
    ''' 
    Takes a list of lists of tuples and
    extracts data based of given dates
    master_list: list of lists of tuples with city information(list)
    start_str: entered start date from user (str)
    end_str: entered end date from user (str)
    Returns: lists of lists of tuples 
    with data in specified parameters(list)
    '''
    start_date = datetime.strptime(start_str, "%m/%d/%Y").date()
    end_date = datetime.strptime(end_str, "%m/%d/%Y").date()
    L= []
    for item in master_list:
        lil_L=[]
        for value in item:
            date = value[0]
            #gets the date in the file
            today = datetime.strptime(date, "%m/%d/%Y").date()
            #compare to start and end date
            if start_date <= today <= end_date:
                lil_L.append(value)
        L.append(lil_L)
    return L

# function to get the min
def get_min(col, data, cities): 
    ''' 
    Takes the list of list of tuples and extracts wanted minimum values.
    col: index of wanted catergories (int)
    data: list of tuples of the data in range (list)
    cities: list of strings of cities (list)
    Returns: list of tuples of city and lowest temp (list)
    '''
    L_min = []
    #get index for each city
    for index,city in enumerate(cities):
        value = data[index]
        #initalize min
        min_value = 1000000
        for tup in value:
            num = tup[col]
            if num == None:
                continue
            #if the number is smaller, make it the min
            elif num < min_value:
                min_value = num
        tupl = (city,min_value) 
        L_min.append(tupl)
    return L_min

# function to get the max        
def get_max(col, data, cities): 
    ''' 
    Takes the list of list of tuples and extracts wanted max values.
    col: index of wanted catergories (int)
    data: list of tuples of the data in range (list)
    cities: list of strings of cities (list)
    Returns: list of tuples of city and highest temp (list)
    '''
    L_max = []
    #get index for each city
    for index,city in enumerate(cities):
        value = data[index]
        #initialize max
        max_value = 0
        for tup in value:
            num = tup[col]
            if num == None:
                continue
            #if the number is bigger, make it max
            elif num > max_value:
                max_value = num
        tupl = (city,max_value) 
        L_max.append(tupl)
    return L_max

# function to get the average    
def get_average(col, data, cities): 
    ''' 
    Takes the list of list of tuples and extracts wanted avg values.
    col: index of wanted catergories (int)
    data: list of tuples of the data in range (list)
    cities: list of strings of cities (list)
    Returns: list of tuples of city and avg temp (list)
    '''
    L_avg = []
    #get index for each city
    for index,city in enumerate(cities):
        value = data[index]
        #counters and collecters for avg at end
        counter = 0
        value_collector = 0
        for tup in value:
            num = tup[col]
            if num == None:
                continue
            value_collector += num
            counter += 1
        avg_value = round((value_collector/counter),2)
        tupl = (city,avg_value) 
        L_avg.append(tupl)
    return L_avg

# function to get the modes
def get_modes(col, data, cities):
    '''
    Takes the list of list of tuples and extracts wanted mode values.
    col: index of wanted catergories (int)
    data: list of tuples of the data in range (list)
    cities: list of strings of cities (list)
    Returns: list of tuples of city and mode temps (list)
    '''
    L_modes = []
    #go thru each city
    for city in cities:
        other_col = []
        aindex = cities.index(city)
        #go through list of cities at index
        for list_cities in data[aindex]:
            new_col = list_cities[col]
            #add to new column if its not none
            if new_col != None:
                other_col.append(new_col)
        other_col.sort()
        #create counter and streak for indexing
        counter = 1
        streak = []
        num1 = other_col[0]
        #get index of items in other_col
        for x,line in enumerate(other_col):
            if x == 0:
                continue
            subtracted = num1 - line
            if num1 == 0:
                #update num value
                num1 = line
                continue
            #gets absolute value of the divided numbers
            divided = abs(subtracted/num1)
            #compares divided with tol constant 
            if divided <= TOL:
                counter += 1
            #if its greater, append it 
            else:
                streak.append((counter,num1))
                num1 = line
                counter =1
        #executes this at the very end after going thru all items
        else:
            streak.append((counter,num1))
        other_streak = []
        maximum = 0
        for value in streak:
            #does some more comparisions on the numbers to get mode
            if value[0] > maximum:
                maximum = value[0]
                #clears it and adds new most common
                other_streak.clear()
                other_streak.append(value[1])
            elif value[0] == maximum:
                #adds most common
                other_streak.append(value[1])
        #checks for final modes returned
        if maximum == 1:
            #if there is no mode
            L_modes.append((city,[],maximum))
        else:
            #if there is a mode
            L_modes.append((city,other_streak,maximum))
    return L_modes

# function to get high and low avgs
def high_low_averages(data, cities, categories):
    '''
    Takes the list of list of tuples and extracts 
    wanted high and low values.
    col: index of wanted catergories (int)
    data: list of tuples of the data in range (list)
    cities: list of strings of cities (list)
    Returns: list of tuples of city and 
    high and low avg for each category(list)
    '''
    L_hilow = []
    #find column index that corresponds to each category
    for category in categories:
        if category in COLUMNS:
            col_index = COLUMNS.index(category)
            new_avgplace = get_average(col_index,data,cities)
            #sort for the highs and lows
            L_highs = sorted(new_avgplace, key=itemgetter(1))
            L_lows = sorted(new_avgplace,key=itemgetter(1), reverse = True)
            #get highest and lowest val
            highest = L_highs[0]
            lowest = L_lows[0]
            #make them a list
            L_small = [highest,lowest]
        else:
            L_small = None
        L_hilow.append(L_small)
    return L_hilow   

# function to display statistics
def display_statistics(col,data, cities):
    ''' 
    Displays the summary statistics for each city.
    col:index of wanted catergories (int)
    data: list of tuples of the data in range (list)
    cities:list of strings of cities (list)
    '''
    get_the_min = get_min(col, data, cities)
    get_the_max = get_max(col, data, cities)
    get_the_avg = get_average(col, data, cities)
    get_the_mode = get_modes(col, data, cities)
    #go through cities and get indexes
    for x,city in enumerate(cities):
        print("\t{}: ".format(city))
        print("\tMin: {:.2f} Max: {:.2f} Avg: {:.2f}"
        .format(get_the_min[x][1],get_the_max[x][1],get_the_avg[x][1]))
        if get_the_mode[x][2]==1:
            print("\tNo modes.")
        else:
            new_list = []
            #makes the floats a string so they can be added
            for val in get_the_mode[x][1]:
                new_list.append(str(val))
            str_new_list = ''
            for item in new_list:
                if item:
                    str_new_list += item
            print("\tMost common repeated values ({:d} occurrences): {:s}\n"
            .format(get_the_mode[x][2],str_new_list))      
# main function to go through inputs            
def main():
    print(BANNER)
    cities, fps = open_files()
    biggest_list = read_files(fps)
    option = input(MENU)
    while option != '7':
        if option == '1':
            start_date=input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date=input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category=input("\nEnter desired category: ")
            data_collect=get_data_in_range(biggest_list, start_date, end_date)
            while category.lower() not in COLUMNS:
                print("\n\t{} category is not found.".format(categories))
                category = input("\nEnter desired category: ")
            col_index = COLUMNS.index(category.lower())
            the_max = get_max(col_index,data_collect,cities)
            print("\n\t{}: ".format(category.lower()))
            #go thru returned max vals
            for city_info in the_max:
                print("\tMax for {:s}: {:.2f}"
                .format(city_info[0],city_info[1]))
            option = input(MENU)   
        elif option == '2':
            start_date=input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date=input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category=input("\nEnter desired category: ")
            data_collect = get_data_in_range(biggest_list, start_date, end_date)
            while category.lower() not in COLUMNS:
                print("\n\t{} category is not found.".format(categories))
                category = input("\nEnter desired category: ")
            #get the index of the cat
            col_index = COLUMNS.index(category.lower())
            the_min = get_min(col_index,data_collect,cities)
            print("\n\t{}: ".format(category.lower()))
            #go thru returned min vals
            for city_info in the_min:
                print("\tMin for {:s}: {:.2f}"
                .format(city_info[0],city_info[1]))
            option = input(MENU)
        elif option =='3':
            start_date=input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date=input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category = input("\nEnter desired category: ")
            data_collect=get_data_in_range(biggest_list,start_date,end_date)
            while category.lower() not in COLUMNS:
                print("\n\t{} category is not found.".format(categories))
                category = input("\nEnter desired category: ")
            #get the index of the cat
            col_index = COLUMNS.index(category.lower())
            the_avg = get_average(col_index,data_collect,cities)
            print("\n\t{}: ".format(category.lower()))
            for city_info in the_avg:
                print("\tAverage for {:s}: {:.2f}"
                .format(city_info[0],city_info[1]))
            option = input(MENU)
        elif option =='4':
            start_date=input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date=input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category= input("\nEnter desired category: ")
            data_collect=get_data_in_range(biggest_list,start_date,end_date)
            while category.lower() not in COLUMNS:
                print("\n\t{} category is not found.".format(categories))
                category = input("\nEnter desired category: ")
            #get the index of the cat
            col_index = COLUMNS.index(category.lower())
            the_mode = get_modes(col_index,data_collect,cities)
            print("\n\t{}: ".format(category.lower()))
            #go thru values given in the mode
            for city_info in the_mode:
                string = ''
                #convert the floats to strings to be iterated thru
                list_modes = [str(val) for val in city_info[1]]
                for value in list_modes:
                    if value:
                        string += value + ','
                #gets rid of last comma
                string = string[:-1]
                print("\tMost common repeated values for "
                "{:s} ({:d} occurrences): {:s}\n"
                .format(city_info[0],city_info[2],string))
            option = input(MENU)
        elif option == '5':
            start_date=input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date=input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category =input("\nEnter desired category: ")
            data_collect = get_data_in_range(biggest_list, start_date, end_date)
            while category.lower() not in COLUMNS:
                print("\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ")
            #get the index of the cat
            col_index = COLUMNS.index(category.lower())
            print("\n\t{}: ".format(category.lower()))
            display_statistics(col_index, data_collect,cities)
            option = input(MENU)
        elif option == '6':
            start_date=input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end_date=input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category=input("\nEnter desired categories "
            "seperated by comma: ").lower().split(',')
            data_collect=get_data_in_range(biggest_list, start_date, end_date)
            get_the_highlow = high_low_averages(data_collect, cities,category)
            #initialize a count for indexing
            count = 0
            print('\nHigh and low averages for each category across all data.')
            for x in get_the_highlow:
                #get the specific cat wanted
                the_cat = category[count]
                if x != None:
                    print("\n\t{}: ".format(the_cat))
                    print("\tLowest Average: {:s} = {:.2f} "
                    "Highest Average: {:s} = {:.2f}"
                    .format(x[0][0],x[0][1],x[1][0],x[1][1]))
                else:
                    print("\n\t{} category is not found.".format(the_cat))
                #increase index
                count += 1
            option = input(MENU)
    print("\nThank you using this program!")

if __name__ == "__main__":
    main()
                                           


