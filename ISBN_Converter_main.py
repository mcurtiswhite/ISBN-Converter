# The following program is an ISBN check digit verifier and converter.
# It can receive ISBN-10 and ISBN-13 input directly from the user or it
# can read ISBN numbers from a file to verify and convert. ISBN numbers
# can be loaded and saved via files and are stored in memory for use while
# the program is running. Data is validated to ensure that ISBN numbers are
# entered correctly. Files are validated to ensure data is loaded correctly
# and that existing data is not overwritten without permission. 

# Import modules.
import isbn_format
import verify
import convert
import file_manager

# Menu constants.
VERIFY_10 = 1
VERIFY_13 = 2
TEN_TO_THIRTEEN = 3
THIRTEEN_TO_TEN = 4
LOAD = 5
SAVE = 6
EXIT = 7

# Call the main function that runs the program.
def main():
    # Declare local variables.
    choice = 0
    # ISBN storage.
    isbn10 = '0000000000'
    isbn13 = '0000000000000'
    # ISBN display storage.
    isbn_pr = ''
    isbn_pr = ''

    # Call the isbn_format function to format ISBN numbers for display.
    isbn10_pr, isbn13_pr = isbn_format.hyphenate(isbn10, isbn13)

    while choice != EXIT:
        # Display the menu
        display_menu(isbn10_pr, isbn13_pr)
        
        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == VERIFY_10:
            # Option to use current ISBN-10.
            memory = str(input('Would you like to verify the current '
                               'ISBN-10 in memory? (y/n) ' ))
            if memory == 'y' or memory == 'Y':
                # Convert characters to uppercase.
                isbn10 = isbn10.upper()
                # Call the function to verify the check digit of the ISBN-10.
                isbn10 = verify.verify10(isbn10)
            else:
                # Get an ISBN-10 from the user.
                isbn10 = str(input('Enter an ISBN-10 (without hyphens): '))
                # Call the isbn10_check function to validate data.
                isbn10 = isbn10_check(isbn10)
                isbn10 = isbn10.upper()
                isbn10 = verify.verify10(isbn10)
            isbn10_pr, isbn13_pr = isbn_format.hyphenate(isbn10, isbn13)
            
        elif choice == VERIFY_13:
            # Option to use current ISBN-13.
            memory = str(input('Would you like to verify the current '
                               'ISBN-13 in memory? (y/n) ' ))
            if memory == 'y' or memory == 'Y':
                # Call the function to verify the check digit of the ISBN-13.
                isbn13 = verify.verify13(isbn13)
            else:
                # Get an ISBN-13 from the user.
                isbn13 = str(input('Enter an ISBN-13 (without hyphens): '))
                # Call the isbn13_check function to validate data.
                isbn13 = isbn13_check(isbn13)
                isbn13 = verify.verify13(isbn13)
            isbn10_pr, isbn13_pr = isbn_format.hyphenate(isbn10, isbn13)
            
        elif choice == TEN_TO_THIRTEEN:
            # Option to use current ISBN-10.
            memory = str(input('Would you like to convert the current '
                               'ISBN-10 in memory? (y/n) ' ))
            if memory == 'y' or memory == 'Y':
                # Convert characters to uppercase.
                isbn10 = isbn10.upper()
                # Call the function to convert an ISBN-10 to an ISBN-13.
                isbn13 = convert.convert10(isbn10)
            else:
                # Get an ISBN-10 from the user.
                isbn10 = str(input('Enter an ISBN-10 (without hyphens): '))
                # Call the isbn10_check function to validate data.
                isbn10 = isbn10_check(isbn10)
                isbn10 = isbn10.upper()
                isbn13 = convert.convert10(isbn10)
            isbn10_pr, isbn13_pr = isbn_format.hyphenate(isbn10, isbn13)
            
        elif choice == THIRTEEN_TO_TEN:
            # Option to use current ISBN-13.
            memory = str(input('Would you like to convert the current '
                               'ISBN-13 in memory? (y/n) ' ))
            if memory == 'y' or memory == 'Y':
                # Call the function to convert an ISBN-13 to an ISBN-10.
                isbn10 = convert.convert13(isbn13)
            else:
                # Get an ISBN-13 from the user.
                isbn13 = str(input('Enter an ISBN-13 (without hyphens): '))
                # Call the isbn13_check function to validate data.
                isbn13 = isbn13_check(isbn13)
                isbn10 = convert.convert13(isbn13)
            isbn10_pr, isbn13_pr = isbn_format.hyphenate(isbn10, isbn13)

        elif choice == LOAD:
            # Call the function to load ISBN numbers from a file.
            isbn10, isbn13 = file_manager.load(isbn10, isbn13)
            isbn10_pr, isbn13_pr = isbn_format.hyphenate(isbn10, isbn13)

        elif choice == SAVE:
            # Call the function to save the ISBN numbers to a file.
            file_manager.save(isbn10, isbn13)
        
        elif choice == EXIT:
            # Call the function to exit program.
            print('Exiting the program...')
            
        else:
            print('Error: Invalid selection.')

# The display_menu function displays the menu.
def display_menu(num1, num2):
    print('------------------------------------------')
    print('ISBN Verification and Conversion Program')
    print('ISBN-10 in memory:', num1)
    print('ISBN-13 in memory:', num2)
    print('------------------------------------------')
    print('Please choose one of the following:')
    print('1) Verify the check digit of an ISBN-10.')
    print('2) Verify the check digit of an ISBN-13.')
    print('3) Convert an ISBN-10 to an ISBN-13.')
    print('4) Convert an ISBN-13 to an ISBN-10.')
    print('5) Load ISBN numbers from file.')
    print('6) Save ISBN numbers to file.')
    print('7) Exit.')

# The isbn10_check function validates the ISBN-10 input.
def isbn10_check(num):
    # ISBN integer check variable.
    isbn_check = ''
    
    # Store input minus check digit for validation.
    isbn_check = num[0:9]
    
    # Loop to check if the ISBN-10 is the correct length or if
    # the user entered numbers.
    while len(num) != 10 or not isbn_check.isdigit():
        print('Invalid ISBN-10. Please try again.')
        num = str(input('Enter an ISBN-10 (without hyphens): '))
        isbn_check = num[0:9]

    # Return the ISBN-10.
    return num

# The isbn13_check function validates the ISBN-13 input.
def isbn13_check(num):
    # ISBN integer check variable
    isbn_check = ''

    # Store input for validation.
    isbn_check = num

    # Loop to check if the ISBN-10 is the correct length or if
    # the user entered numbers.
    while len(num) != 13 or not num.isdigit():
        print('Invalid ISBN-13. Please try again.')
        num = str(input('Enter an ISBN-13 (without hyphens): '))
        isbn_check = num

    # Return the ISBN-13.
    return num
    

# Call the main function.
main()
