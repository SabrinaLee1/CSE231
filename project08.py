####################################################
# Programming Project 08
#
# function to open files
# function to read the game files
# function to read the discount files
# function to get games in certain year
# function to get games by genre
# function to get games by developer
# function to get games discounted price
# function to get games by developer and year
# function to get games with no dicount by genre
# function to get games with a dicount by developer
# main function to go through inputs
# call open and read file for games and dicounts
# while loop for option selection
#     if/elif/else statements for options
#         display selected option results
# closing message
# main function required code
#
################################################
import csv
from operator import itemgetter

MENU = '''\nSelect from the option: 
        1.Games in a certain year 
        2. Games by a Developer 
        3. Games of a Genre 
        4. Games by a developer in a year 
        5. Games of a Genre with no discount 
        6. Games by a developer with discount 
        7. Exit 
        Option: '''
# function to open files
def open_file(s):
    ''' 
    Opens entered files only if files exist
    Returns: file pointers of games and discounts(file object)
    '''
    while True:
        #opens both dicount and games csv
        open_file = input('\nEnter {} file: '.format(s))
        try:
            #tries to open file
            fp = open(open_file, 'r', encoding='UTF-8')
            break
        except FileNotFoundError:
            print('\nNo Such file')
            #goes back up to input statement
            continue
    return fp
# function to read the game files
def read_file(fp_games):
    ''' 
    This function uses the provided file pointer and 
    reads the games data file.
    fp_games:file pointer of games csv (file pointer)
    Returns:a dictionary with name of the game as the key
    and a list of the remaining data as the value (dict)
    '''
    reader = csv.reader(fp_games)
    next(reader, None)
    D_games = {}
    for line in reader:
        L = []
        #extracting the values
        name = str(line[0])
        release_date = str(line[1])
        developer = (line[2])
        developer = developer.split(';')
        genres = (line[3])
        genres = genres.split(';')
        player_modes = (line[4]).lower()
        player_modes = player_modes.split(';')
        if player_modes[0] != 'multi-player':
            player_modes = 1
        else:
            player_modes = 0
        try:
            #make the price correct
            price = float(line[5].replace(',', ''))
            price = price *0.012
        except:
            price = 0.0
        overall_reviews = (line[6])
        reviews = int(line[7])
        percent_positive = (line[8].replace('%', ''))
        percent_positive = int(percent_positive)
        win_support = line[9]
        #making a list of the supports
        if int(win_support) == 1:
            L.append('win_support')
        mac_support = line[10]
        if int(mac_support) == 1:
            L.append('mac_support')
        lin_support = line[11]
        if int(lin_support) == 1:
            L.append('lin_support')
        D_games[name] = [release_date, developer, genres,player_modes, 
        price, overall_reviews, reviews, percent_positive, L]
    return D_games
# function to read the discount files
def read_discount(fp_discount):
    ''' 
    This function uses the provided file pointer and reads the dicounts data file.
    fp_discount: file pointer of dicounts csv (file pointer)
    Returns:a dictionary with key as the name of the game and value as
    the discount as a float rounded to 2 decimals (dict)
    '''
    reader = csv.reader(fp_discount)
    next(reader, None)
    D_discount = {}
    for line in reader:
        #extracting the values
        name = str(line[0])
        discount = round(float(line[1]), 2)
        D_discount[name] = discount
    return D_discount
# function to get games in certain year
def in_year(master_D, year):
    '''
    This function filters out games that were released in a specific year.
    master_D: dictionary made in the read file function (dict)
    year: user entered year (int)
    Returns: a list of game names sorted alphabetically (list of strings)
    '''
    #had extra time so tried using list comprehension get the date from the values and
    #make a list of just the numbers of date and check if its the same as the user entered year 
    big_list = [key for key, value in master_D.items() if int(
        value[0].split('/')[2]) == year]
    return sorted(big_list)
