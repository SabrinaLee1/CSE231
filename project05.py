############################################
# Programming Project 05
#
# function to display menu
# function to open file
# function to find maximums
# function to find minimums
# function to read files
# function to search through animes
# main function for inputs
#   print BANNER
#   display options
#   ask for selection of options 
#   while loop for options 
#       if/elif/else statements for options
#   while loop for closing option
#main function required code
###########################################

#function to display menu
def display_menu():
    """
    Displays menu of options
    Returns: menu of options
    """
    MENU = "Options" + \
          "\n\t1) Get max/min stats" + \
          "\n\t2) Search for an anime" + \
          "\n\t3) Stop the program!" 
    print(MENU)
# function to open file
def open_file():
    """
    Opens entered file only if file exists
    Returns: file pointer (file)
    """
    while True:
        filename = input("\nEnter filename: ")
        try:
            fp = open(filename,'r', encoding="utf-8")
            break
        except (FileNotFoundError, IOError):
            print("\nFile not found!")
            continue
    return fp
# function to find maximums
def find_max(value, name, max_value, max_name):
    """
    Finds maximum values and the names associated.
    Value: entered value (float)
    Name: entered name (str)
    Max_value: maximum possible value (float)
    Max_name: name of maximum possible value (str)
    Returns: maximum value (float) and maximum name (str)
    """
    if value < max_value:
        max_name = "\n\t{}".format(max_name.strip())
        return max_value, max_name
    if value > max_value:
        name = "\n\t{}".format(name.strip())
        return value, name
    else:
        max_value = value
        concat_name = "\n\t{}\n\t{}".format(max_name.strip(), name.strip())
        return max_value, concat_name
# function to find minimums
def find_min(value, name, min_value, min_name):
    """
    Finds minimum values and the names associated.
    Value: entered value (float)
    Name: entered name (str)
    Min_value: minimum possible value (float)
    Min_name: name of minimum possible value (str)
    Returns: minimum value (float) and minimum name (str)
    """
    if value > min_value:
        min_name = "\n\t{}".format(min_name.strip())
        return min_value, min_name
    if value < min_value:
        name = "\n\t{}".format(name.strip())
        return value, name
    else:
        min_value = value
        concat_name = "\n\t{}\n\t{}".format(min_name.strip(), name.strip())
        return min_value, concat_name
# function to read files
def read_file(data_fp):
    """
    Reads a file and finds the highest scoring title, 
    the highest episode count title, and the lowest scoring title
    Data_fp:entered and retured fp file object from open_file() (file object)
    Returns:the max score (float),name of max score(str),max episodes (float),
    name of max episode (str), min score (float), name of min score (str),
    average score (float)
    """
    #initializing all values
    max_score = 0
    max_score_name = ''
    max_episodes = 0
    max_episode_name = ''
    min_score = 100000
    min_score_name = ''
    total_score = 0
    num_of_anime = 0
    avg_score =0
    for line in data_fp:
        title = line[0:100].strip()
        score = line[100:105].strip() 
        episodes = line[105:110].strip()
        #check to see if score is addable or not 
        if score != 'N/A':
            score = float(score)
            max_score, max_score_name = find_max(score, title,\
            max_score, max_score_name)
            min_score, min_score_name = find_min(score, title,\
            min_score, min_score_name)
            total_score += score
            num_of_anime += 1
        #check to see if episodes are addable or not 
        if episodes != 'N/A':
            episodes = float(episodes)
            max_episodes, max_episode_name = find_max(episodes,\
            title, max_episodes, max_episode_name)
        # if number of animes are zero fix
        if num_of_anime == 0: 
            avg_score = 0.0 
        else:
            avg_score = round(total_score/num_of_anime,2)
    return max_score, max_score_name, max_episodes, max_episode_name,\
    min_score, min_score_name, avg_score
# function to search through animes
def search_anime(data_fp, anime_name): 
    """
    Reads through a file and returns the title and release 
    season if it contains the search string passed as parameter.
    Data_fp:entered and retured fp file from open_file()(file object)
    Anime_name:user intputted anime name
    Returns:the number of titles with the search string which is count(int)
    and title and release season output string which is out_str(str)
    """
    count = 0
    out_str = ''
    for line in data_fp:
        title = line[0:100]
        release_season = line[110:122]
        if anime_name in title:
            count +=1 
            title = "\n\t{}{}".format(title, release_season)
            out_str += title
    return count, out_str
# main function for inputs
def main():
    """
    Goes through each menu option and asks for inputs/checks parameters.
    Returns calculated answers for each of the above functions.
    """
    BANNER = "\nAnime-Planet.com Records" \
             "\nAnime data gathered in 2022" 
    print(BANNER)
    display_menu()
    option = input("\tEnter option: ")
    while option != '3':
        #read file option 
        if option == '1':
            fp = open_file()
            max_score, max_score_name,max_episodes,max_episode_name,min_score,\
            min_score_name, avg_score = read_file(fp)
            print("\n\nAnime with the highest score of {}:".format(max_score))
            print(max_score_name)
            print("\n\nAnime with the highest episode count of {:,.0f}:"\
            .format(max_episodes))
            print(max_episode_name)
            print("\n\nAnime with the lowest score of {:.2f}:".\
            format(min_score))
            print(min_score_name)
            print("\n\nAverage score for animes in file is {}".\
            format(avg_score))
            display_menu()
            option = input("\tEnter option: ")
        #search anime option
        elif option == '2':
            fp = open_file()
            in_str =input("\nEnter anime name: ")
            count, out_str = search_anime(fp, in_str)
            if count == 0 and out_str == '':
                print("\nNo anime with '{}' was found!".\
                format(in_str))
            else:
                print("\nThere are {} anime titles with '{}'".\
                format(count, in_str))
                print(out_str)
            display_menu()
            option = input("\tEnter option: ")
        #else to exit program and invalid input chck
        else:
            if option == '3':
                fp.close()
                break
            else:
                print("\nInvalid menu option!!! Please try again!")
                display_menu()
                option = input("\tEnter option: ")
    # while loop to exit program
    while option == '3':
        print("\nThank you using this program!")
        break
if __name__ == "__main__":
    main()
    

