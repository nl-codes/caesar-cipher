'''This program encrypts or decrypts message 
using caesar cipher which can be
read from console or file and
written to new file'''

def welcome():
    '''Prints text to welcome user to Caesar Cipher.'''
    print('Welcome to the Caesar Cipher')
    print('This program encrypts and decrypts text with the Caesar Cipher.')
    print()

def mode_validator():
    '''Asks user to input mode of conversion,
    Validates the mode of conversion and
    returns valid mode only'''

    valid_input = ('e','d')
    encrypt_decrypt = input('Would you like to encrypt (e) or decrypt (d): ')
    while True:
        if encrypt_decrypt.lower() in valid_input:
            break
        print('Invalid Mode')
        encrypt_decrypt = input('Would you like to encrypt (e) or decrypt (d): ')
    return encrypt_decrypt

def shift_key_validator():
    '''Asks user to input shift number,
    Validates the shift number and
    returns valid shift number only'''

    while True:
        shift_number = input('What is the shift number (0 - 25): ')
        try:
            valid_shift_number = int(shift_number)
            if valid_shift_number in range(0,26):
                break
            print('Shift number range = [0,25]')
        except ValueError:
            print('Invalid Shift')
    return valid_shift_number

def enter_message():
    '''Inputs and returns
    valid mode of conversion,
    text to encrypt/decrypt, and
    shfit number'''

    # Stores valid conversion mode
    conversion_mode = mode_validator()

    # Input message to encrypt/decrypt
    if conversion_mode == 'e':
        text_to_en_decrypt = input('What message would you like to encrypt: ')
    else:
        text_to_en_decrypt = input('What message would you like to decrypt: ')

    return conversion_mode, text_to_en_decrypt

def is_file(file_name):
    '''Checks if the user given file
    exists in the realtive directory
    or not'''
    while True:
        try:
            with open(file_name, mode="r", encoding="utf-8"):
                return True
        except FileNotFoundError:
            print("Invalid Filename")
            return False

def process_file(filename, encrypt_decrypt):
    '''Reads file given by user and
    Performs conversion given by user
    Either encryption or decryption'''
    result  = []
    key = shift_key_validator()
    with open(filename, mode='r', encoding="utf-8") as file:
        for line in file:
            if encrypt_decrypt == 'e':
                result.append(encrypt(line.strip(),key))
            else:
                result.append(decrypt(line.strip(),key))
        return result

def write_messages(list_to_write):
    '''Writes encrypted or decrypted message
    to results.txt'''
    with open("results.txt",mode="a",encoding="utf-8") as file:
        for line in list_to_write:
            file.writelines(line + '\n')
    print('Output written to results.txt')

def file_or_console():
    '''Inputs where to take message from
    validates inputs
    returns valid input only'''
    valid_input = ('f','c')
    while True:
        read_from = input('Would you like to read from a file (f) or the console (c)? ')
        if read_from.lower() in valid_input:
            break
        print('Invalid Reading format')
    return read_from

def message_or_file():
    '''Inputs and returns
    valid mode of conversion,
    text to encrypt/decrypt, and
    shfit number'''
    take_input_from = file_or_console()

    # If user selects to read from console
    if take_input_from == 'c':
        encrypt_decrypt, text_to_process = enter_message()
        return encrypt_decrypt,text_to_process,None

    # If user selects to read from file
    encrypt_decrypt = mode_validator()
    while True:
        file_name = input('Enter a filename: ')
        if is_file(file_name):
            return encrypt_decrypt,None,file_name

# Caesar Cipher letters
LETTERS = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plain_text, shift_number):
    '''Encrypts plain text to Caesar Cipher using index of Caesar Cipher letters:
    for shift of 3, index of current letter will shift forward by 3
    if current letter is a it will be replaced by d
    '''
    encrypted_text = ''
    for char in plain_text.lower():
    # if char is a space returns space
        if char == ' ':
            encrypted_text += ' '
        else:
            # else encrypts the text
            current_index = LETTERS.find(char)
            if current_index == -1:
                # if char is special symbol or number : keep as it is
                encrypted_text += char
            else:
                # else shift the alphabet using provided shift number
                new_index = current_index + shift_number
                if new_index >= 26:
                    new_index -=26
                encrypted_text += LETTERS[new_index]
    return encrypted_text.upper()


def decrypt(encryted_text, shift_number):
    '''Decrypts encrypted text to Plain text using index of Caesar Cipher letters:
    for shift of 3, index of current letter will shift backward by 3
    if current letter is a it will be replaced by w
    '''
    plain_text = ''
    for char in encryted_text.lower():
    # if char is a space returns space
        if char == ' ':
            plain_text += ' '
        else:
            # else decrypts the text
            index = LETTERS.find(char)
            if index == -1:
                # if char is special symbol or number : keep as it is
                plain_text += char
            else:
                # else shift the alphabet using provided shift number
                new_index = index - shift_number
                if new_index < 0:
                    new_index +=26
                plain_text += LETTERS[new_index]
    return plain_text.upper()

def run_again():
    '''Asks user to
    encrypt or decrypt more'''
    valid_input = ('y','n')
    while True:
        yes_or_no = input('Would you like to encrypt or decrypt another message? (y/n): ')
        if yes_or_no in valid_input:
            return bool(yes_or_no == 'y')

def main():
    '''1. prompts user to select mode,
    2. validates mode,
    3. prompts user to read from file or console,
    4. validates reading format,
    5. prompts user to enter message to encrypt or decrypt,
    6. prompts user to enter shift number,
    7. validates shift number,
    8. prompts user if they want to encrypt or decrypt another message,
    9. validates input if they want or not 
    10. if user doesn't want another, 
    11. then ends program,
    12. otherwies goes back to step 1.'''
    encrypt_or_decrypt, text_from_console, file_name = message_or_file()
    if text_from_console is None:
        list_of_processed_text = process_file(file_name, encrypt_or_decrypt)
        write_messages(list_of_processed_text)
    if file_name is None:
        shift_key = shift_key_validator()
        if encrypt_or_decrypt == 'e':
            text_encrypted = encrypt(text_from_console,shift_key)
            print(text_encrypted)
        else:
            text_decrypted = decrypt(text_from_console,shift_key)
            print(text_decrypted)
    if run_again():
        main()
    else:
        print('Thanks for using the program, goodbye!')

welcome()
main()