# function to get games by genre
def by_genre(master_D, genre):
    ''' 
    This function filters out games that are of a specific genre.
    master_D: dictionary made in the read file function (dict)
    genre: user entered genre (list)
    Returns: s a list of game names sorted by percentage positive 
    reviews in descending order (list of strings)
    '''
    genre_ = []
    for key, value in master_D.items():
        #get the list of genres
        genre_list = value[2]
        for item in genre_list:
            if item in genre:
                #append the name and parameter to be sorted by
                genre_.append([key, value[7]])
                break
    #sort by the parameter
    sort_gen = sorted(genre_, key=itemgetter(1), reverse=True)
    name_list = [item[0] for item in sort_gen]
    return name_list
# function to get games by developer
def by_dev(master_D, developer):
    ''' 
    This function filters out games that are made by a specific developer
    master_D: dictionary made in the read file function (dict)
    developer: user entered developer (list)
    Returns: a list of game names sorted from latest to oldest 
    released games (list of strings)
    '''
    dev_list = []
    for key, val in master_D.items():
        #get the developers
        dev = val[1]
        if developer in dev:
            #get the name and year(only the actual year portion)
            dev_list.append((key, int(val[0][-4:])))
    sort_dev = sorted(dev_list, key=itemgetter(1), reverse=True)
    L = []
    for item in sort_dev:
        L.append(item[0])
    return L
# function to get games discounted price
def per_discount(master_D, games, discount_D):
    ''' 
    This function accepts as an argument the main dictionary you have 
    created in the read_file function, a list of games (games), and the discount dictionary 
    master_D: dictionary made in the read file function (dict)
    games: user entered games (list)
    discount_D: dictionary made in the read discount file function (dict)
    Returns: a list of the discounted price for each game in the list of 
    games rounded to 6 decimal digits (list of strings)
    '''
    dis_list = []
    for key in games:
        if key not in discount_D:
            dis_list.append(master_D[key][4])    
        else:
            #append the price and apply the equation to it, and round
            dis_list.append(
                round((1-(discount_D[key]/100))*master_D[key][4], 6))   
    return dis_list
# function to get games by developer and year
def by_dev_year(master_D, discount_D, developer, year):
    ''' 
    This function filters out games by a specific developer and released in a specific year.
    master_D: dictionary made in the read file function (dict)
    discount_D: dictionary made in the read discount file function (dict)
    developer: user entered developer (str)
    year: user entered year (int)
    Returns: a list of game names sorted in increasing prices (list of strings)
    '''
    #get the games by developers and years
    by_developer = set(by_dev(master_D, developer))
    by_year = set(in_year(master_D, year))
    #get the similar values
    final = (by_developer & by_year)
    final_list = list(final)
    #get the prices with discounts
    by_dis = per_discount(master_D, final_list, discount_D)
    by_dev_year_list = []
    #get the index
    for x,item in enumerate(final_list):
        by_dev_year_list.append((final_list[x], by_dis[x]))
    sorted_bydev = sorted(by_dev_year_list, key=itemgetter(1))
    #get just the name
    name_list = [item[0] for item in sorted_bydev]
    return name_list


def by_genre_no_disc(master_D, discount_D, genre):
    ''' 
    This function filters out games by a specific genre that do not offer
    a discount on their price.
    master_D: dictionary made in the read file function (dict)
    discount_D: dictionary made in the read discount file function (dict)
    genre: user entered genre (str)
    Returns: a list of game names sorted from cheapest to most expensive. (list of strings)
    '''
    #get games by genre
    bygen = by_genre(master_D, genre)
    L = []
    for game_name in bygen:
        if game_name not in discount_D:
            #append game name and parameter
            L.append((game_name, master_D[game_name][4]))
    #sort by the parameter
    L_sort = sorted(L, key=itemgetter(1))
    # getting just the name
    name_list = [item[0] for item in L_sort]
    return name_list


