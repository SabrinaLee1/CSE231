#################################
# Programming Project 06
#
# function to open file
# function to read file
# function to get books by criterion
# function to get books by criteria
# function to get books by keyword
# function to sort authors
# function to recommend books
# function to display books
# function to get option
# main function to go through inputs
# call open file, read file, and get option
# while loop for option selection
#     if/elif/else statements for options
#     display selected option results
# close the file
# main function required code
#
##################################

import csv
from operator import itemgetter

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 (3) Category\n\
                 (5) Year Published\n\
                 (6) Average Rating (or higher) \n\
                 (7) Page Number (within 50 pages) \n\
                 Enter criteria number: "
# function to open file
def open_file():
    """
    Opens entered file only if file exists
    Returns: file pointer (file)
    """
    while True:
        filename = input("Enter file name: ")
        try:
            fp = open(filename,'r', encoding="utf-8")
            break
        except (FileNotFoundError, IOError):
            print("\nError opening file. Please try again.")
            continue
    return fp
# function to read file
def read_file(fp):
    """
    Reads a csv file using a file pointer and returns
    a list of book tuples
    fp: opened and returns file object from open_file (file object)
    Returns: list of book tuples (list)
    """
    reader = csv.reader(fp)
    next(reader,None)
    L =[]
    for line in reader:
        tup_list = []
        try:
            #extracting values from csv and adding to list
            isbn13 = line[0]
            tup_list.append(isbn13)
            title = line[2]
            tup_list.append(title)
            authors = line[4]
            tup_list.append(authors)
            categories = line[5].lower()
            if ',' in categories:
                new_categories = categories.split(',')
                tup_list.append(new_categories)
            else:
                cat_list = []
                cat_list.append(categories)
                tup_list.append(cat_list)
            description = line[7]
            tup_list.append(description)
            year = line[8]
            tup_list.append(year)
            rating = line[9]
            tup_list.append(float(rating))
            num_pages= line[10]
            if num_pages.isnumeric():
                tup_list.append(int(num_pages))
            rating_count= line[11]
            if rating_count.isnumeric():
                tup_list.append(int(rating_count))
        except:
            continue
        tup_list = tuple(tup_list)
        L.append(tup_list)
    return L
    
TITLE = 1
CATEGORY = 3
YEAR = 5
RATING = 6
PAGES = 7
# function to get books by criterion
def get_books_by_criterion(list_of_tuples, criterion, value):
    """
    Retrieve list of book tuples that match a certain criterion
    List_of_tuples: list of selected book tuples (list)
    Criterion: entered criterion (int)
    Value: desired value for selected criterion (int/float/string)
    Returns: List of book tuples that match selected criterion (list)
    """
    L_books = []
    #going through each criterion option and appending to list
    if criterion == 1:
        for tup in list_of_tuples:
            if tup[1].lower() == value.lower():
                return tup
    elif criterion == 3:
        for tup in list_of_tuples:
            for categories in tup[3]:
                if value.lower()==categories.lower():
                    L_books.append(tup)
    elif criterion == 5:
        for tup in list_of_tuples:
            if tup[5]==value:
                L_books.append(tup)
    elif criterion == 6:
        for tup in list_of_tuples:
            if float(tup[6])>=float(value):
                L_books.append(tup)
    elif criterion == 7:
        for tup in list_of_tuples:
            #checking length of pages
            if (tup[7]) in range(int(value)-50,int(value)+51):
                L_books.append(tup)
    return L_books
# function to get books by criteria
def get_books_by_criteria(list_of_tuples, category, rating, page_number):
    """
    Calls get_books_by_criterion three times to sort the list of book
    tuples by a certain criteria
    List_of_tuples: list of selected book tuples (list)
    Category: entered category (string)
    Rating: entered rating (float)
    Page_number: entered page number (int)
    Returns: list of book tuples sorted by given criteria (list)
    """
    category_call = get_books_by_criterion(list_of_tuples,3,category)
    rating_call = get_books_by_criterion(category_call,6,rating)
    page_call = get_books_by_criterion(rating_call,7,page_number)
    return page_call
# function to get books by keyword
def get_books_by_keyword(list_of_tuples, keywords):
    """
    Retrives all books whos description contains a given keyword
    List_of_tupes: list of selected book tuples (list)
    keywords: entered key words (list)
    Returns: list of book tuples containing given keyword (list)
    """
    L_keyword = []
    for tup in list_of_tuples:
        #checking every keyword in list of keywords
        for keyword in keywords:
            if keyword.lower() in tup[4].lower():
                L_keyword.append(tup)
                break
    return L_keyword 
