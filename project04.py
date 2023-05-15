######################
#Programming Project 04
#
#function to display menu
#function for number to binary
#function for binary to number
#function for base to binary
#helper function for encode
#function for encoding messages
#function for decoding messages
#main function for inputs 
#   ask for selection 
#   while loop for options
#       if/elif/else statements for each option
#   while loop for closing option
#main function required code
#######################

#function that displays menu options
def display_menu():
    """
    Displays menu of options
    Returns: menu of options
    """
    MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             E. Encode an image with a text.
             D. Decode an image.
             M. Display the menu of options.
             X. Exit from the program.'''
    print(MENU)
# function that converts numbers to their binary strings
def numtobase( N, B ):
    """
    Converts a decimal number to a string in its binary format.
    N: a non-negative interger (int)
    cannot be a float
    B: base value for conversion (int)
    must be between 2 and 10
    Returns: the string binary format of the entered interger (str)
    """
    binarystring =  ''
    if N == 0:
        return ''
    while N > 0:
        binarystring += str(N % B)
        N = N//B 
    return binarystring[::-1].zfill(8)
#function that converts binary strings back to their number 
def basetonum( S, B ):
    """
    Converts a binary string format of a number to its decimal value.
    S: binary string representing a number (str)
    B: base value of binary string number (int)
    must be between 2 and 10
    Returns: Decimal number value of the given binary string (int)
    """
    dec = 0
    power = 0
    if S == ' ' or S == '':
        return 0
    S = int(S)
    while (S) > 0:
        dec += B ** power * (S%10)
        S //= 10
        power +=1
    return dec
#function that converts bases to their binary strings
def basetobase(B1,B2,s_in_B1):
    """
    Converts two base values into a string representing a number in base 2.
    B1: a base value (int)
    must be between 2 and 10
    B2: a base value(int)
    must be between 2 and 10
    s_in_B1: a string representing a number in base 1(str)
    Returns: a string representing the same number in s_in_B1 as in B2
    """
    dec = basetonum(s_in_B1, B1)
    if s_in_B1 == '0':
        return ''
    if s_in_B1 == '':
        return s_in_B1
    while (B2 > int(dec)):
        base_B2 = dec
        base_B2 = str(base_B2)
        return base_B2.zfill(8)
    while (B2 <= int(dec)):
        base_B2 = numtobase(dec, B2)
        if len(base_B2) > 8:
            return base_B2.zfill(16)
        else:
            return base_B2.zfill(8)
# helper function to convert a string of text to binary
def text_tobin(text):
    """
    Converts a string of text to its binary string format.
    text: a string of letters (str)
    Returns:the binary string format of the given letters (str)
    """
    newtext= ''
    for ch in (text):
        dec = ord(ch) 
        changed_text = numtobase(dec, 2)
        newtext += changed_text
    return newtext
#function that encodes a given text into an image 
def encode_image(image,text,N):
    """
    Embeds a given text into a binary string image.
    image: a binary string that represents an image (str)
    text: a string message of letters to be hidden in the image (str)
    N: a number that represents how many bits are in each pixel (int)
    Returns: the encoded binary string with the new embeded message (str)
    """
    encoded_image = ''
    if image == '':
        return ''
    if text == '':
        return image
    newtext = text_tobin(text)
    if len(newtext) > len(image):
        return None
    count = 0
    for ch in range(0, len(image)):
        #check to see if image or newtext should be added
        if (ch +1) % int(N) != 0 or ch == 0:
            encoded_image += image[ch]
        else:
            try:
                #check to see if the values are equal in order to add
                if image[ch] == newtext[count]:
                    encoded_image += image[ch]
                else:
                    encoded_image += newtext[count]
            #fix for when there is still image left but no text
            except IndexError:
                encoded_image += image[ch]
            count += 1
    return encoded_image
#function that decodes the text that is hidden in an image
def decode_image(stego,N):
    """
    Decodes a hidden message from inside a binary string.
    stego: a binary string that inlcudes a message (str)
    N: a number representing how many bits in each pixel (int)
    Returns : a string of letters that is the hidden message (str)
    """
    text_out = ''
    intstego = int(len(stego))
    #converting stego into concatenated string of readable binary numbers
    for ch in range(0, intstego, int(N)):
        text_out += stego[ch:ch + int(N)][-1]
    final_decoded = ''
    int_text = int((len(text_out)//8)*8)
    #converting binary numbers back to letters
    for i in range (0,int_text,8):
        letter = ''
        letter = (text_out[i:i+8])
        new_letter = basetonum(letter,2)
        final_decoded += chr(new_letter)
    return final_decoded
     
#main function that interacts with user/asks for inputs
def main():
    """
    Goes through each menu option and asks for inputs/checks parameters.
    Returns calculated answers for each of the above functions.
    """
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''

    print(BANNER)
    display_menu()
    answer = input("\n\tEnter option: ")
    while answer != 'X' or answer != 'x':
        if answer == 'A' or answer == 'a':
            N = input("\n\tEnter N: ")
            while not N.isnumeric():
                print("\n\tError: {} was not a valid non-negative integer."\
                .format(N))
                N = input("\n\tEnter N: ")
            N= int(N)
            B = input("\n\tEnter Base: ")
            while (int(B) <= 1):
                print("\n\tError: {} was not a valid integer between 2 and "
                "10 inclusive.".format(B))
                B = input("\n\tEnter Base: ")
            while int(B) >= 11:
                print("\n\tError: {} was not a valid integer between 2 and "
                "10 inclusive.".format(B))
                B = input("\n\tEnter Base: ")
                if int(B) <= 1:
                    print("\n\tError: {} was not a valid integer between 2 "
                    "and 10 inclusive.".format(B))
                    B = input("\n\tEnter Base: ")
            B= int(B)
            binarystring = numtobase(N, B)
            while binarystring.isdigit:
                print ("\n\t {} in base {}: {}".format(N,B,numtobase(N, B)))
                break
            answer = input("\n\tEnter option: ")            
        elif answer =='B' or answer == 'b' :
            S = input("\n\tEnter string number S: ")
            B = input("\n\tEnter Base: ")
            while (int(B) <= 1):
                print("\n\tError: {} was not a valid integer between 2 and"
                " 10 inclusive.".format(B))
                B = input("\n\tEnter Base: ")
            while int(B) >= 11:
                print("\n\tError: {} was not a valid integer between 2 and"
                " 10 inclusive.".format(B))
                B = input("\n\tEnter Base: ")
                if int(B) <= 1:
                    print("\n\tError: {} was not a valid integer between 2"
                    " and 10 inclusive.".format(B))
                    B = input("\n\tEnter Base: ")
            B= int(B)
            dec = str(basetonum(S, B))
            while dec.isnumeric():
                print("\n\t {} in base {}: {}".format(S,B,basetonum(S, B)))
                break
            answer = input("\n\tEnter option: ")
        elif answer == 'C' or answer == 'c':
            B1 = input("\n\tEnter base B1: ")
            while (int(B1) <= 1):
                print("\n\tError: {} was not a valid integer between 2 and"
                " 10 inclusive.".format(B1))
                B1 = input("\n\tEnter base B1: ")
            while int(B1) >= 11:
                print("\n\tError: {} was not a valid integer between 2 and"
                " 10 inclusive.".format(B1))
                B1 = input("\n\tEnter base B1: ")
                if int(B1) <= 1:
                    print("\n\tError: {} was not a valid integer between 2"
                    " and 10 inclusive.".format(B1))
                    B1 = input("\n\tEnter base B1: ")
            B1 = int(B1)
            B2 = input("\n\tEnter base B2: ")
            while (int(B2) <= 1):
                print("\n\tError: {} was not a valid integer between 2 and"
                " 10 inclusive.".format(B2))
                B2 = input("\n\tEnter base B2: ")
            while int(B2) >= 11:
                print("\n\tError: {} was not a valid integer between 2 and"
                " 10 inclusive.".format(B2))
                B2 = input("\n\tEnter base B2: ")
                if int(B2) <= 1:
                    print("\n\tError: {} was not a valid integer between 2"
                    " and 10 inclusive.".format(B2))
                    B2 = input("\n\tEnter base B2: ")
            B2 = int(B2)
            s_in_B1 = input ("\n\tEnter string number: ")
            print("\n\t {} in base {} is {} in base {}...".format(s_in_B1,B1,\
            basetobase(B1,B2,s_in_B1),B2))
            answer = input("\n\tEnter option: ")
        elif answer == 'E' or answer == 'e':
            image = input("\n\tEnter a binary string of an image: ")
            N = input("\n\tEnter number of bits used for pixels: ")
            text = input("\n\tEnter a text to hide in the image: ")
            encoded_image = encode_image(image,text,N)
            if encoded_image == '' or encoded_image == None:
                print("\n\tImage not big enough to hold all the text to"
                " steganography")
            else:
                print("\n\t Original image: {}".format(image))
                print("\n\t Encoded image: {}".format(encoded_image))
            answer = input("\n\tEnter option: ")
        elif answer == 'D' or answer == 'd':
            stego = input("\n\tEnter an encoded string of an image: ")
            N = input("\n\tEnter number of bits used for pixels: ")
            final_decoded = decode_image(stego,N)
            print ("\n\t Original text: {}".format(final_decoded))
            answer = input("\n\tEnter option: ")
        elif answer == 'M':
            display_menu()
            answer = input("\n\tEnter option: ")
        else:
            if answer == 'X' or answer == 'x':
                break
            else:
                print("\nError:  unrecognized option [{}]".format(\
                answer.upper()))
                display_menu()
                answer = input("\n\tEnter option: ")
    while answer == 'X' or answer == 'x':
       print('\nMay the force be with you.')
       break
if __name__ == '__main__': 
    main()

