################################################
# Programming Project 09
#
# function to open file
# function to read files
# function to fill completions
# function to find completions
# main function to go through inputs
# call open file, read file, and fill completions
# ask for input
# while loop for not equal to quit option
#     find completion for prefix if available
#     display results
# closing message
# main function required code
#
#
#################################################

'''
Main data structure is a dictionary
   word_dic[(i,ch)] = set of words with ch at index i
'''
import string

# function to open file
def open_file():
    '''
    This function prompts the user to enter a vocabulary file name.
    The program will try to open the data file.
    Returns: file pointer of wanted file (file object)
    '''
    while True:
        filename = input("\nInput a file name: ")
        try:
            fp = open(filename, 'r', encoding='UTF-8')
            break
        except FileNotFoundError:
            print("\n[Error]: no such file")
            continue
    return fp

# function to read files
def read_file(fp):
    '''
    This function uses the provided file pointer and reads the vocabulary data file. 
    It returns a set of words in the file
    fp: provided file pointer from open file (file object)
    Returns: a set of words in the file (set)
    '''
    word_set = set()
    for line in fp:
        # make a list of words
        words = line.split()
        for word in words:
            word = word.strip(string.punctuation)
            # dont add words with punctuation
            if not word.isalpha():
                continue
            else:
                # joining all the words with no punctuation
                new_word = "".join(
                    char for char in word if char not in string.punctuation)
                if new_word.isalpha() and len(new_word) > 1:
                    word_set.add(new_word.lower())
    return word_set

# function to fill completions
def fill_completions(words):
    """
    This function takes a set of words and returns a dictionary whose 
    keys are tuples and the values are sets
    words: set of words from read file (set)
    Returns: the completion dictionary (dict)
    """
    word_dic = {}
    # go thru each word in set of words
    for word in words:
        # get the index of each character in word
        for index, ch in enumerate(word):
            # make a key of the index and the character
            key_tup = (index, ch.lower())
            # if its in the dictionary, then add the next key
            if key_tup in word_dic:
                word_dic[key_tup].add(word.lower())
            # initialize if its not in the dictionary
            else:
                word_dic[key_tup] = {word.lower()}
    return word_dic

# function to find completions
def find_completions(prefix, word_dic):
    """
    This function takes a prefix of a word and a completions dictionary.
    prefix: user entered prefix (string)
    word_dic: completions dictionary from find completions (dict)
    Returns: a set of words in the completions dictionary that complete the 
    prefix, if any (set)
    """
    completions_set = set()
    # go thru each index in the prefix
    for index in range(len(prefix)):
        # make a key of the index and the character at that index
        key = (index, prefix[index])
        # if its in the dict then go thru
        if key in word_dic:
            if len(completions_set) == 0:
                completions_set = word_dic[key]
            # find the intersection at that key
            else:
                completions_set = completions_set & word_dic[key]
                if len(completions_set) == 0:
                    return set()
        # if its not in the dict then return empty set
        else:
            return set()
    #print(completions_set)
    return completions_set

# main function to go through inputs
def main():
    # call all of the functions
    fp = open_file()
    word_set = read_file(fp)
    words_comp = fill_completions(word_set)
    #promt for a prefix
    prefix = input("\nEnter a prefix (# to quit): ")
    #while its not equal to quit option
    while prefix != '#':
        #call find completions
        word_prefix = find_completions(prefix, words_comp)
        #join them and seperate with a string
        word_prefix = ', '.join(sorted(word_prefix))
        #if its not a empty set
        if word_prefix:
            print("\nThe words that completes {} are: {}".format(
                prefix, word_prefix))
        #if its empty
        else:
            print("\nThere are no completions.")
        prefix = input("\nEnter a prefix (# to quit): ")
    print('\nBye')


if __name__ == '__main__':
    main()