#function to sort authors
def sort_authors(list_of_tuples, a_z=True):
    """
    Creates a new list of book tuples sorted by authors name
    List_of_tuples: list of selected book tuples (list)
    a_z: determines ascending and descending order of sort (bool)
    Returns: new list of book tuples sorted by author name (list)
    """
    if a_z == True:
        sorted_authors=sorted(list_of_tuples,key=itemgetter(2),reverse= False)
    elif a_z == False:
        sorted_authors=sorted(list_of_tuples,key=itemgetter(2),reverse= True)
    return sorted_authors
# function to recommend books
def recommend_books(list_of_tuples,keywords,category,rating,page_number,a_z):
    """
    Retrieves all books filtered by category, rating, page number and keyword
    and returns list sorted by author name.
    List_of_tuples: list of selected book tuples (list)
    Keywords: entered keywords (string)
    Category: entered category (string)
    Rating: entered rating (float)
    Page_number: entered number of pages (int)
    A_z: Determines ascending and descending sorting (bool)
    Returns: New list of book tuples sorted by given parameters (list)
    """
    criteria_call=get_books_by_criteria(list_of_tuples,category\
    ,rating,page_number)
    keyword_call = get_books_by_keyword(criteria_call, keywords)
    authors_call = sort_authors(keyword_call, a_z)
    return authors_call
#function to display books
def display_books(list_of_tuples):
    """
    Displays book information if title and authors are less then 35 characters
    List_of_tuples: list of selected book tuples (list)
    """
    print('\nBook Details:')
    if len(list_of_tuples) > 0:
        print(f"{'ISBN-13':15s} {'Title':35s} {'Authors':35s} {'Year':6s}"
        f" {'Rating':8s} {'Number Pages':15s} {'Number Ratings':15s}")
        for tup in list_of_tuples:
            #checking length before displaying
            if len(tup[1]) <= 35 and len(tup[2]) <= 35:
                print(f"{tup[0]:15s} {tup[1]:35s} {tup[2]:35s} {tup[5]:6s}"
                f" {tup[6]:<8.2f} {tup[7]:<15d} {tup[8]:<15d}")
    else:
        print("Nothing to print.")
# function to get option
def get_option():
    """
    Displays menu of options and returns selected option
    Returns: selected option (string)
    """
    MENU = "\nWelcome to the Book Recommendation Engine\n\
        Choose one of below options:\n\
        1. Find a book with a title\n\
        2. Filter books by a certain criteria\n\
        3. Recommend a book \n\
        4. Quit the program\n\
        Enter option: "
    option = input(MENU)
    if option in ['1','2','3','4']:
        return option
    else: 
        print("\nInvalid option")
        return None
# main function for inputs
def main():
    """
    Goes through each menu option and asks for inputs/checks parameters.
    Returns calculated answers for each of the above functions
    """
    # open the file, read it, and get an option
    fp = open_file()
    L = read_file(fp)
    option = get_option()
    while option != '4':
        # find a book with a title
        if option == '1':
            book_title = input("\nInput a book title: ")
            #getting books with book title
            L_books = [get_books_by_criterion(L,1,book_title)]
            display_books(L_books)
            option = get_option()
        # filter books by a certain criteria
        elif option =='2':
            while True:
                try:
                    criterion_wanted = input(CRITERIA_INPUT)
                    criterion_wanted = int(criterion_wanted)
                    if criterion_wanted not in [3,5,6,7]:
                        print("\nInvalid input")
                        continue
                    else:
                        break
                except:
                    print("\nInvalid input")
            while True:
                wanted_val = input("\nEnter value: ")
                #check if criteria 6 and 7 have correct type
                if criterion_wanted == 6 or criterion_wanted == 7:
                    try:
                        if criterion_wanted == 6:
                            wanted_val = float(wanted_val)
                            break
                        else:
                            wanted_val = int(wanted_val)
                            break
                    except:
                        print("\nInvalid input")
                else:
                    break
            L_books=get_books_by_criterion(L,criterion_wanted,wanted_val)
            L_books_sort = sort_authors(L_books)
            display_books(L_books_sort[:30])
            option = get_option()
        #recommend a book
        elif option == '3':
            cat_des = input("\nEnter the desired category: ")
            rat_des = input("\nEnter the desired rating: ")
            page_des = input("\nEnter the desired page number: ")
            #check to have correct type
            while True:
                try:
                    rat_des = float(rat_des)
                    page_des = int(page_des)
                    break
                except:
                    print("\nInvalid input")
            a_z_val=input("\nEnter 1 for A-Z sorting, and 2 for Z-A sorting: ")
            if a_z_val == '1':
                a_z_val = True
            else:
                a_z_val = False
            keywordz_des = input("\nEnter keywords (space separated): ")\
            .strip().split()
            books_rec = recommend_books(L, keywordz_des, cat_des,\
            rat_des,page_des,a_z_val)
            display_books(books_rec)
            option = get_option()
        else:
            option = get_option()
    fp.close()

if __name__ == "__main__":
    main()
