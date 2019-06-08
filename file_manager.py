# Import modules.
import os.path

# The load function loads ISBN numbers from a file.
def load(num1, num2):
    # Get a filename from the user.
    print('Note: the file must contain an ISBN-10 and ISBN-13.')
    filename = str(input('Please enter the filename to load: '))

    # Loop to check if the file exists.
    while not os.path.exists(filename):
        filename = str(input('File does not exist. Please enter a ' +
                             'valid filename: '))

    # Open the file.
    infile = open(filename, 'r')
    
    # Read the data from the file.
    ten = infile.readline()
    thirteen = infile.readline()

    # Strip the newline from each string.
    ten = ten.rstrip('\n')
    thirteen = thirteen.rstrip('\n')

    # Close the file.
    infile.close()

    # Validate data.
    ten_check = ten
    thirteen_check = thirteen
    if len(ten) != 10 or not ten_check.isdigit():
        print()
        print('Invalid ISBN-10. Please try again.')
        print()
        print()
        ten = num1
        thirteen = num2
        return num1, num2
    if len(thirteen) != 13 or not thirteen_check.isdigit():
        print()
        print('Invalid ISBN-13. Please try again.')
        print()
        print()
        ten = num1
        thirteen = num2
        return num1, num2

    # Display confirmation message.
    print()
    print('***** ' + filename + ' has been loaded! *****')
    print()
    print()
    
    # Return the contents.
    return ten, thirteen

# The save function saves the ISBN numbers to a file.
def save(ten, thirteen):
    # Get a filename from the user.    
    filename = str(input('Please enter a filename to save to: '))

    # Variable to validate file.
    file_check = filename

    # Check to save file if it does not exist.
    if not os.path.exists(file_check):
        create(filename, ten, thirteen)
        file_check = ''

    else:
        
        # Loop to check if the file exists.
        while os.path.exists(file_check):
            confirm = str(input('This file already exists. Are you sure you ' +
                                    'want to overwrite this file? (y/n) '))

            if confirm == 'y' or confirm == 'Y':
                # Call the create function to save the file.
                create(filename, ten, thirteen)
                # Clear file_check to end loop.
                file_check = ''

            else:
                filename = str(input('Please enter a filename to save to: '))
                file_check = filename
                # Save the file if it does not exist.
                if not os.path.exists(file_check):
                    create(filename, ten, thirteen)
                    file_check = ''

# The create function opens a file, writes data to it, and closes it, displaying
# a confirmation message when finished.
def create(file, num1, num2):

    # Create/open the file.
    outfile = open(file, 'w')

    # Write data to file.
    outfile.write(num1 + '\n')
    outfile.write(num2 + '\n')

    # Close the file.
    outfile.close()

    # Display confirmation message.
    print()
    print('***** Your ISBN numbers have been saved to ' + file +'! *****')
    print()
    print()

    return