def by_dev_with_disc(master_D, discount_D, developer):
    ''' 
    This function filters out games by a specific developer and offers discounts.
    master_D: dictionary made in the read file function (dict)
    discount_D: dictionary made in the read discount file function (dict)
    developer: user entered developer (str)
    Returns: a list of game names sorted from cheapest to most expensive.(list of strings)
    '''
    dev_with = []
    for game_name, game_data in master_D.items():
        #check if the developer is in the data
        if developer in game_data[1]:
            if game_name in discount_D:
                #add the name and the parameter
                dev_with.append((game_name, discount_D[game_name]))
    #sort alphabetically
    dev_with_alph = sorted(dev_with)
    #sort by parameter
    sorted_ = sorted(dev_with_alph, key=itemgetter(1))
    name_list = [item[0] for item in sorted_]
    return name_list


def main():
    #open all the files
    fp_games = open_file('games')
    fp_dis = open_file('discount')
    #read the files
    D_games = read_file(fp_games)
    D_discount = read_discount(fp_dis)
    option = input(MENU)
    #start while loop for options
    while option != '7':
        #check if its a valid option
        if option not in ['1', '2', '3', '4', '5', '6', '7']:
            print("\nInvalid option")
            option = input(MENU)
        elif option == '1':
            while True:
                #checking if its a valid year
                year_in = input('\nWhich year: ')
                try:
                    year_in = int(year_in)
                    break
                except:
                    print("\nPlease enter a valid year")
            #getting the games by year
            games_inyear = in_year(D_games, year_in)
            #if it returns a value, print it
            if len(games_inyear) != 0:
                print("\nGames released in {}:".format(year_in))
                print(', '.join(games_inyear))
            else:
                print("\nNothing to print")
            option = input(MENU)
        elif option == '2':
            developer = input('\nWhich developer: ')
            #get the games by developer
            dev_in = by_dev(D_games, developer)
            #it it returns a true val,  print it
            if len(dev_in) != 0:
                print("\nGames made by {}:".format(developer))
                print(', '.join(dev_in))
            else:
                print("\nNothing to print")
            option = input(MENU)
        elif option == '3':
            genre = input('\nWhich genre: ')
            #get the games by genre
            gen_in = by_genre(D_games, genre)
            #if its a valid val, print it
            if len(gen_in) != 0:
                print("\nGames with {} genre:".format(genre))
                print(', '.join(gen_in))
            else:
                print("\nNothing to print")
            option = input(MENU)
        elif option == '4':
            developer = input('\nWhich developer: ')
            while True:
                #check if the year is valid
                year_in = input('\nWhich year: ')
                try:
                    #if its a valid year
                    year_in = int(year_in)
                    break
                except:
                    print("\nPlease enter a valid year")
            #get the games by developer and year
            dev_and_year = by_dev_year(D_games, D_discount, developer,year_in)
            #if it returns a valid val, print it
            if len(dev_and_year) != 0:
                print("\nGames made by {} and released in {}:"
                      .format(developer, year_in))
                print(', '.join(dev_and_year))
            else:
                print("\nNothing to print")
            option = input(MENU)
        elif option == '5':
            genre = input('\nWhich genre: ')
            #get games by genre with no dicounts
            gen_nodis = by_genre_no_disc(D_games, D_discount, genre)
            #if it returns a valid val, print it
            if len(gen_nodis) != 0:
                print("\nGames with {} genre and without a discount:"
                      .format(genre))
                print(', '.join(gen_nodis))
            else:
                print("\nNothing to print")
            option = input(MENU)
        elif option == '6':
            developer = input('\nWhich developer: ')
            #get games with discount by developer
            dev_wdis = by_dev_with_disc(D_games, D_discount, developer)
            #if it returns a valid val, print it
            if len(dev_wdis) != 0:
                print("\nGames made by {} which offer discount:"
                      .format(developer))
                print(', '.join(dev_wdis))
            else:
                print("\nNothing to print")
            option = input(MENU)
    #if they choose option 7
    print("\nThank you.")


if __name__ == "__main__":
    main()
