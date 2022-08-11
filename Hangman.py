def check_valid_input(letter_guessed, old_letters_guessed):
    """check if the letter typed is valid.
    :param letter_guessed: letter_guessed value
    :param old_letters_guessed: old_letters_guessed value
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True / False 
    :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    return(bool((len(letter_guessed) == 1) and (letter_guessed.isalpha() == True) and (old_letters_guessed.count(letter_guessed) == 0) and (letter_guessed.isascii() == True)))

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """check if the letter typed is valid , and add it to the used letters.
    :param letter_guessed: letter_guessed value
    :param old_letters_guessed: old_letters_guessed value
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True / False , list , string
    :rtype: string , list
    """
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print('X', (' -> ').join(sorted(old_letters_guessed)), sep='\n')
        return False

def show_hidden_word(secret_word, old_letters_guessed):
    """check if a list of letters are exist in a givin word 
    :param secret_word: secret_word value
    :param old_letters_guessed: old_letters_guessed value
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True / False
    :rtype: bool 
    """
    blanks = ''
    for letter in secret_word.lower():
        if letter in old_letters_guessed:
            blanks += letter
        else:
            blanks += '_'
    return(" ".join(blanks))

def check_win(secret_word, old_letters_guessed):
    """check if a word exist in a givin list of letters 
    :param secret_word: secret_word value
    :param old_letters_guessed: old_letters_guessed value
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True / False
    :rtype: bool 
    """
    return all(element in old_letters_guessed for element in list(secret_word.lower()))

def choose_word(file_path, index):
    """return a word in a givin index from a text file
    :param file_path: file_path value
    :param index: index value
    :type secret_word: str
    :type old_letters_guessed: string
    :return: word
    :rtype: str 
    """
    with open(file_path, 'r') as f:
        f_data = (f.read()).split(' ')
        return(f_data[(int(index) % len(f_data)-1)])

def print_hangman(num_of_tries):
    """return a 'picture' according to the given integer
    :param num_of_tries: num_of_tries value
    :type secret_word: int
    :return: 'picture'
    :rtype: str 
    """
    HANGMAN_PHOTO = {}
    HANGMAN_PHOTO[0] = "x-------x"
    HANGMAN_PHOTO[1] = """
    x-------x
    |
    |
    |
    |
    |
    """
    HANGMAN_PHOTO[2] = """ 
    x-------x
    |       |
    |       0
    |
    |
    |
    """
    HANGMAN_PHOTO[3] = """ 
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """
    HANGMAN_PHOTO[4] = """  
    x-------x   
    |       0
    |      /|\\
    |
    |
    """
    HANGMAN_PHOTO[5] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """
    HANGMAN_PHOTO[6] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
    if(num_of_tries == 0):
        return(HANGMAN_PHOTO[0])
    elif(num_of_tries == 1):
        return(HANGMAN_PHOTO[1])
    elif(num_of_tries == 2):
        return(HANGMAN_PHOTO[2])
    elif(num_of_tries == 3):
        return(HANGMAN_PHOTO[3])
    elif(num_of_tries == 4):
        return(HANGMAN_PHOTO[4])
    elif(num_of_tries == 5):
        return(HANGMAN_PHOTO[5])
    elif(num_of_tries == 6):
        return(HANGMAN_PHOTO[6])

def open_screen():
    """returns a 'picture' and an integer
    :return: none
    :rtype: none 
    """
    HANGMAN_ART =("""      _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/""")
    global MAX_TRIES #יודע שהדבר אינו מקובל אך זהו משתנה שאינו משתנה ! על כן מעיף להגדירו פעם אחת.
    MAX_TRIES = 6 
    print(HANGMAN_ART, MAX_TRIES, sep='\n')

def main():
    open_screen()
    file_path = input('Please enter a path to text file: ')
    index = input('Please enter a number to get a random word: ')
    num_of_tries = 0
    secret_word_str = choose_word(file_path, index)
    old_letters_guessed = []
    print('Your corrent situation: %s' % print_hangman(num_of_tries), show_hidden_word(secret_word_str, old_letters_guessed), sep='\n')
    while(check_win(secret_word_str, old_letters_guessed) == False) and (num_of_tries < MAX_TRIES):
        letter_guessed = input('Please enter a letter to guess: ')
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            if ((secret_word_str).lower()).count(letter_guessed.lower()):
                print(show_hidden_word(secret_word_str, old_letters_guessed))
            else:
                num_of_tries += 1
                print("): %s" % print_hangman(num_of_tries), show_hidden_word(secret_word_str, old_letters_guessed), sep='\n')
    if check_win(secret_word_str, old_letters_guessed):
        print("Win! you got the secret word!")
    else:
        print("Lose , never mind try again soon!")
        
if __name__ == "__main__":
  main()